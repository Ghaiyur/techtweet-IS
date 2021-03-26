from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    follows = models.ManyToManyField('self',
                                     related_name='followed_by',
                                     symmetrical=False)

    def __str__(self):
        return self.user.username


User.users = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])