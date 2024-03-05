from django.db import models
from conversations.models import Converstions,Message
from django.core.management.base import BaseCommand
from users.models import User
from faker import Faker
import random


class Command(BaseCommand):
    help = "This command is to create dummy Conversations and Messages"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, help="How many fake Conversations you want to create", default=1)

    def handle(self, *args, **options):
        number = options.get("number")
        fake = Faker()

        users = User.objects.all()

        for _ in range(number):
            # Create a conversation
            conversation = Converstions.objects.create()
            # Choose random participants for the conversation
            participants = random.sample(list(users), random.randint(2, 5))
            conversation.participants.add(*participants)

            # Generate random number of messages for the conversation
            num_messages = random.randint(1, 20)
            for _ in range(num_messages):
                # Create a message
                message = Message.objects.create(
                    text=fake.text(),
                    user=random.choice(participants),
                    converstions=conversation
                )

        self.stdout.write(self.style.SUCCESS(
            f"{number} Conversation(s) created successfully with messages"))
