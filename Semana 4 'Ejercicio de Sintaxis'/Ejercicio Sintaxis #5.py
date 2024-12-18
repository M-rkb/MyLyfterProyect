total_notas=int(input("Ingrese total de notas: "))
contador_de_notas=0
can_notas_desaprobadas=can_notas_aprobadas=0
prom_notas_desaprobadas=prom_notas_aprobadas=prom_notas_total=0
while contador_de_notas<total_notas:
    nota_actual=int(input('Ingrese nota numero'+str(contador_de_notas + 1) + ': '))
    if nota_actual>=70:
        can_notas_aprobadas+=1
        prom_notas_aprobadas+=nota_actual
    else:
        can_notas_desaprobadas+=1
        prom_notas_desaprobadas+=nota_actual
    prom_notas_total+=nota_actual/total_notas
    contador_de_notas+=1
if can_notas_aprobadas > 0:
    prom_notas_aprobadas = prom_notas_aprobadas / can_notas_aprobadas
else:
    prom_notas_aprobadas = 0    
if can_notas_desaprobadas > 0:
    prom_notas_desaprobadas = prom_notas_desaprobadas / can_notas_desaprobadas
else:
    prom_notas_desaprobadas = 0
print('El estudiante tiene esta cantidad de notas aprobadas:',can_notas_aprobadas)
print('Este es el promedio de notas aprobadas:',prom_notas_aprobadas)
print('El estudiante tiene esta cantidad de notas desaprobadas:',can_notas_desaprobadas)
print('Este es el promedio de notas desaprobadas:',prom_notas_desaprobadas)
print('Este es el promedio de notas:',prom_notas_total)
