from django.shortcuts import render
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Budget, Budget_item
from datetime import datetime
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
import pdb

class BudgetListView(ListView):
    model = Budget
    template_name = 'budgets/Budget_list.html'
    context_object_name = 'budgets'

class BudgetCreateView(CreateView):
    model = Budget
    Budget.objects.order_by().filter()
    template_name = 'budgets/Budget_create.html'
    fields = '__all__'
    success_url = reverse_lazy('budget_list')

class BudgetDetailView(DetailView):
    queryset = Budget.objects

    template_name = 'budgets/Budget_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['budget_items'] = Budget_item.objects.all

        amount = 0
        #for item in Budget_item.objects:
            #print(item)
            #b = Budget_item.calc_total(item)
            #amount = (amount + b)
        context['budget_total'] = amount

        return context




class BudgetUpdateView(UpdateView):
    model = Budget
    template_name = 'budgets/Budget_update.html'
    context_object_name = 'budget'
    fields = '__all__'
    success_url = reverse_lazy('budget_list')

class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = 'budgets/Budget_delete.html'
    context_object_name = 'budget'
    success_url = reverse_lazy('budget_list')

#BUDGET ITEMS

class Budget_itemListView(ListView):
    model = Budget_item
    template_name = 'budgets/Budget_detail.html'
    context_object_name = 'budget_items'


class Budget_itemCreateView(CreateView):
    model = Budget_item
    Budget.objects.order_by().filter()
    template_name = 'budgets/Budget_item_create.html'
    fields = '__all__'
    success_url = reverse_lazy('budget_item_list')

class Budget_itemDetailView(DetailView):
    model = Budget_item
    template_name = 'budgets/Budget_item_detail.html'
    context_object_name = 'budget_item'

class Budget_itemUpdateView(UpdateView):
    model = Budget_item
    template_name = 'budgets/Budget_item_update.html'
    context_object_name = 'budget_item'
    fields = '__all__'
    success_url = reverse_lazy('budget_item_list')

class Budget_itemDeleteView(DeleteView):
    model = Budget_item
    template_name = 'budgets/Budget_item_delete.html'
    context_object_name = 'budget_item'
    success_url = reverse_lazy('budget_item_list')