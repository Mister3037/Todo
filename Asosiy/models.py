from django.db import models

class Reja(models.Model):

    sarlavha = models.CharField(max_length=100)
    matn = models.TextField()
    vaqt = models.TimeField(null=True, blank=True)
    holat = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return self.sarlavha

