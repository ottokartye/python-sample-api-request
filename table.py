from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['ID', 'Firstname', 'Lastname', 'Age']

table.add_row(['1', 'Otto', 'Kartye', '36'])
table.add_row(['2', 'Adi', 'Cartis', '36'])

print(table)

