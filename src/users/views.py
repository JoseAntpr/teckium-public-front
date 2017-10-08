from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from blogs.decorators import jwt_required
from users.requests_api import tk_authenticate
from users.forms import LoginForm


class LoginView(View):

    def get(self, request):
        """
        Presenta el formulario de login a un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

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
                url = request.GET.get('next', 'index')  # Permite redirigir a la url desde donde venga el usuario al hacer login
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
    @method_decorator(jwt_required)
    def get(self, request, *args, **kwargs):
        """
        Presenta el formulario de login a un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

        print(kwargs['profile'])

        '''context = {
            'form': LoginForm()
        }'''

        return render(request, "signin.html")
