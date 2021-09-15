from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#Very important. Using this approach lets you customize django user in the future by adding your fields.
class User(AbstractUser):
    pass

class Lead(models.Model):

    # SOURCE_CHOICES = (
    #     ('Youtube', 'Youtube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter'),
    # )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    #
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField()


class Agent(models.Model):
    # Every agent has its own user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username