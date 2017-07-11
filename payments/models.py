from django.db import models
from datetime import datetime

# Create your models here.
# User model
class Child(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='ФИО ребенка')
    user = models.ForeignKey('auth.User', null = True, verbose_name = 'Логин')
    parent = models.CharField(max_length=200, null = True, verbose_name='ФИО родителя')
    parent_phone = models.CharField(max_length=30, null = True, blank = True, verbose_name='Телефон родителя')
    parent_email = models.EmailField(max_length=75, null = True, blank = True, verbose_name='Email родителя')
    discount = models.BooleanField(default=False, verbose_name = 'Льгота')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = u"Ребенок"
        verbose_name_plural = u"Дети"



# Payment model
class Payment_made(models.Model):
    name = models.ForeignKey('Child', db_index=True, null = True, verbose_name = 'ФИО ребенка')
    contribution = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    payment_date = models.DateField()



    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = u"Выполненный платеж"
        verbose_name_plural = u"Выполненные платежи"

class Payment_needed(models.Model):
    ADDRESS = (
        ('С', 'Сад'),
        ('Г', 'Группа'),
    )
    category = models.CharField(max_length=200, db_index=True, verbose_name="Категория")
    address = models.CharField(max_length=10, choices=ADDRESS, null = True, verbose_name="Куда")
    reckoning = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    deadline = models.DateField(default=datetime.now, verbose_name="Срок сдачи")
    discount = models.BooleanField(default=False, verbose_name='Льгота')

    def __str__(self):
        return str(self.category)

    class Meta:
        verbose_name = u"Необходимый платеж"
        verbose_name_plural = u"Необходимые платежи"
