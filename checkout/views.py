from django.shortcuts import render

# Create your views here.

def checkoutview(request):
    if request.method == 'POST':
        coffee = request.POST.get('coffee')
        price = request.POST.get('coffee_price')
        quantity = request.POST.get('quantity')
        total_cost = int(price) * int(quantity)
        print(coffee, price)
        return render(request, 'checkout.html', {'coffee_order': coffee,
                                                 'coffee_order_price': price,
                                                 'coffee_quantity': quantity,
                                                 'coffee_total': total_cost})
    else:
        return render(request, 'checkout.html')
