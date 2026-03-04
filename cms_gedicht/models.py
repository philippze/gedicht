from django.db import models


class Bestellung(models.Model):
    name = models.CharField(max_length=100)
    zeitpunkt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bestellung"
        verbose_name_plural = "Bestellungen"