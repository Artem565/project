from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    pass


@admin.register(Watches)
class ToysAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    pass


@admin.register(PosOrder)
class PosOrderAdmin(admin.ModelAdmin):
    pass


@admin.register(PosSupply)
class PosSupplyAdmin(admin.ModelAdmin):
    pass