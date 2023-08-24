from django.db import models

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    cnpj_cpf = models.CharField(max_length=18, unique=True)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    atividade_economica_profissao = models.CharField(max_length=255)

class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)

class Operador(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

class MaquinaExtrusao(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

class MaquinaImpressao(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

class MaquinaCorte(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    acabamento = models.CharField(max_length=100)

class OrdemServico(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    data = models.DateField()
    tratamento = models.CharField(max_length=100)
    tipo_material = models.CharField(max_length=100)

class Tinta(models.Model):
    id = models.AutoField(primary_key=True)
    cor = models.CharField(max_length=50)

class TintaOrdemServico(models.Model):
    id = models.AutoField(primary_key=True)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    tinta = models.ForeignKey(Tinta, on_delete=models.CASCADE)

class Ingredientes(models.Model):
    id = models.AutoField(primary_key=True)
    ingrediente = models.CharField(max_length=100)

class IngredienteOrdemServico(models.Model):
    id = models.AutoField(primary_key=True)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE)

class Extrusao(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    maquina_extrusao = models.ForeignKey(MaquinaExtrusao, on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField()
    hora_fim = models.DateTimeField()
    data = models.DateField()

class Impressao(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    maquina_impressao = models.ForeignKey(MaquinaImpressao, on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField()
    hora_fim = models.DateTimeField()
    data = models.DateField()

class Corte(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    maquina_corte = models.ForeignKey(MaquinaCorte, on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField()
    hora_fim = models.DateTimeField()
    data = models.DateField()
