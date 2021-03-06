from django.db import models

class Jobs(models.Model):

    type = models.CharField(max_length=11)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    how_to_apply = models.TextField()
    activ = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.type} - {self.title}"

