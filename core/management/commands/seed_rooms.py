from django.core.management.base import BaseCommand
from rooms.models import Room, Amenities, Facility, HouseRule, RoomType, RoomPhotos
from django.conf import settings
from users.models import User
from faker import Faker
import random
import os


class Command(BaseCommand):
    help = "This command is to create Dummy Rooms"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int,
                            help="How many fake Rooms you want to create", default=1)

    def handle(self, *args, **options):
        number = options.get("number")
        fake = Faker()

        amenities = Amenities.objects.all()
        facilities = Facility.objects.all()
        house_rules = HouseRule.objects.all()
        room_types = RoomType.objects.all()
        hosts = User.objects.all()

        for i in range(number):
            room = Room.objects.create(
                name=fake.company(),
                description=fake.paragraph(),
                country=fake.country(),
                city=fake.city(),
                address=fake.address(),
                price_per_night=random.randint(100, 500),
                max_guests=random.randint(1, 10),
                is_available=random.choice([True, False]),
                beds=random.randint(1, 5),
                bedrooms=random.randint(1, 3),
                baths=random.randint(1, 3),
                checkin=fake.time(pattern="%H:%M:%S"),
                checkout=fake.time(pattern="%H:%M:%S"),
                host=random.choice(hosts),
                room_type=random.choice(room_types)
            )
            room.amenities.set(random.sample(
                list(amenities), random.randint(1, len(amenities))))
            room.facilities.set(random.sample(
                list(facilities), random.randint(1, len(facilities))))
            room.house_rules.set(random.sample(
                list(house_rules), random.randint(1, len(house_rules))))

            # Add room photos
            photos_folder = "roomsphotos"
            photos_path = os.path.join(settings.MEDIA_ROOT, photos_folder)
            room_photos = os.listdir(photos_path)
            upload_dir = os.path.join(settings.MEDIA_ROOT, "uploaded")
            selected_photos = random.sample(
                room_photos, random.randint(3, len(room_photos)))
            for photo in selected_photos:
                photo_path = os.path.join(photos_folder, photo)
                RoomPhotos.objects.create(
                    img=photo_path, room=room)

        self.stdout.write(self.style.SUCCESS(
            f"{number} Room(s) created successfully"))
