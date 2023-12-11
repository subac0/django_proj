from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta

class Voo(models.Model):
    numero_voo = models.IntegerField(validators=[
        MaxValueValidator(9999, message='O número do voo deve ter no máximo 4 dígitos.'),
        MinValueValidator(1, message='O número do voo deve ter exatamente 4 dígitos.'),
        ],
    )

    CLASSE_CHOICES = [
        ('Econômica', 'Econômica'),
        ('Executiva', 'Executiva'),
    ]

    origem = models.CharField(max_length=100, default='Petrolina')
    destino = models.CharField(max_length=100)
    data_partida = models.CharField(max_length=10, default=(datetime.now() + timedelta(days=1)).strftime('%d-%m-%Y'))
    data_chegada = models.CharField(max_length=10, null=True, blank=True)
    nome = models.CharField(max_length=50)
    classe = models.CharField(max_length=20, choices=CLASSE_CHOICES)

    def save(self, *args, **kwargs):
        # Verifica se o número de voo já existe no banco de dados
        if Voo.objects.filter(numero_voo=self.numero_voo).exists():
            # Obtém o primeiro registro com o número de voo em questão
            primeiro_registro = Voo.objects.filter(numero_voo=self.numero_voo).first()

            # Preenche os campos com os valores do primeiro registro
            self.origem = primeiro_registro.origem
            self.destino = primeiro_registro.destino
            self.data_partida = primeiro_registro.data_partida

        super().save(*args, **kwargs)