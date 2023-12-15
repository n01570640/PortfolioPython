from django.db import models
from django.conf import settings

# Create Book model
class Book(models.Model):
    #Store book attributes
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.FloatField()
    description = models.TextField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        #Return book title when printing book model
        return self.title