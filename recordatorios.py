
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]


# AQUI AGREGO UNA NUEVA LINEA QUE NO ESTABA ANTES
recordatorios.append(['2021-01-02', '06:00', 'Empezar el año'])


# AQUI MODIFICO LA FECHA LA CUAL ERA 2021-07-15'
recordatorios [2][0] = '2021-07-16'

# eliminar el evento del dia del trabajo
recordatorios.pop(1)

# AQUI AGREGO UNA NUEVA LINEA QUE NO ESTABA ANTES
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# PARA ORDENAR LA LISTA DE ACUERDO A LAS FECHAS USO EL SORT, ME DEVUELVE LAS LISTA EN ORDEN
recordatorios.sort()

# Output
for lista_recordatorio in recordatorios:
    print(f"[{lista_recordatorio[0]}, {lista_recordatorio[1]}, {lista_recordatorio[2]}]")

# print(recordatorios[0])
# print(recordatorios[1])
# print(recordatorios[2])
# print(recordatorios[3])
# print(recordatorios[4])
# print(recordatorios[5])
# print(recordatorios[6])

