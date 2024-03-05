from django.core.management.base import BaseCommand
from django.utils import timezone
from reservations.models import Reservation, Status
from users.models import User
from rooms.models import Room
from faker import Faker
import random

class Command(BaseCommand):
    help = "This command is to create Dummy Reservations"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, help="How many fake reservations you want to create", default=1)

    def handle(self, *args, **options):
        number = options.get("number")
        fake = Faker()
        
        users = User.objects.all()
        rooms = Room.objects.all()
        statuses = Status.objects.all()

        for _ in range(number):
            check_in = fake.date_time_between(start_date="-30d", end_date="+30d")
            check_out = check_in + timezone.timedelta(days=random.randint(1, 14))
            status = random.choice(statuses)
            guest = random.choice(users)
            room = random.choice(rooms)
            reservation = Reservation.objects.create(
                room=room,
                check_in=check_in,
                check_out=check_out,
                status=status,
                guest=guest
            )

        self.stdout.write(self.style.SUCCESS(f"{number} Reservation(s) created successfully"))
