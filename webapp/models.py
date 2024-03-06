from django.db import models

# Model for Clubs and Bars
class Club(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    music_type = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Model for Opening Hours, we aren't actually using this model, but thought id keep if i work a bit more on this project in the future
class OpeningHours(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    Club = models.ForeignKey(Club, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.Club.name} - {self.get_day_display()}: {self.open_time} - {self.close_time}"
