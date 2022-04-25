from django.db import models

ATTR_LEN = 255


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=ATTR_LEN)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name}, дата выпуска {self.release_date}, поддержка LTE {self.lte_exists}, обозначение {self.slug}'
