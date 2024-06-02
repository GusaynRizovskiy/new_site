from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order,Product
class Command(BaseCommand):
    """
    Command to create orders
    """
    user = User.objects.get(username='admin')
    def handle(self, *args, **options):
        self.stdout.write("Creating orders...")
        order,created = Order.objects.get_or_create(
            delivery_address = "Lenina street, 27 building, 74 home",
            promocode = "2HDS$DS",
            user = User.objects.get(username='admin'),
        )
        self.stdout.write(self.style.SUCCESS("Order created successfully"))