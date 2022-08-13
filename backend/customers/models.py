from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'