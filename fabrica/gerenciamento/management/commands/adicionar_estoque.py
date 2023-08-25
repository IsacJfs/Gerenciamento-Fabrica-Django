from django.core.management.base import BaseCommand
from gerenciamento.models import (
        Cliente,
        Endereco,
        Operador,
        MaquinaExtrusao,
        MaquinaImpressao,
        MaquinaCorte,
        Tratamento,
        Material,
        Acabamento,
        CorProduto,
        Produto,
        OrdemServico,
        StatusServico,
        Tinta,
        TintaOrdemServico,
        Ingredientes,
        IngredienteOrdemServico,
        Extrusao,
        Impressao,
        Corte,
        ProdutoExtrusao,
        ProdutoImpressao,
        ProdutoCorte
        )



class Command(BaseCommand):
    help = 'Adiciona clientes ao banco de dados'

    def handle(self, *args, **kwargs):
        # Chamando o método para adicionar clientes
        self.add_operador()
        self.stdout.write(self.style.SUCCESS('Operador adicionados com sucesso!'))
        self.add_maq_extrusao()
        self.stdout.write(self.style.SUCCESS('Maquina Extrusao adicionados com sucesso!'))
        self.add_maq_impressao()
        self.stdout.write(self.style.SUCCESS('Impressora adicionados com sucesso!'))
        self.add_corte()
        self.stdout.write(self.style.SUCCESS('Corte adicionados com sucesso!'))
        self.add_Tratamento()
        self.stdout.write(self.style.SUCCESS('Tratamento adicionados com sucesso!'))
        self.add_material()
        self.stdout.write(self.style.SUCCESS('material adicionados com sucesso!'))
        self.add_acabamento()
        self.stdout.write(self.style.SUCCESS('acabamento adicionados com sucesso!'))
        self.add_cor()
        self.stdout.write(self.style.SUCCESS('cor adicionados com sucesso!'))
        self.add_tintas()
        self.stdout.write(self.style.SUCCESS('tintas adicionados com sucesso!'))
        self.add_ingredientes()
        self.stdout.write(self.style.SUCCESS('ingredientes adicionados com sucesso!'))

    def add_operador(self):
        lista_operador = [
            {'nome' : 'ASDROS',
            'cargo' : 'operador'},
            {'nome' : 'BRENO',
            'cargo' : 'operador'},
            {'nome' : 'EDSON',
            'cargo' : 'operador'},
            {'nome' : 'HENRIQUE',
            'cargo' : 'operador'},
            {'nome' : 'HERNANDES',
            'cargo' : 'operador'},
            {'nome' : 'JAIRO',
            'cargo' : 'operador'},
            {'nome' : 'JOSIMAR',
            'cargo' : 'operador'},
            {'nome' : 'KERVENS',
            'cargo' : 'operador'},
            {'nome' : 'LAURA',
            'cargo' : 'operador'},
            {'nome' : 'LEANDRO',
            'cargo' : 'operador'},
            {'nome' : 'LUCIANO',
            'cargo' : 'operador'},
            {'nome' : 'MATEUS',
            'cargo' : 'operador'},
            {'nome' : 'MAYGLEIDE',
            'cargo' : 'operador'},
            {'nome' : 'PAULO',
            'cargo' : 'operador'},
            {'nome' : 'PRISCILA',
            'cargo' : 'operador'},
            {'nome' : 'ROSE',
            'cargo' : 'operador'},
            {'nome' : 'VANILZA',
            'cargo' : 'operador'},
            {'nome' : 'WANDERSON',
            'cargo' : 'operador'},
            {'nome' : 'WESLEI',
            'cargo' : 'operador'},
            {'nome' : 'WOLLYSTON',
            'cargo' : 'operador'}]

        operador = [Operador(**data) for data in lista_operador]
        Operador.objects.bulk_create(operador)

    def add_maq_extrusao(self):
        lista_estrusoras = [
            {'marca' : 'EXTRUSORA 01',
            'modelo' : 'QUE CORTA'},
            {'marca' : 'EXTRUSORA 02',
            'modelo' : 'QUE CORTA'}]

        estrusora = [MaquinaExtrusao(**data) for data in lista_estrusoras]
        MaquinaExtrusao.objects.bulk_create(estrusora)

    def add_maq_impressao(self):
        lista_impressora = [
            {"marca" : "HECE", 'modelo' : "xpto"},
            {"marca" : "IMPRESSORA", 'modelo' : "600"},
            {"marca" : "IMPRESSORA", 'modelo' : "800"},
            {"marca" : "REINAFLEX", 'modelo' : "600"}
        ]

        impressora = [MaquinaImpressao(**data) for data in lista_impressora]
        MaquinaImpressao.objects.bulk_create(impressora)

    def add_corte(self):
        lista_corte = [
            {'marca' : 'SACOLEIRA', 'modelo' : 'xpto'},
            {'marca' : 'SANTORO', 'modelo' : '1000'},
            {'marca' : 'SANTORO', 'modelo' : '500 - 01'},
            {'marca' : 'SANTORO', 'modelo' : '500 - 02'},
            {'marca' : 'SANTORO', 'modelo' : '500 - 03'},
            {'marca' : 'SANTORO', 'modelo' : '500 - 04'},
            {'marca' : 'SANTORO', 'modelo' : '500 - 05'},
            {'marca' : 'SANTORO', 'modelo' : '500 - 06'},
            {'marca' : 'SANTORO', 'modelo' : '500 - 07'},
            {'marca' : 'SANTORO', 'modelo' : '500 - 08'},
            {'marca' : 'SANTORO', 'modelo' : '600'},
            {'marca' : 'SANTORO', 'modelo' : '800'}
            ]

        corte = [MaquinaCorte(**data) for data in lista_corte]
        MaquinaCorte.objects.bulk_create(corte)

    def add_Tratamento(self):
        lista_tratamento = [
            {'tratamento_produto' : 'TOTAL'},
            {'tratamento_produto' : 'FAIXA CENTRAL'},
            {'tratamento_produto' : 'DUAS PISTAS'},
            {'tratamento_produto' : 'SEM TRATAMENTO'},
            {'tratamento_produto' : 'FAIXA CENT.13 CM'},
            {'tratamento_produto' : 'FAIXA CENT.17 CM'},
            {'tratamento_produto' : 'FAIXA CENT.21 CM'},
            {'tratamento_produto' : 'FAIXA CENT. X CM'},
            {'tratamento_produto' : 'FAIXA LAT. (FUNDO 4 CM)'},
            {'tratamento_produto' : 'FAIXA LAT.(FUNDO 5 CM)'},
            {'tratamento_produto' : 'FAIXA LAT.(FUNDO 7 CM)'},
            {'tratamento_produto' : 'FAIXA LAT.(FUNDO X CM)'}
        ]

        tratamento = [Tratamento(**data) for data in lista_tratamento]
        Tratamento.objects.bulk_create(tratamento)

    def add_material(self):
        lista_material = [
            {'material_produto' : 'ALTA'},
            {'material_produto' : 'ALTA SOPRO'},
            {'material_produto' : 'BAIXA'},
            {'material_produto' : 'CANELA'},
            {'material_produto' : 'CARGA (CARBONATO DE CÁLCIO)'},
            {'material_produto' : 'INDUSTRIAL'},
            {'material_produto' : 'LINEAR'},
            {'material_produto' : 'OUTROS'},
            {'material_produto' : 'PIGMENTO'},
            {'material_produto' : 'RECICLADO COLORIDO'},
            {'material_produto' : 'RECUPERADO ALTA'},
            {'material_produto' : 'RECUPERADO BAIXA'}
        ]

        materiais = [Material(**data) for data in lista_material]
        Material.objects.bulk_create(materiais)

    def add_acabamento(self):
        lista_acabamento = [
            {'acabamento_produto' : 'ABERTA 1 LADO'},
            {'acabamento_produto' : 'COM ABA'},
            {'acabamento_produto' : 'COM ALÇA VAZADA'},
            {'acabamento_produto' : 'COM CORTE FRONHA'},
            {'acabamento_produto' : 'COM FITA ADESIVA'},
            {'acabamento_produto' : 'COM FURO CHAPÉU MEXICANO'},
            {'acabamento_produto' : 'COM FURO REDONDO'},
            {'acabamento_produto' : 'COM VERNIZ'},
            {'acabamento_produto' : 'COM ZIPLOCK'},
            {'acabamento_produto' : 'CORTE RASGA FÁCIL'},
            {'acabamento_produto' : 'ESPECIAL'},
            {'acabamento_produto' : 'ESTILO CAMISETA'},
            {'acabamento_produto' : 'FOLHA'},
            {'acabamento_produto' : 'FRENTE E VERSO'},
            {'acabamento_produto' : 'FURADO'},
            {'acabamento_produto' : 'HAMBURGUER'},
            {'acabamento_produto' : 'HOT DOG'},
            {'acabamento_produto' : 'LAMINADO'},
            {'acabamento_produto' : 'MINI HOT DOG'},
            {'acabamento_produto' : 'REFILADO'},
            {'acabamento_produto' : 'SANFONADO FUNDO'},
            {'acabamento_produto' : 'SANFONADO LATERAL'},
            {'acabamento_produto' : 'SEM SANFONA'},
            {'acabamento_produto' : 'SEM TRATAMENTO'},
            {'acabamento_produto' : 'SOLDA FUNDO'},
            {'acabamento_produto' : 'SOLDA POUCH LATERAL'},
            {'acabamento_produto' : 'TRATADO'},
            {'acabamento_produto' : 'TUBOLAR'},
        ]

        acabamentos = [Acabamento(**data) for data in lista_acabamento]
        Acabamento.objects.bulk_create(acabamentos)

    def add_cor(self):
        lista_cor = [
            {'cor_produto' : 'AMARELO'},
            {'cor_produto' : 'BRANCO LEITOSO'},
            {'cor_produto' : 'LARANJA'},
            {'cor_produto' : 'NATURAL FOSCO'},
            {'cor_produto' : 'ROSA'},
            {'cor_produto' : 'ROXO'},
            {'cor_produto' : 'TRANSPARENTE'},
            {'cor_produto' : 'VERDE'}
        ]

        cores = [CorProduto(**data) for data in lista_cor]
        CorProduto.objects.bulk_create(cores)

    def add_tintas(self):
        lista_cores = [
            {'cor' : 'CIANO'},
            {'cor' : 'MAGENTA'},
            {'cor' : 'AMARELO'},
            {'cor' : 'PRETO'},
            {'cor' : 'VERDE'}
            ]

        tintas = [Tinta(**data) for data in lista_cores]
        Tinta.objects.bulk_create(tintas)

    def add_ingredientes(self):
        lista_ingredientes = [
            {'ingrediente' : 'RECUPERADO AD'},
            {'ingrediente' : 'LINEAR BD'},
            {'ingrediente' : 'Polietileno de Alta Densidade'},
            {'ingrediente' : 'Polietileno B'},
            {'ingrediente' : 'Polietileno C'},
            {'ingrediente' : 'Polietileno D'},
            {'ingrediente' : 'Pigmento Branco GL 171 - 70%'},
            {'ingrediente' : 'Pigmento Verde'},
            {'ingrediente' : 'Pigmento A'},
            {'ingrediente' : 'Pigmento B'}
        ]

        ingredientes = [Ingredientes(**data) for data in lista_ingredientes]
        Ingredientes.objects.bulk_create(ingredientes)