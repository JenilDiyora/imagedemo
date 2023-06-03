from django.db import models
STATE_CHOICE = ((
    ('Bihar','Bihar'),
    ('Jharkhand','Jaharkhnd'),
    ('West Bengal','West Bengal'),
))

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # pimage = models.ImageField(upload_to='pimages', blank=True)
    pimage = models.ImageField(upload_to = 'geo_entity_pic')

