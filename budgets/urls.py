
from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [


 path('create/', views.BudgetCreateView.as_view(), name='budget_create'),
 path('list/', views.BudgetListView.as_view(), name='budget_list'),
 path('detail/<int:pk>', views.BudgetDetailView.as_view(), name='budget_detail'),
 path('update/<int:pk>', views.BudgetUpdateView.as_view(), name='budget_update'),
 path('delete/<int:pk>', views.BudgetDeleteView.as_view(), name='budget_delete'),

 path('create/', views.Budget_itemCreateView.as_view(), name='budget_item_create'),
 path('list/', views.Budget_itemListView.as_view(), name='budget_item_list'),
 path('detail/<int:pk>', views.Budget_itemDetailView.as_view(), name='budget_item_detail'),
 path('update/<int:pk>', views.Budget_itemUpdateView.as_view(), name='budget_item_update'),
 path('delete/<int:pk>', views.Budget_itemDeleteView.as_view(), name='budget_item_delete'),

]