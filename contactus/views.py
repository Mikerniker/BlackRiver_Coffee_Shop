from django.shortcuts import render

# Create your views here.


def contact_view(request):
    if request.method == 'POST':
        name = request.POST['yourName']
        email = request.POST['yourEmail']
        message = request.POST['yourMessage']
        print(name, email, message)
        return render(request, 'contact.html', {'message_received': "Thank you for your message! We'll get back to you within 24 hours."})
    else:
        return render(request, 'contact.html')