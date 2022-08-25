from . import views

from django.urls import path

urlpatterns = [

    path('about/', views.AboutView.as_view(), name='about_view'),
    path('contact/', views.ContactView.as_view(), name='contact_view'),
    path('coffee/', views.CoffeeList.as_view(), name='coffee_view'),
    path('recipes/', views.RecipesView.as_view(), name='recipe_view'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout_view'),
    path('', views.home_view, name='home_view'),
]