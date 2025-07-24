from django.db import models

class Prompt(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


