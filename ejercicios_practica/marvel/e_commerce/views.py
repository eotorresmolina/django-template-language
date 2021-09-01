from typing import ClassVar
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

# Importamos vistas genericas:
from django.views.generic import TemplateView, FormView


# Importamos los modelos que vamos a usar:
from django.contrib.auth.models import User
from e_commerce.models import *

# Importo el formulario:
from e_commerce.forms import LoginForm

# Importamos el módulo authenticate
from django.contrib.auth import authenticate

# Importo la vista para poder realizar un Logueo.
from django.contrib.auth.views import LoginView, LogoutView


class LoginFormView(LoginView):
    '''
    Creo una clase con un Formulario dedicado
    al login de un usuario.
    Dentro del contexto obtiene la variable
    "form" con los datos del formulario.
    '''

    # Template a renderizar
    template_name = 'e-commerce/login.html'
    #success_url = 'home'

    # Agrego algunas variables a mi contexto.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Login'
        context['title'] = 'Log In'
        return context

    # En caso de que el Login sea exitoso, 
    # le indico a donde debe redirigirse.
    def get_success_url(self):
        return'home'


class MyLogoutView(LogoutView):
    template_name = 'e-commerce/logout.html'


# Vista basada en Clase que muestra un
# listado de los datos del usuario logueado.
class UserView(TemplateView):
    template_name = 'e-commerce/user.html'


class HomeView(TemplateView):
    template_name = 'e-commerce/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        username = ''

        if self.request.user.is_authenticated:
            username = self.request.user.username

        context['username'] = username

        return context


class UserDataView(TemplateView):
    template_name = 'e-commerce/user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            if self.request.user.is_authenticated:
                id_user = self.request.user.pk  # Obtengo el 'id' del usuario authenticado.
                queryset = User.objects.filter(id=id_user)
                user_data = queryset.values().first()
                context['user_data'] = user_data
        except:
                context['user_data'] = {'error': 'unauthenticated user'}

        return context
            

class CartView(TemplateView):
    template_name = 'e-commerce/comic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            # Pregunto si el usuario está authenticado, de ser
            # así, obtengo su id para luego obtener los detalles de los 
            # comics que tiene en el carrito.
            if self.request.user.is_authenticated:
                user_id= self.request.user.id
                wish_obj = WishList.objects.filter(user_id=user_id, cart=True)    # Obtengo los comics que están en el carrito.
                ids= [id[0] for id in wish_obj.values_list()]       # Obtengo los ids de dichos comics

                comic_obj = Comic.objects.filter(id__in=ids)   # Obtengo el objeto comic.
                comics = comic_obj.values()     # Obtengo una lista de diccionarios con los detalles de cada comic
                
                context['comics'] = comics.values()
                
        except:
            context['comics'] = {'error': 'unauthenticated user'}

        return context


class WishView(TemplateView):
    template_name = 'e-commerce/comic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            # Pregunto si el usuario está authenticado, de ser
            # así, obtengo su id para luego obtener los detalles de los 
            # comics que tiene en el carrito.
            if self.request.user.is_authenticated:
                user_id= self.request.user.id
                wish_obj = WishList.objects.filter(user_id=user_id, favorite=True)    # Obtengo los comics que están en el carrito.
                ids= [id[0] for id in wish_obj.values_list()]       # Obtengo los ids de dichos comics

                comic_obj = Comic.objects.filter(id__in=ids)   # Obtengo el objeto comic.
                comics = comic_obj.values()     # Obtengo una lista de diccionarios con los detalles de cada comic
                
                context['comics'] = comics.values()
                
        except:
            context['comics'] = {'error': 'unauthenticated user'}

        return context




# class PruebaView(TemplateView):
#     template_name = 'e-commerce/prueba_form.html'


# class PruebaFormView(FormView):
#     template_name = 'e-commerce/base.html'
#     form_class = LoginForm
#     success_url = 'thanks'

#     def form_valid(self, form):

#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']

#         return super().form_valid(form)


#     def post(self, request, *args, **kwargs):
#         form = self.get_form()

#         username = request.POST['username']
#         password = request.POST['password']

#         account = authenticate(username=username, password=password)
        
#         if form.is_valid() and account:
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
    



# class ThanksView(TemplateView):
#     template_name = 'e-commerce/thanks.html'


