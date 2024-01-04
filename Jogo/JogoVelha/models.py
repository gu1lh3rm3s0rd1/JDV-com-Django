from django.db import models

# Create your models here.


class JogoVelha(models.Model):
    # Defina os campos necessários para representar o estado do jogo (por exemplo, as posições do tabuleiro)
    posicao_1 = models.CharField(max_length=1, default='-')
    posicao_2 = models.CharField(max_length=1, default='-')
    posicao_3 = models.CharField(max_length=1, default='-')
    posicao_4 = models.CharField(max_length=1, default='-')
    posicao_5 = models.CharField(max_length=1, default='-')
    posicao_6 = models.CharField(max_length=1, default='-')
    posicao_7 = models.CharField(max_length=1, default='-')
    posicao_8 = models.CharField(max_length=1, default='-')
    posicao_9 = models.CharField(max_length=1, default='-')
