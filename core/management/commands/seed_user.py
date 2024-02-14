from django.core.management.base import BaseCommand, CommandError, CommandParser
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = "This is commond is to create the Dummy Users"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number", help="How many fake Users You wants to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, int(number), {
            "is_staff": False,
            "is_superuser": False
        })
        inserted_pks = seeder.execute()
        self.stdout.write(self.style.SUCCESS("User created Succesfully"))
