from django.contrib import admin
from .models import Genre, Book, Author, Languages, BookInstance

# Register your models here.
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Languages)
admin.site.register(BookInstance)

