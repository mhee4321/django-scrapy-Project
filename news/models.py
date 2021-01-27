from django.db import models

# Create your models here.
class News(models.Model):
    objects = models.Manager()
    title = models.TextField('TITLE', max_length=255, unique=True)
    content = models.TextField('CONTENT', blank=True)
    company = models.CharField('COMPANY', max_length=50,blank=True)
    saved_time = models.TextField('SAVED_TIME', blank=True)
    
    # link = models.ImageField('LINK', blank=True, null=True)

    def __str__(self):
        return self.title
 
    class Meta:
        # verbose_name = 'news'
        # verbose_name_plural = 'newsapp'
        db_table = 'news'
        # ordering = ('modify_date', 'author') # asc & author
        ordering = ('-saved_time',) # desc,