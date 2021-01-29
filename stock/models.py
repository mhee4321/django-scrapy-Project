from django.db import models

class Stock(models.Model):
    objects = models.Manager()
    name = models.CharField('NAME', max_length=30, unique=True)
    code = models.IntegerField('CODE', blank=True)
    price = models.TextField('PRICE', blank=True)
    max_price = models.IntegerField('MAX_PRICE', blank=True, null=True)
    min_price = models.IntegerField('MIN_PRICE', blank=True, null=True)
    saved_time = models.DateTimeField('SAVED_TIME', auto_now_add=True)
    url = models.URLField('URL')

    def __str__(self):
        return self.name + self.url
 
    class Meta:
        verbose_name = 'stock'
        verbose_name_plural = 'stocks'
        db_table = 'stock'
        ordering = ('-saved_time',) # desc,