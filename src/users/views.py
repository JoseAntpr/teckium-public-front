from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from users.api import tk_authenticate
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
                return redirect(url)
            else:
                # Usuario no autenticadopero
                messages.warning(request, 'Usuario o contraseña incorrecta.')
        context['form'] = form

        return render(request, 'login.html', context)


def singin(request):
    return render(request, "singin.html")
