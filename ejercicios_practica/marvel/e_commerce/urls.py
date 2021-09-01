from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *


urlpatterns = [
    # NOTE: e_commerce base:
    #path('prueba-form', PruebaFormView.as_view()),
    
    #TODO: Tarea!
    #path('prueba-form', PruebaFormView.as_view()),
    path('home', HomeView.as_view(), name='home'), 
    path('login', LoginFormView.as_view(), name='login'),
    path('logout', MyLogoutView.as_view(), name='logout'),
    path('user', UserDataView.as_view(), name='user'),
    path('cart', CartView.as_view(), name='cart'),
    path('wish', WishView.as_view(), name='wish'),
    ]