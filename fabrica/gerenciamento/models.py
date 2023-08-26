from django.db import models

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    cnpj_cpf = models.CharField(max_length=18, unique=True)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    atividade_economica_profissao = models.CharField(max_length=255)

    def __str__(self):
        nome = self.razao_social
        return nome

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

class Tratamento(models.Model):
    id = models.AutoField(primary_key=True)
    tratamento_produto = models.CharField(max_length=100)

    def __str__(self):
        return self.tratamento_produto

class Material(models.Model):
    id = models.AutoField(primary_key=True)
    material_produto = models.CharField(max_length=100)

    def __str__(self):
        return self.material_produto

class Acabamento(models.Model):
    id = models.AutoField(primary_key=True)
    acabamento_produto = models.CharField(max_length=100)

    def __str__(self):
        return self.acabamento_produto

class CorProduto(models.Model):
    id = models.AutoField(primary_key=True)
    cor_produto = models.CharField(max_length=100)

    def __str__(self):
        return self.cor_produto

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    cor_produto = models.ForeignKey(CorProduto, on_delete=models.CASCADE)
    acabamento_produto = models.ForeignKey(Acabamento, on_delete=models.CASCADE)
    tratamento_produto = models.ForeignKey(Tratamento, on_delete=models.CASCADE)
    material_produto = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo
    
class OrdemServico(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    observacao = models.CharField(max_length=100)
    data_inicio = models.DateField()

class StatusServico(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    hora_alteracao = models.DateTimeField()
    data_alteracao = models.DateField()

class Tinta(models.Model):
    id = models.AutoField(primary_key=True)
    cor = models.CharField(max_length=50)

class TintaOrdemServico(models.Model):
    id = models.AutoField(primary_key=True)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    tinta = models.ForeignKey(Tinta, on_delete=models.CASCADE)
    qtde = models.CharField(max_length=10)

class Ingredientes(models.Model):
    id = models.AutoField(primary_key=True)
    ingrediente = models.CharField(max_length=100)

class IngredienteOrdemServico(models.Model):
    id = models.AutoField(primary_key=True)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE)
    qtde = models.CharField(max_length=10)

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

class ProdutoExtrusao(models.Model):
    id = models.AutoField(primary_key=True)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    item_produzido = models.ForeignKey(Extrusao, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=10)
    qtde = models.CharField(max_length=10)
    peso = models.CharField(max_length=10)

class ProdutoImpressao(models.Model):
    id = models.AutoField(primary_key=True)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    item_produzido = models.ForeignKey(Impressao, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=10)
    qtde = models.CharField(max_length=10)
    peso = models.CharField(max_length=10)

class ProdutoCorte(models.Model):
    id = models.AutoField(primary_key=True)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    item_produzido = models.ForeignKey(Corte, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=10)
    qtde = models.CharField(max_length=10)
    peso = models.CharField(max_length=10)