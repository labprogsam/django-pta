from django.db import models

class People(models.Model):
    name = models.CharField(verbose_name = 'Nome Completo', max_length = 100, null = True, blank=True)
    cpf = models.IntegerField('CPF', primary_key = True)
    email = models.EmailField('E-mail', null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.name

# Create your models here.
