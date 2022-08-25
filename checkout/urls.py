from . import views

from django.urls import path

urlpatterns = [
    path('checkout/', views.checkoutview, name='checkout_view2'),
]