from django.contrib import admin
from cartapp import models

admin.site.register(models.ProductModel)
admin.site.register(models.OrderModel)
admin.site.register(models.DetailModel)