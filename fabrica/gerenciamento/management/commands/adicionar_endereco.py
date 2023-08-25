from django.core.management.base import BaseCommand
from gerenciamento.models import Cliente, Endereco



class Command(BaseCommand):
    help = 'Adiciona clientes ao banco de dados'

    def handle(self, *args, **kwargs):
        # Chamando o método para adicionar clientes
        self.add_endereco()

        self.stdout.write(self.style.SUCCESS('Endereços adicionados com sucesso!'))

    def add_endereco(self):
        enderecos_data = [
            {'cliente_codigo' : 2,
                'rua' : 'Avenida Farid Miguel Safatle',
            'numero' : '825',
            'complemento' : 'Setor Central',
            'cidade' : 'Catalão',
            'estado' : 'GO',
            'cep' : '75701040'},
            {'cliente_codigo' : 3,
                'rua' : 'Quadra Quadra 44',
            'numero' : '275',
            'complemento' : 'Parque das Águas Bonitas I',
            'cidade' : 'Águas Lindas de Goiás',
            'estado' : 'GO',
            'cep' : '72926086'},
            {'cliente_codigo' : 4,
                'rua' : 'Rua 5',
            'numero' : '380',
            'complemento' : 'Parque da Colina I',
            'cidade' : 'Formosa',
            'estado' : 'GO',
            'cep' : '73808016'},
            {'cliente_codigo' : 5,
                'rua' : 'Alameda Rio Doce',
            'numero' : '830',
            'complemento' : 'Conjunto Rio Claro III',
            'cidade' : 'Jataí',
            'estado' : 'GO',
            'cep' : '75804282'},
            {'cliente_codigo' : 6,
                'rua' : 'Quadra Quadra 144',
            'numero' : '687',
            'complemento' : 'Mansões de Recreio Estrela Dalva IV',
            'cidade' : 'Luziânia',
            'estado' : 'GO',
            'cep' : '72856090'},
            {'cliente_codigo' : 7,
                'rua' : 'Avenida Dom Bosco',
            'numero' : '428',
            'complemento' : 'Anexo Bom Sucesso',
            'cidade' : 'Anápolis',
            'estado' : 'GO',
            'cep' : '75045350'}
            ]

        for endereco_data in enderecos_data:
            # Encontre o cliente correspondente pelo código
            cliente = Cliente.objects.get(codigo=endereco_data['cliente_codigo'])

            # Crie um objeto de endereço e associe-o ao cliente
            endereco = Endereco(
                cliente=cliente,
                rua=endereco_data['rua'],
                numero=endereco_data['numero'],
                cidade=endereco_data['cidade'],
                estado=endereco_data['estado'],
                cep=endereco_data['cep']
            )
            endereco.save()