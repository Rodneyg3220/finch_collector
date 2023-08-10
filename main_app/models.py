from django.db import models
from django.urls import reverse
from datetime import date

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


# Create your models here.
class Shoe(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('shoes_detail', kwargs={'pk': self.id})

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    shoes = models.ManyToManyField(Shoe)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
  # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

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