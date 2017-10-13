import json

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from blogs.decorators import jwt_required
from blogs.requests_api import get_tags
from users.requests_api import tk_authenticate, create_user, tk_refresh, put_profile
from users.forms import LoginForm, RegisterForm, ProfileForm, UserForm


class LoginView(View):
    def get(self, request):
        """
        Presenta el formulario de login a un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

        token = request.session.get("jwt", None)
        new_token = None
        if token:
            token = {'token': token}
            data = tk_refresh(token)
            if data:
                new_token = data['token']
                request.session["jwt"] = new_token
                url = request.GET.get('next', 'index')  # Permite redirigir a la url desde donde venga el usuario al hacer login
                return redirect(url)

        context = {
            'form': LoginForm()
        }

        return render(request, 'login.html', context)

    def post(self, request):
        """
        Hace login de un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

        form = LoginForm(request.POST)
        context = dict()
        if form.is_valid():
            data = form.cleaned_data
            token = tk_authenticate(data)
            if token is not None:
                # Usuario autenticado
                request.session["default-language"] = "es"
                url = request.GET.get('next',
                                      'index')  # Permite redirigir a la url desde donde venga el usuario al hacer login
                request.session["jwt"] = token['token']
                return redirect(url)
            else:
                # Usuario no autenticadopero
                messages.warning(request, 'Usuario o contraseña incorrecta.')
        context['form'] = form

        return render(request, 'login.html', context)


class LogoutView(View):
    @method_decorator(jwt_required)
    def get(self, request, *args, **kwargs):
        try:
            del request.session['jwt']
            url = request.GET.get('next', 'index')
            return redirect(url)
        except KeyError:
            pass

        url = request.GET.get('next', 'login')
        return redirect(url)


class SigninView(View):
    #@method_decorator(jwt_required)
    def get(self, request, **kwargs):
        """
        Presenta el formulario de registro de un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

        #print(kwargs['user'])
        token = request.session.get("jwt", None)
        new_token = None
        if token:
            token = {'token': token}
            data = tk_refresh(token)
            if data:
                new_token = data['token']
                request.session["jwt"] = new_token
                url = request.GET.get('next', 'index')  # Permite redirigir a la url desde donde venga el usuario al hacer login
                return redirect(url)

        context = {
            'form': RegisterForm()
        }

        return render(request, 'signin.html', context)

    def post(self, request):
        """
        Hace el registro de un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

        form = RegisterForm(request.POST)
        context = dict()
        if form.is_valid():
            data = form.cleaned_data

            if data.get('password') == data.get('password2'):
                request_data = create_user(data)

                if request_data is not None:
                    data = {'username': data.get('username'),
                            'password': data.get('password')}
                    token = tk_authenticate(data)
                    # Usuario autenticado
                    request.session["default-language"] = "es"
                    url = request.GET.get('next', 'index')  # Permite redirigir a la url desde donde venga el usuario al hacer login
                    request.session["jwt"] = token['token']
                    return redirect(url)
                else:
                    # Usuario no autenticadopero
                    messages.warning(request, 'El usuario ya existe.')

            else:
                # Usuario no autenticadopero
                messages.warning(request, 'Las contraseñas no conciden.')

        context['form'] = form

        return render(request, 'signin.html', context)


class ProfileView(View):
    @method_decorator(jwt_required)
    def get(self, request, **kwargs):
        """
        Presenta los datos del perfil del usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

        user = kwargs['user']
        tags = get_tags()

        context = {
            'userForm': UserForm(user),
            'profileForm': ProfileForm(user.get('profile')),
            'tags': tags['results'],
            'user': user
        }

        return render(request, 'profile.html', context)

    @method_decorator(jwt_required)
    def post(self, request, **kwargs):
        """
        Actualiza los datos del perfil del usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        user = kwargs['user']
        tags = get_tags()

        userForm = UserForm(request.POST)
        profileForm = ProfileForm(request.POST, request.FILES)

        context = dict()
        if userForm.is_valid() and profileForm.is_valid():
            context = userForm.cleaned_data
            file = {
                'profile.avatar': profileForm.cleaned_data.get('avatar')
            }
            context['profile.bio'] = profileForm.cleaned_data.get('bio')

            result = put_profile(user.get('id'), file, context)

            if result:
                messages.success(request, "Se ha actualizado correctamente.")

                return HttpResponseRedirect(reverse('profile'))
            else:
                messages.warning(request, "No se ha podido actualizar.")

        context = {
            'userForm': userForm,
            'profileForm': profileForm,
            'tags': tags['results'],
            'user': user
        }

        return render(request, 'profile.html', context)
