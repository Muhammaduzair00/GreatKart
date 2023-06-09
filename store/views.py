from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import category


def store(request, category_slug=None):
    categrios = None
    products = None
    if category_slug !=None:
        categrios = get_object_or_404(category,slug=category_slug)
        products = Product.objects.filter(category=categrios, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
            'products': products,
            'product_count': product_count,
    }
    return render(request,'store/store.html',context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug= product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html',context)
