from django.contrib import admin

# Register your models here.
from .models import User,Category,Product,Review,SubCategory

admin.site.register(User)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Review)