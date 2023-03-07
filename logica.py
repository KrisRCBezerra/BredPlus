import datetime
produto = input("Digite o nome do produto: ")
data_str = input("Digite a data de emissão (YYYY-MM-DD): ")

ano, mes, dia = map(int, data_str.split("-"))
data = datetime.date(ano, mes, dia)