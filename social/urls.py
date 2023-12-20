from django.conf.urls.static import static
from django.urls import path

from narxozsocial import settings
from . import views


urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('base/', views.base, name='base'),
    path('main/', views.main_page, name='main'),
    path('friends/', views.friends_view, name='friends'),
    path('add/', views.add, name='add'),
    path('chat/', views.chat, name='chat'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),
    path('posts/', views.posts_view, name='posts'),
    path('groups/', views.groups_view, name='groups'),
    path('profile_friends/', views.profile_friends_view, name='profile_friends'),
    path('activity/', views.activity_view, name='activity'),
    #path('profile/details/', views.profile_details, name='profile_details'),
    path('settings/info/', views.settings_info, name='settings_info'),
    path('add/', views.add_post, name='add_post'),
    path('delete_account/',views.delete_account, name='delete_account'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
