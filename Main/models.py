from django.db import models

class Mechanics(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Appointments(models.Model):
    mechanic = models.ForeignKey(Mechanics, on_delete=models.CASCADE)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    car_color = models.CharField(max_length=200, default='Black')
    car_regi_num = models.CharField(max_length=200)
    car_licence = models.CharField(max_length=200, default='')

    def __str__(self):
        return f"{self.customer_name} - {self.date} {self.mechanic}"