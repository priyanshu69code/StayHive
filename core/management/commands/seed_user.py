from django.core.management.base import BaseCommand, CommandError, CommandParser
from django_seed import Seed
from users.models import User, Gender, Language
import random
from django_countries.fields import CountryField


class Command(BaseCommand):
    help = "This is commond is to create the Dummy Users"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number", help="How many fake Users You wants to create", default=1
        )

    def handle(self, *args, **options):
        countries = [country.code for country in CountryField().countries]
        number = options.get("number")
        seeder = Seed.seeder()
        gender = Gender.objects.all()
        language = Language.objects.all()
        seeder.add_entity(User, int(number), {
            "is_staff": False,
            "is_superuser": False,
            "gender": lambda x: random.choice(gender),
            "language": lambda x: random.choice(language),
            "country": lambda x: random.choice(countries)
        })
        inserted_pks = seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            f"{number}User created Succesfully"))
