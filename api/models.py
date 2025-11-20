from django.db import models

# 1. Modelo de Parque (Unidade de Conservação)

class Parque(models.Model):
     
    TIPO_CHOICES = (
        ('NACIONAL', 'Parque Nacional da Serra dos Órgãos'),
        ('ESTADUAL', 'Parque Estadual dos Três Picos'),
        ('MUNICIPAL', 'Parque Natural Municipal Montanhas de Teresópolis'),
    )

    nome = models.CharField(
        max_length=200, 
        choices=TIPO_CHOICES,
        unique=True,
        verbose_name="Nome Oficial do Parque"
    )
    descricao_geral = models.TextField(
        verbose_name="Descrição Geral",
        help_text="Foco em geografia, limites e importância."
    )
    altitude_media = models.IntegerField(
        null=True, 
        blank=True, 
        verbose_name="Altitude Média (m)"
    )
    horario_funcionamento = models.CharField(
        max_length=255, 
        verbose_name="Horário de Funcionamento/Temporada"
    )
    
    class Meta:
        verbose_name = "Parque"
        verbose_name_plural = "Parques"

    def __str__(self):
        return self.get_nome_display()

# 2. Modelo de Trilha

class Trilha(models.Model):
    """
    Informações detalhadas sobre trilhas disponíveis nos Parques.
    """
    
    DIFICULDADE_CHOICES = (
        ('F', 'Fácil'),
        ('M', 'Média'),
        ('D', 'Difícil'),
        ('E', 'Extrema'),
    )
    
    parque = models.ForeignKey(
        Parque, 
        on_delete=models.CASCADE, 
        related_name='trilhas'
    )
    nome = models.CharField(
        max_length=100, 
        verbose_name="Nome da Trilha"
    )
    descricao = models.TextField(
        verbose_name="Detalhes da Trilha"
    )
    dificuldade = models.CharField(
        max_length=1, 
        choices=DIFICULDADE_CHOICES, 
        verbose_name="Nível de Dificuldade"
    )
    distancia_km = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        verbose_name="Distância (km)"
    )
    tempo_estimado_horas = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        verbose_name="Tempo Estimado (h)"
    )
    status_aberta = models.BooleanField(
        default=True, 
        verbose_name="Trilha Aberta para Visitação"
    )
    
    class Meta:
        verbose_name = "Trilha"
        verbose_name_plural = "Trilhas"
        unique_together = ('parque', 'nome') # Garante que não haja duas trilhas com o mesmo nome no mesmo parque

    def __str__(self):
        status = "ABERTA" if self.status_aberta else "FECHADA"
        return f"{self.nome} ({status}) - {self.parque.get_nome_display()}"

# 3. Modelo de Evento

class Evento(models.Model):
    """
    Eventos, novidades ou avisos que ocorrem nas Unidades de Conservação.
    """
    
    parque = models.ForeignKey(
        Parque, 
        on_delete=models.CASCADE, 
        related_name='eventos'
    )
    titulo = models.CharField(
        max_length=255, 
        verbose_name="Título do Evento/Novidade"
    )
    descricao = models.TextField(
        verbose_name="Descrição Detalhada"
    )
    data_inicio = models.DateTimeField(
        verbose_name="Data e Hora de Início"
    )
    data_fim = models.DateTimeField(
        null=True, 
        blank=True, 
        verbose_name="Data e Hora de Fim (opcional)"
    )
    disponibilidade = models.CharField(
        max_length=255, 
        verbose_name="Detalhes de Disponibilidade/Vagas",
        help_text="Ex: 'Livre', 'Vagas limitadas', 'Inscrições abertas'."
    )
    
    class Meta:
        verbose_name = "Evento/Novidade"
        verbose_name_plural = "Eventos e Novidades"
        ordering = ['data_inicio']

    def __str__(self):
        return f"[{self.data_inicio.strftime('%d/%m/%Y')}] {self.titulo}"

