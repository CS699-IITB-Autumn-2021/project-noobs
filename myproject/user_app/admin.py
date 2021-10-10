from django.contrib import admin

# Register your models here.
from .models import User,Category,Product,Review

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)