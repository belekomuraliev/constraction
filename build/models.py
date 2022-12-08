from django.db import models
from django.contrib import admin

class Block(models.Model):
    block_number = models.IntegerField(verbose_name='Номер блока')
    price_m = models.IntegerField(verbose_name='Стоимость за 1 кв. метр')
    amount_entry = models.IntegerField(verbose_name='Колличество подъезда')
    amount_apartments_floor = models.IntegerField(verbose_name='Колличество квартир на этаж')
    ammount_floors = models.IntegerField(verbose_name='Колличество этажей', default=9)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='rel_client', default=1)

    def __str__(self):
        return str(self.block_number)

    @admin.display(description='общая сумма в Блоке')
    def total_sum(self):

        return self.client.total_area*self.price_m*self.amount_entry*self.amount_apartments_floor*self.ammount_floors

class Client(models.Model):
    owner = models.CharField(max_length=20, verbose_name='ФИО владельца')
    sale_date = models.DateField(verbose_name='Дата продажи', null=True, blank=True)
    status = models.CharField(max_length=50, choices=(
        ('выкуп','Выкуп'), ('доконца','Выкуп не доконца'), ('расторнут','Расторгнуто'),('продан','Не прдано'),
    ), verbose_name='Статус квартиры')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='rel_block', related_query_name='rel_client')
    total_area = models.IntegerField(verbose_name='Общая площадь кв.м.')

    def __str__(self):
        return self.owner

    @admin.display(description='Стоимость квартиры')
    def total_sum_aparment(self):
        return self.total_area * self.block.price_m


