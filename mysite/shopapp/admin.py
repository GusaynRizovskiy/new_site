from django.contrib import admin
from django.http import HttpRequest
from .admin_mixins import ExportAsCSVMixin
from shopapp.models import Product,Order
# Register your models here.
@admin.action(description="Archive products")
def mark_archived(modeladmin: admin.ModelAdmin,request:HttpRequest,queryset):
    queryset.update(archived=True)
@admin.action(description="Unarchive products")
def mark_unarchived(modeladmin: admin.ModelAdmin,request:HttpRequest,queryset):
    queryset.update(archived=False)
class OrderInline(admin.TabularInline):
    model = Product.orders.through
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    inlines = [
        OrderInline,
    ]
    list_display = (
                    "pk",
                    "name",
                    "description_short",
                    "price",
                    "discount",
                    "created_at",
                    "archived")
    list_display_links = (
                        "pk",
                        "name")
    ordering = "pk", "name"
    search_fields = "name",
    fieldsets = [
        (None, {
            "fields": (
                "name",
                "description"
            ),
        }),
        ("Price options", {
            "fields": (
                "price",
                "discount",
            ),
            "classes": (
                "collapse",
            ),
        }),
        ("Extra options", {
            "fields": (
                "archived",
            ),
            "classes": (
                "collapse",
            ),
            "description":(
                "Extra options. Field 'archived' is for soft delete",
            ),
        }),
    ]
    def description_short(self,obj:Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."
class ProductInline(admin.TabularInline):
    model = Order.products.through
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = (
        "delivery_address",
        "promocode",
        "created_at",
        "user_verbose")
    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")
    def user_verbose(self,obj:Order)->str:
        return obj.user.username or obj.user.first_name