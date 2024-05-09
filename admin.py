from django.contrib import admin
from .models import StudentProfile,Product,CartItems

admin.site.register(StudentProfile)

# Register your models here.
admin.site.register(CartItems)
admin.site.register(Product)