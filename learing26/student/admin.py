from django.contrib import admin
from .models import student ,product,StudentProfile,Category,Service

from .models import accountholder
from .models import bank

# Register your models here.

admin.site.register(student)
admin.site.register(product)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(StudentProfile)

admin.site.register(accountholder)
admin.site.register(bank)


