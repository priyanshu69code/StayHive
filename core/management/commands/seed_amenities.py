from django.core.management.base import BaseCommand, CommandError
from rooms.models import Amenities
ALLAMENITIES = [
    ["Wifi", "Wireless internet connection available"],
    ["Kitchen", "Fully equipped kitchen for cooking meals"],
    ["TV", "Television with access to entertainment"],
    ["Heating", "Central heating or space heaters provided"],
    ["Air conditioning", "Cooling system available for comfort"],
    ["Washing machine", "Laundry machine for washing clothes"],
    ["Dryer", "Laundry dryer for drying clothes"],
    ["Free parking on premises", "Complimentary parking available on-site"],
    ["Gym", "Access to fitness facilities or gym equipment"],
    ["Pool", "Private or shared pool for swimming"],
    ["Hot tub", "Jacuzzi or hot tub for relaxation"],
    ["Pets allowed", "Pets permitted in the accommodation"],
    ["Smoke detector", "Smoke detector installed for safety"],
    ["Carbon monoxide detector", "Carbon monoxide detector for safety"],
    ["Essentials", "Basic amenities like towels, bed sheets, soap, and toilet paper"],
    ["Shampoo", "Shampoo provided for guests"],
    ["Hair dryer", "Hair dryer available for guest use"],
    ["Iron", "Iron and ironing board provided for clothing care"],
    ["Laptop-friendly workspace", "Desk or workspace suitable for laptop use"],
    ["Self check-in", "Option for guests to check in to the accommodation independently"],
    ["Lockbox", "Secure lockbox for key retrieval"],
    ["First aid kit", "First aid kit available for emergencies"],
    ["Fire extinguisher", "Fire extinguisher for fire safety"],
    ["Elevator", "Elevator or lift for accessing upper floors"],
    ["Wheelchair accessible", "Accommodation accessible to guests with mobility challenges"]
]


class Command(BaseCommand):
    help = "This is commond is to create the Dummy Amenities Data"

    def handle(self, *args, **options):
        for a in ALLAMENITIES:
            Amenities.objects.create(name=a[0], description=a[1])
            self.stdout.write(self.style.SUCCESS(f"Created  amenity {a[0]}"))
        self.stdout.write(self.style.SUCCESS("Amenities created Succesfully"))
