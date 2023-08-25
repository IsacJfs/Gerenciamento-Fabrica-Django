from django.core.management.base import BaseCommand
from gerenciamento.models import Cliente, Endereco



class Command(BaseCommand):
    help = 'Adiciona clientes ao banco de dados'

    def handle(self, *args, **kwargs):
        # Chamando o método para adicionar clientes
        self.add_clientes()

        self.stdout.write(self.style.SUCCESS('Clientes adicionados com sucesso!'))

    def add_clientes(self):
        clientes_data = [
            {'cnpj_cpf' : '51372408000125',
            'razao_social' : 'Louise e Bryan Marcenaria ME',
            'nome_fantasia' : 'nomeFantasia',
            'celular' : '6436992684',
            'email' : 'representantes@louiseebryanmarcenariame.com.br',
            'atividade_economica_profissao' : 'comercio'},
            {'cnpj_cpf' : '90846189000120',
            'razao_social' : 'Carlos e Bryan Gráfica ME',
            'nome_fantasia' : 'nomeFantasia',
            'celular' : '6127298588',
            'email' : 'seguranca@carlosebryangraficame.com.br',
            'atividade_economica_profissao' : 'comercio'},
            {'cnpj_cpf' : '65702577000190',
            'razao_social' : 'Fábio e Carla Entregas Expressas Ltda',
            'nome_fantasia' : 'nomeFantasia',
            'celular' : '6128712042',
            'email' : 'tesouraria@fabioecarlaentregasexpressasltda.com.br',
            'atividade_economica_profissao' : 'comercio'},
            {'cnpj_cpf' : '10640555000151',
            'razao_social' : 'Giovana e Otávio Advocacia Ltda',
            'nome_fantasia' : 'nomeFantasia',
            'celular' : '6435485251',
            'email' : 'faleconosco@giovanaeotavioadvocacialtda.com.br',
            'atividade_economica_profissao' : 'comercio'},
            {'cnpj_cpf' : '66530129000110',
            'razao_social' : 'Yuri e Jorge Padaria ME',
            'nome_fantasia' : 'nomeFantasia',
            'celular' : '6136477010',
            'email' : 'producao@yuriejorgepadariame.com.br',
            'atividade_economica_profissao' : 'comercio'},
            {'cnpj_cpf' : '47473141000195',
            'razao_social' : 'Manuel e Maitê Telecom Ltda',
            'nome_fantasia' : 'nomeFantasia',
            'celular' : '6228241934',
            'email' : 'presidencia@manuelemaitetelecomltda.com.br',
            'atividade_economica_profissao' : 'comercio'}
        ]

        clientes = [Cliente(**data) for data in clientes_data]
        Cliente.objects.bulk_create(clientes)

        

