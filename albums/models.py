from django.db import models

# this class defines what all albums will have
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')
    # this allows you to read the title and not just the object
    def __str__(self):
        return self.title