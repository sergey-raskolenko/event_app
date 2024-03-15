from datetime import datetime

from django.core.management import BaseCommand
from myapp.models import Organization, User, Event


class Command(BaseCommand):
    def handle(self, *args, **options):
        org1 = Organization.objects.create(
            title='First',
            description='first organization',
            address='First city',
            postcode='111111'
        )
        org2 = Organization.objects.create(
            title='Second',
            description='second organization',
            address='Second city',
            postcode='222222'
        )
        org3 = Organization.objects.create(
            title='Third',
            description='third organization',
            address='Third city',
            postcode='333333'
        )

        user1 = User.objects.create(
            email='1@admin.admin',
            phone=f'+79998887761'
        )
        user1.organizations.set([org1])
        user1.set_password(f'admin1')
        user1.save()

        user2 = User.objects.create(
            email='2@admin.admin',
            phone=f'+79998887762'
        )
        user2.organizations.set([org1, org2])
        user2.set_password(f'admin2')
        user2.save()

        user3 = User.objects.create(
            email='3@admin.admin',
            phone=f'+79998887763'
        )
        user3.organizations.set([org1, org2, org3])
        user3.set_password(f'admin3')
        user3.save()

        Event.objects.create(
            title='First',
            description='first event',
            date=datetime.now()
        ).organizations.set([org1, org2, org3])
        Event.objects.create(
            title='Second',
            description='second event',
            date=datetime.now()
        ).organizations.set([org2, org3])
        Event.objects.create(
            title='Third',
            description='third event',
            date=datetime.now()
        ).organizations.set([org3])
