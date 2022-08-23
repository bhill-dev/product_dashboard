from django.shortcuts import render
from .models import Category, Tag, Product
from .filters import ProductFilter
from django.views.generic import ListView, DetailView


def index(request):
    num_products = Product.objects.all().count()
    num_tags = Tag.objects.all().count()
    num_categories = Category.objects.all().count()
    products = Product.objects.all()
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs

    context = {
        'num_products': num_products,
        'num_categories': num_categories,
        'num_tags': num_tags,
        'products': products,
        'my_filter': my_filter
    }

    return render(request, 'index.html', context=context)


