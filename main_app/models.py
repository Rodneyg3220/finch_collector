from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
  # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
    # set the default value for meal to be 'B'
        default=MEALS[0][0]
        )

    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    #Changing this instance method does not impact the database, therefore no makemigrations is necessary.
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    class Meta:
        ordering = ['-date']