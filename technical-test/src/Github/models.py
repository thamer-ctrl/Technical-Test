from django.db import models

# Create your models here.


class Github(models.Model) :
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=200)




    def __str__(self):
        return self.title