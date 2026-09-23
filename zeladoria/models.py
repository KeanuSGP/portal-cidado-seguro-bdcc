from django.db import models

# Create your models here.
class Solicitacao(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pendente', 'Pendente'), ('em andamento', 'Em Andamento'), ('concluída', 'Concluída')])
    imagem = models.ImageField(upload_to='solicitacoes/', blank=True, null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    usuario = models.ForeignKey('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome