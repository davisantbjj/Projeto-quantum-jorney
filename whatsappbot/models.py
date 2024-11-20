from django.db import models

class Userresponse(models.Model):
    phone_number = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    responses = models.TextField(null=True, blank=True)  # Campo para armazenar as respostas

    class Meta:
        db_table = 'whatsappbot_userresponse'  # Nome correto da tabela

    def __str__(self):
        return self.name
