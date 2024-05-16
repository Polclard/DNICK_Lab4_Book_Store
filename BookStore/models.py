from django.db import models

# Create your models here.


PAGES_TYPES = {
    "Hard": "HARD",
    "Soft": "SOFT"
}
BOOK_CATEGORIES = {
    "Romance": "ROMANCE",
    "Thriller": "THRILLER",
    "Biography": "BIOGRAPHY",
    "Classic": "CLASSIC",
    "Drama": "DRAMA",
    "History": "HISTORY"
}


class PublishingHouse(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    found_date = models.DateTimeField()
    website_url = models.CharField(max_length=100)


class Book(models.Model):
    ISBN = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    release_date = models.DateTimeField()
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    dimensions = models.CharField(max_length=100)
    page_type = models.CharField(choices=PAGES_TYPES, max_length=20)
    category = models.CharField(choices=BOOK_CATEGORIES, max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=10)
