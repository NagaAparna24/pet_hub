from django.db import models
class PetReturnRequest(models.Model):
    pet_id = models.CharField(max_length=50)
    pet_name = models.CharField(max_length=100)
    pet_breed = models.CharField(max_length=100)
    pet_age = models.IntegerField()
    return_reason = models.TextField()
    return_date = models.DateField()
class Meta:
    db_table = "petreturnstatus"
class PetBooking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    reason = models.TextField()
    pet_type = models.CharField(max_length=50, choices=[
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('fish', 'Fish'),
        ('rabbit', 'Rabbit'),
        ('parrot', 'Parrot'),
        ('goat', 'Goat'),
        ('horse', 'Horse'),
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = "petbookinfo"
    def __str__(self):
        return self.name
