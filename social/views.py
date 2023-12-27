from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm, PostForm, UserProfileForm, UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from .models import UserProfile, Post
from django.contrib.auth import logout


@login_required
def base(request):
    user_profile = request.user.userprofile  # предполагаем, что у пользователя есть ассоциированный профиль
    return render(request, 'social/base.html', {'user_profile': user_profile})

def main_page(request):
    # Получение всех постов из базы данных
    posts = Post.objects.all()

    # Ваш остальной код
    return render(request, 'social/main_page.html', {'posts': posts})

def friends_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'social/friends.html', {'user_profile': user_profile})

@login_required
def add(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = user_profile
            post.save()
            messages.success(request, 'Your post was successfully created!')
            return redirect('main')
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    else:
        form = PostForm()

    return render(request, 'social/add.html', {'user_profile': user_profile, 'form': form})

def chat(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'social/chat.html', {'user_profile': user_profile})

def settings(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'social/settings.html', {'user_profile': user_profile})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Обработка данных регистрации
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Аутентификация пользователя после успешной регистрации
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user:
                login(request, authenticated_user)

                # Уведомление об успешной регистрации
                messages.success(request, 'Вы успешно зарегистрировались!')

                # Перенаправление на страницу логина
                return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'social/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Перенаправление на главную страницу (main)
                return redirect('main')  # Используйте 'social:main' вместо 'main'
            else:
                return render(request, 'social/login.html', {'form': form, 'error_message': 'Invalid login credentials'})
    else:
        form = LoginForm()

    return render(request, 'social/login.html', {'form': form})


def logout_view(request):
    # Выполнение выхода пользователя
    logout(request)
    # Перенаправление на страницу входа или другую страницу
    return redirect('login')  # Замените 'social:login' на ваш URL для страницы входа


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        # Получите новости из базы данных (вам может потребоваться импортировать вашу модель News)


        # Передайте данные в контекст шаблона


        return render(request, 'social/main_page.html', )


def posts_view(request):
    return render(request, 'social/posts.html')

def groups_view(request):
    return render(request, 'social/groups.html')

def profile_friends_view(request):
    return render(request, 'social/profile_friends.html')

def activity_view(request):
    return render(request, 'social/activity.html')


def settings_info(request):
    content_id = request.GET.get('content', 'account-info')
    template_name = f'social/settings_{content_id}.html'

    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your settings were successfully saved!')
            return redirect('settings_info')
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    else:
        form = UserProfileForm(instance=user_profile)

    context = {'form': form, 'content_id': content_id}
    return render(request, template_name, context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post was successfully created!')
            return redirect('news')
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    else:
        form = PostForm()

    return render(request, 'social/add.html', {'form': form})

def update_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправьте на страницу профиля
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'social/update_profile.html', {'form': form})

@login_required
@login_required
def delete_account(request):
    if request.method == 'POST':
        # Удаление пользователя и выход из системы
        request.user.delete()

        logout(request)

        # Редирект на страницу логина или другую страницу по вашему выбору
        return redirect('login')

    return render(request, 'social/delete_account.html')

@login_required
def profile(request):
    user_profile = request.user.userprofile  # предполагаем, что у пользователя есть ассоциированный профиль
    return render(request, 'social/profile.html', {'user_profile': user_profile})

