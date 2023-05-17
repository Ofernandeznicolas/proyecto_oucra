
# Importar de la biblioteca  datetime para trabajar con fechas.
from datetime import datetime, timedelta, date

# definir funcion para que me realice la suma de los dias.
# definir los argumentos de la funcion.
def Fecha_Finalizacion_Curso(cantidad_dias, fecha_inicio, fechas_excluidas, dias_no_laboral):
    delta = timedelta(days=1)  # Crea un delta de tiempo de un día
    
    contador_dias = -1  # Inicializa el contador de días hábiles
    
    fecha_resultado = fecha_inicio  # Inicializa la fecha resultante
    
    while contador_dias < cantidad_dias:
        fecha_resultado += delta  # Suma un día a la fecha actual
        
        # Verifica si la fecha resultante es un día hábil (lunes a viernes) y no está en los días excluidos
        if fecha_resultado.weekday() < 5 and fecha_resultado not in fechas_excluidas and fecha_resultado not in dias_no_laboral:
            contador_dias += 1  # Incrementa el contador de días hábiles
    
    return fecha_resultado

# Fecha inicio y la cantidad de días
fecha_inicio = datetime.strptime(input("Ingrese la fecha para iniciar el curso (YYYY-MM-DD): "), "%Y-%m-%d").date()
dias_total = int(input("Ingrese la cantidad de dias del curso: "))

# preguntar que dias de la semana puede asistir el docente
# 0 - lunes - 1 martes.... 6 domingo (CAMBIAR para que ingrese nombre y guardar como numero)
dias_no_laboral = []
dia_no_laboral = input("Ingrese el dia que no puede asistir el docente o presionar 0 para finalizar: ")
while dia_no_laboral != "0":
    dias_no_laboral.append(int(dia_no_laboral))
    dia_no_laboral = input("Ingrese otro día que no puede asistir el docente o presionar 0 para finalizar: ")

# fechas para feriados o paros
# Mejorar las indicaciones ?
fechas_excluidas = []
fecha_excluir = input("Con el siguiente formato YYYY-MM-DD ingrese feriados o dias no laborables para excluirlos del contador o presionar 0 para finalizar: ")
while fecha_excluir != "0":
    fecha_excluir = datetime.strptime(fecha_excluir, "%Y-%m-%d").date()
    fechas_excluidas.append(fecha_excluir)
    fecha_excluir = input("Ingrese otro feriado o dia no laboral para excluirlo del contador con el formato YYYY-MM-DD o presionar 0 para finalizar: ")

# resultado de la fecha
fecha_resultado = Fecha_Finalizacion_Curso(dias_total, fecha_inicio, fechas_excluidas, dias_no_laboral)

# devolver el resultado de la fecha
### cambio
print(f"La fecha de finalizacion del curso excluyendo el/los dia/s {dias_no_laboral} y el/los feriado/s {fechas_excluidas} es: {fecha_resultado}")