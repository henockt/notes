from django.db import models

# Create your models here.
class Notes(models.Model):
    note_id = models.CharField(max_length=10)
    note_title = models.CharField(max_length=50)
    note = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.note