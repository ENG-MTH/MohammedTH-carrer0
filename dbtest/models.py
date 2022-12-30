from django.db import models


class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.title
