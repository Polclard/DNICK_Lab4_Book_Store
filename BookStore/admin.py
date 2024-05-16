from django.contrib import admin
from BookStore.models import Book, PublishingHouse

# Register your models here.


admin.site.register(Book)
admin.site.register(PublishingHouse)
