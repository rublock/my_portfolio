from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=9999)
    image = models.ImageField(upload_to='portfolio/img')
    url = models.URLField(blank=True)  # open in new page
    tech = models.JSONField()

    def __str__(self):
        return self.title
