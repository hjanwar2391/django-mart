from django.shortcuts import render

# Create your views here.

def orders(request):
    return render( request, 'orders/order_complete.html')