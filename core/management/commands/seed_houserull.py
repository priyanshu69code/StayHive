from django.core.management.base import BaseCommand, CommandError
from rooms.models import HouseRule, Facility

ALL_HOUSE_RULES = [
    ["No smoking", "Smoking is not allowed in the accommodation"],
    ["No parties or events", "Parties or events are not permitted in the accommodation"],
    ["No pets", "Pets are not allowed in the accommodation"],
    ["No unregistered guests", "Only registered guests are allowed in the accommodation"],
    ["Quiet hours", "Quiet hours are enforced during specific times"],
    ["No loud noise after 10 PM", "Loud noise is not allowed after 10 PM"],
    ["No cooking late at night", "Cooking is not allowed late at night"],
    ["No outside visitors after 11 PM",
        "Visitors from outside are not allowed after 11 PM"],
]


class Command(BaseCommand):
    help = "This command is to create dummy House Rules and Facilities Data"

    def handle(self, *args, **options):
        for rule in ALL_HOUSE_RULES:
            HouseRule.objects.create(name=rule[0], description=rule[1])
            self.stdout.write(self.style.SUCCESS(
                f"Created house rule {rule[0]}"))
        self.stdout.write(self.style.SUCCESS(
            "House rules created successfully"))
