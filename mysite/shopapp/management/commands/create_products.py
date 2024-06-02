from django.core.management import BaseCommand
from shopapp.models import Product
class Command(BaseCommand):
    """
    Command to create products
    """
    def handle(self, *args, **options):
        self.stdout.write("Creating products...")
        proucts_name = [
            "Laptop",
            "Smartphone",
            "Computer",
        ]
        for product_name in proucts_name:
            product,created = Product.objects.get_or_create(name = product_name)
            self.stdout.write(f"Created product {product.name}")
        self.stdout.write(self.style.SUCCESS("Products created successfully"))