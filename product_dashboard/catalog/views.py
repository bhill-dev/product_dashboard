from django.shortcuts import render
from .models import Category, Tag, Product


def index(request):
    num_products = Product.objects.all().count()
    num_tags = Tag.objects.all().count()
    num_categories = Category.objects.all().count()

    context = {
        'num_products': num_products,
        'num_categories': num_categories,
        'num_tags': num_tags
    }

    return render(request, 'index.html', context=context)
