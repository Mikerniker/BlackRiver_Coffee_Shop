from django.shortcuts import render

# Create your views here.
from . models import Coffee
from django.views import generic


def home_view(request):
    if request.method == 'POST':
        email = request.POST['subscribeEmail']
        print(email)
        return render(request, 'coffee_shop.html', {'email_received': "Thank you for subscribing!"})
    else:
        return render(request, 'coffee_shop.html')


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ContactView(generic.TemplateView):
    template_name = 'contact.html'


class CoffeeList(generic.ListView):
    queryset = Coffee.objects.filter(status=1)
    template_name = 'coffee_products.html'


class CheckoutView(generic.TemplateView):
    template_name = 'checkout.html'


class RecipesView(generic.TemplateView):
    template_name = 'recipes.html'
