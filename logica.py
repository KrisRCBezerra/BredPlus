import datetime
class Nota:
    def __init__(self, produto, data, status):
        self.produto = produto
        self.data = data
        self.status = "em aberto"
        
    def adicionar_produto(self, produto):
        self.produto = input("Digite o nome do produto: ")
        print(f'Produto: {self.produto}, adicionado com sucesso')

    def adicionar_data(self, data):
        self.data = input("Digite a data de emissão (YYYY-MM-DD): ")
        ano, mes, dia = map(int, data.split("-"))
        self.data = data = datetime.date(ano, mes, dia)
        print(f'Data de emissão atualizada para {data}')

    def mudar_status(self, status):
        self.status = input("Digite o status da nota (cancelado, ok): ")
        if self.status == "ok":
            self.status = "ok"
        elif self.status == "cancelado":
            self.status = "cancelado"
        else:
            self.status = "em aberto"
        print(f'Status atualizado para {self.status}')