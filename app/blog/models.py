from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/img')
    url = models.URLField(blank=True) #open in new page
    date = models.DateField(default='')

    def __str__(self):
        return self.title
