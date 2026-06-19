from django.shortcuts import render
from .models import Product

# Create your views here.
def store(req):
    products = Product.objects.all().filter(is_Available = True)
    product_count = products.count()
    
    context = {
        'products':products,
        'product_count':product_count
    }
    
    return render(req,'store/store.html',context)