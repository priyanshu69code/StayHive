from django.core.management.base import BaseCommand
from lists.models import List
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
                            help="How many fake Rooms you want to create",default=1)

    def handle(self, *args, **options):
        number = options.get("number")
        fake = Faker()
        

        users = User.objects.all()
        rooms = Room.objects.all()

        for i in range(number):
            new_list = List.objects.create(
                name = fake.paragraph(),
                user = random.choice(users)
            )
            new_list.rooms.set(random.sample(list(rooms), random.randint(1, 15)))
        self.stdout.write(self.style.SUCCESS(
            f"{number} Room(s) created successfully"))
