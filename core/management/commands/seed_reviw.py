from django.core.management.base import BaseCommand
from review.models import Review
from django.conf import settings
from users.models import User
from rooms.models import Room
from faker import Faker
import random
import os


class Command(BaseCommand):
    help = "This command is to create Dummy Rooms"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int,
                            help="How many fake Rooms you want to create")

    def handle(self, *args, **options):
        number = options.get("number")
        fake = Faker()

        
        user = User.objects.all()

        for i in range(number):
            room = Review.objects.create(
                accuracy = random.randint(1,10),
                clearniness = random.randint(1,10),
                location = random.randint(1,10),
                check_in = random.randint(1,10),
                value = random.randint(1,10),
                communication = random.randint(1,10),
                review = fake.paragraph(),
                room = random.choices(Room),
                user = random.choices(user)
            )

        self.stdout.write(self.style.SUCCESS(
            f"{number} Room(s) created successfully"))
