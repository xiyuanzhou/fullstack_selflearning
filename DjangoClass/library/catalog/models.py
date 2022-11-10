from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Languages(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Book(models.Model):

    title = models.CharField(max_length=50)
    author = models.ForeignKey("Author",on_delete=models.SET_NULL,null=True)
    summary = models.TextField(max_length =600)
    isbn = models.CharField(max_length=13,unique=True)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey("Languages", on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering =['last_name','first_name']
    
    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.last_name} and {self.first_name}"
    
import uuid

class BookInstance(models.Model):
    id = models.UUIDField(primary_key =True,default=uuid.uuid4)

    book = models.ForeignKey("Book", on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=50)
    due_back = models.DateField(auto_now=False, auto_now_add=False)

    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On Loan'),
        ('a','Avaiable'),
        ('r','Reserved')
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'
    