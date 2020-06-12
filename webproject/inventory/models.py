from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_count = models.IntegerField(default = 0)
    total_unit = models.IntegerField(default = 0)

    def __str__(self):
        return self.item_name


class ItemModel(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    model_name = models.CharField(max_length = 200)
    item_count = models.IntegerField(default = 0)
    item_price = models.IntegerField(default = 0)

    def __str__(self):
        return self.model_name
