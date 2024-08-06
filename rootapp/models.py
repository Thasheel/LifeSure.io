from django.db import models
#
# # Create your models here.






class LifeInsurance(models.Model):


    duration_plans=(

        ('3 years', '3 year'),
        ('5 years', '5 year'),
        ('10 years', '10 year',)
    )
    life_plans=(
        ('health','health'),
        ('car','car'),
        ('home','home'),
        ('life','life'),

    )


    name=models.CharField(max_length=20)
    age=models.IntegerField()
    plans=models.CharField(max_length=20,choices=life_plans)
    price=models.IntegerField()
    duration=models.CharField(choices=duration_plans,max_length=25)

