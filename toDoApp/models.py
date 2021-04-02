from django.db import models


class ToDoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    creation_date = models.DateTimeField()

    def __str__(self):
        return self.title
