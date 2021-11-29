from django.contrib import admin

from django.contrib import admin

from .models import Customer, Employee, User

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)