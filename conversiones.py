'''
Considere las siguientes tasas de conversión de Peso Chileno:
● a Sol peruano: 0.0046
● a Peso Argentino: 0.093
● a Dólar Americano: 0.00013
'''
import sys

# Coloque int y float para que estos multipliquen
pesos_chilenos  = int(sys.argv[-1])
sol_peruano     = float(sys.argv[1])
peso_argentino  = float(sys.argv[2])
dolar_americano = float(sys.argv[3])

print(f"Los {pesos_chilenos} pesos equivalen a: ")
print(f"{sol_peruano*pesos_chilenos} Soles")
print(f"{peso_argentino*pesos_chilenos} Pesos Argentinos")
print(f"{dolar_americano*pesos_chilenos} Dólares ")
