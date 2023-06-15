from django.db import models


class Joke(models.Model):
    query = models.CharField(max_length=50)
    response = models.TextField()
    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.query} - {self.created_at}"