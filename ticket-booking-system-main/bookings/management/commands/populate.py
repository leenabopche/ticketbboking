from django.core.management.base import BaseCommand
from bookings.models import Event  # Import from your app
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Adds sample movies/events'

    def handle(self, *args, **options):
        movies = [
            
            {
                "title": "Dune: Part Two",
                "date": timezone.now() + timezone.timedelta(days=1),
                "venue": "IMAX Sci-Fi Theater",
                "total_seats": random.randint(80, 150),
                "image_url": "https://image.tmdb.org/t/p/w500/8b8R8l88Qje9dn9OE8PY05Nxl1X.jpg",
                "description": "Paul Atreides unites with Chani and the Fremen to wage war against House Harkonnen."
            },
            {
                "title": "The Batman",
                "date": timezone.now() + timezone.timedelta(days=2),
                "venue": "Gotham Cinemas",
                "total_seats": random.randint(70, 120),
                "image_url": "https://image.tmdb.org/t/p/w500/74xTEgt7R36Fpooo50r9T25onhq.jpg",
                "description": "Batman uncovers corruption in Gotham City while pursuing the Riddler."
            },
            {
                "title": "Top Gun: Maverick",
                "date": timezone.now() + timezone.timedelta(days=3),
                "venue": "ActionPlex",
                "total_seats": random.randint(90, 180),
                "image_url": "https://image.tmdb.org/t/p/w500/62HCnUTziyWcpDaBO2i1DX17ljH.jpg",
                "description": "After thirty years, Maverick still pushes the envelope as a top naval aviator."
            },
            {
                "title": "Black Panther: Wakanda Forever",
                "date": timezone.now() + timezone.timedelta(days=4),
                "venue": "Marvel Megaplex",
                "total_seats": random.randint(100, 200),
                "image_url": "https://image.tmdb.org/t/p/w500/sv1xJUazXeYqALzczSZ3O6nkH75.jpg",
                "description": "The Wakandans fight to protect their nation after the death of King T'Challa."
            },
            {
                "title": "Avatar: The Way of Water",
                "date": timezone.now() + timezone.timedelta(days=5),
                "venue": "3D Premium Theater",
                "total_seats": random.randint(120, 250),
                "image_url": "https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
                "description": "Jake Sully and Ney'tiri fight to protect Pandora from new threats."
            }

        ]

        for movie in movies:
            Event.objects.create(
                title=movie['title'],
                date=movie['date'],
                venue=movie['venue'],
                total_seats=movie['total_seats'],
                available_seats=movie['total_seats'],
                image_url=movie['image_url']
            )
        
        self.stdout.write(self.style.SUCCESS('Added 2 blockbuster movies!'))