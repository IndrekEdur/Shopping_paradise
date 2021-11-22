from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Category
from datetime import datetime
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
import pdb

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    Product.objects.order_by().filter()
    template_name = 'products/product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')

from .forms import MyForm
def my_form(request):
    # If this is a POST request we need to process the form data.

    if request.method == 'POST':
        # Create a form instance and populate it
        # with data from the request.
        form = MyForm(request.POST)
        # Check whether it is valid.
        pdb.set_trace()
        if form.is_valid():
            # Does any data require extra processing?
            # If so, do it in form.cleaned_data as required.
            # ...
            # Redirect to a new URL.
            return HttpResponseRedirect('/thank-you')
        else:
            # Redirect back to the same page if the data
            # was invalid.
            return render(request, 'my_form.html', {'form': form})

    # If a GET (or any other method) we will create a blank form.
    else:
        form = MyForm()
    return render(request, 'my_form.html', {'form': form})

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    Product.objects.order_by().filter()
    template_name = 'category_create.html'
    fields = '__all__'
    success_url = reverse_lazy('category_list')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_update.html'
    context_object_name = 'category'
    fields = '__all__'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')







# def products(request):
#     Category(name="laptop").save()
#     Product(name="Mac", price=200.00, category_id=1).save()
#     return HttpResponse("DONE")