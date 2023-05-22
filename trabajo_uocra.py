
# Importar de la biblioteca  datetime para trabajar con fechas.
from datetime import datetime, timedelta, date

# defino funcion para llegar a la fecha final del curso, incrementando los dias por dia/s no laboral/es o feriado/s
def Fecha_Finalizacion_Curso(cantidad_dias, fecha_inicio, fechas_excluidas, dias_no_laboral):
    
    SumaDia = timedelta(days=1)  # Variable con valor de 1 dia.
    
    contador_dias = 1  # Variable para contador de dias.
    
    fecha_resultado = fecha_inicio  # Variable para mi fecha inicial la cual voy a ir sumando. Contador fechas
    
    while contador_dias < cantidad_dias:
        
        
        # Verifico si la fecha resultante no es un día hábil (lunes a viernes) y no está en los días excluidos (feriados y dias no laborales)
        if fecha_resultado.weekday() < 5 and fecha_resultado not in fechas_excluidas and fecha_resultado.weekday() not in dias_no_laboral:
            contador_dias += 1  # Incremento el contador de los dias cursados mientras la fecha no este excluida.
            fecha_resultado += SumaDia
        else: 
            fecha_resultado += SumaDia

        while fecha_resultado.weekday() in dias_no_laboral or fecha_resultado.weekday() > 4 or fecha_resultado in fechas_excluidas:
            fecha_resultado += SumaDia 
        
       
          
    return fecha_resultado

# Fecha inicio y la cantidad de días
fecha_inicio = datetime.strptime(input("Ingrese la fecha para iniciar el curso (DD-MM-YYYY): "), "%d-%m-%Y").date()
dias_total = int(input("Ingrese la cantidad de dias del curso: "))

# preguntar que dias de la semana puede asistir el docente

dias_no_laboral = []
dia_no_laboral = input("Ingrese el dia que no puede asistir el docente o presionar 9 para finalizar: ")
while dia_no_laboral != "9":
    dias_no_laboral.append(int(dia_no_laboral))
    dia_no_laboral = input("Ingrese otro día que no puede asistir el docente o presionar 9 para finalizar: ")

# fechas para feriados o paros
fechas_excluidas = []
fecha_excluir = input("Con el siguiente formato DD-MM-YYYY ingrese feriados o dias no laborables para excluirlos del contador o presionar 0 para finalizar: ")
while fecha_excluir != "0":
    fecha_excluir = datetime.strptime(fecha_excluir, "%d-%m-%Y").date()
    fechas_excluidas.append(fecha_excluir)
    fecha_excluir = input("Ingrese otro feriado o dia no laboral para excluirlo del contador con el formato DD-MM-YYYY o presionar 0 para finalizar: ")

# resultado de la fecha
fecha_resultado = Fecha_Finalizacion_Curso(dias_total, fecha_inicio, fechas_excluidas, dias_no_laboral)

# devolver el resultado de la fecha
print(f"La fecha de finalizacion del curso excluyendo el/los dia/s {dias_no_laboral} y el/los feriado/s {fechas_excluidas} es: {fecha_resultado}")