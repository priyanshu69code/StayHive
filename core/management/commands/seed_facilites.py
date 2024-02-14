from django.core.management.base import BaseCommand, CommandError
from rooms.models import HouseRule, Facility


ALL_FACILITIES = [
    ["Free parking", "Complimentary parking available on-site"],
    ["Gym", "Access to fitness facilities or gym equipment"],
    ["Pool", "Private or shared pool for swimming"],
    ["Hot tub", "Jacuzzi or hot tub for relaxation"],
    ["Garden or backyard", "Outdoor space for relaxation or activities"],
    ["BBQ grill", "Barbecue grill available for outdoor cooking"],
    ["Terrace or balcony", "Outdoor terrace or balcony with seating"],
    ["Game room", "Room equipped with games or entertainment options"],
    ["Cinema room", "Dedicated room for watching movies or shows"],
    ["Library", "Collection of books available for reading"],
]


class Command(BaseCommand):
    help = "This command is to create dummy House Rules and Facilities Data"

    def handle(self, *args, **options):
        for facility in ALL_FACILITIES:
            Facility.objects.create(name=facility[0], description=facility[1])
            self.stdout.write(self.style.SUCCESS(
                f"Created facility {facility[0]}"))
        self.stdout.write(self.style.SUCCESS(
            "Facilities created successfully"))
