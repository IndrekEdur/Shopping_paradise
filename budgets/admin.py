from django.contrib import admin
from .models import Budget, Budget_item

# Register your models here.

admin.site.register(Budget)
admin.site.register(Budget_item)