from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['1', '2', '3']
table.add_row(['4', '5', '6'])

print(table)
