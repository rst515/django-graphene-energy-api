from django.core.management.base import BaseCommand
from energy.models import Customer, Tariff, UsageRecord
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed database with demo customers, tariffs, and usage records'

    def handle(self, *args, **kwargs):
        # Clear existing data
        UsageRecord.objects.all().delete()
        Customer.objects.all().delete()
        Tariff.objects.all().delete()

        # Create customers
        alice = Customer.objects.create(name="Alice Smith", email="alice@example.com")
        bob = Customer.objects.create(name="Bob Jones", email="bob@example.com")

        # Create tariffs
        standard = Tariff.objects.create(name="Standard", price_per_kwh=0.30)
        green = Tariff.objects.create(name="Green Energy", price_per_kwh=0.35)

        # Create usage records
        UsageRecord.objects.create(customer=alice, tariff=standard, kwh_used=12.5, timestamp=timezone.now())
        UsageRecord.objects.create(customer=alice, tariff=green, kwh_used=8.3, timestamp=timezone.now())
        UsageRecord.objects.create(customer=bob, tariff=standard, kwh_used=15.0, timestamp=timezone.now())

        self.stdout.write(self.style.SUCCESS("Demo data seeded!"))
