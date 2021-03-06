from django.db import models

class Weather(models.Model):
    objects = models.Manager()
    city = models.CharField('CITY', max_length=50)
    date = models.TextField('DATE')
    desc = models.TextField('DESC')
    temp_min = models.TextField('TEMP_MIN')
    temp_max = models.TextField('TEMP_MAX')
    humidity = models.TextField('HUMIDITY')
    pressure = models.TextField('PRESSURE')
    deg = models.TextField('DEG')
    speed = models.TextField('SPEED')

    def __str__(self):
        return self.city + self.date + self.desc

    class Meta:
        db_table = 'weather'
        ordering = ('date',)



