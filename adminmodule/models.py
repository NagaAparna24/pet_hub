from django.db import models
from django.contrib.auth.models import User
class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    class Meta:
        db_table = "info"

    def __str__(self):
        return self.user.username

# Create your models here.
