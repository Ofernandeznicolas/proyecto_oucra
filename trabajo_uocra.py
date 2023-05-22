
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
            fecha_resultado += SumaDia  # Si el ultimo dia cae en una fecha o dia excluido voy sumando un dia hasta que el mismo no este excluido.
        
       
          
    return fecha_resultado

# Fecha inicio y la cantidad de días
fecha_inicio = datetime.strptime(input("Ingrese la fecha para iniciar el curso (DD-MM-YYYY): "), "%d-%m-%Y").date()
dias_total = int(input("Ingrese la cantidad de dias del curso: "))


# preguntar que dias de la semana puede asistir el docente

dias_no_laboral = []
dias_no_laboral_nombre = []
dia_no_laboral = input("Ingrese que dia de la semana no puede asistir el docente o presionar 9 para finalizar: ")
while dia_no_laboral != "9":
    if dia_no_laboral.lower() == "lunes":
       dia_no_laboral = 0
       dias_no_laboral_nombre.append("Lunes")
    elif dia_no_laboral.lower() == "martes":
        dia_no_laboral = 1
        dias_no_laboral_nombre.append("Martes")
    elif dia_no_laboral.lower() == "miercoles":
        dia_no_laboral = 2
        dias_no_laboral_nombre.append("Miercoles")
    elif dia_no_laboral.lower() == "jueves":
        dia_no_laboral = 3
        dias_no_laboral_nombre.append("Jueves")
    elif dia_no_laboral.lower() == "viernes":
        dia_no_laboral = 4
        dias_no_laboral_nombre.append("Viernes")
    elif dia_no_laboral.lower() == "sabado":
        dia_no_laboral = 5
        dias_no_laboral_nombre.append("Sabado")
    elif dia_no_laboral.lower() == "domingo":
        dia_no_laboral = 6
        dias_no_laboral_nombre.append("Domingo")
    else:
        print("Por favor ingrese un dia correcto EJ: Martes")
        
    dias_no_laboral.append(int(dia_no_laboral))
    dia_no_laboral = input("Ingrese otro día de la semana que no pueda asistir el docente o presionar 9 para finalizar: ")

# fechas para feriados o paros
fechas_excluidas = []
fechas_excluidas_str = []
fecha_excluir = input("Con el siguiente formato DD-MM-YYYY ingrese feriados o dias no laborables para excluirlos del contador o presionar 0 para finalizar: ")
while fecha_excluir != "0":
    try:
        fecha_excluir = datetime.strptime(fecha_excluir, "%d-%m-%Y").date()
        fechas_excluidas.append(fecha_excluir)
        fechas_excluidas_str.append(fecha_excluir.strftime("%d-%m-%Y"))
    except ValueError:
        print("Formato de fecha incorrecto. Por favor, ingrese nuevamente la fecha en el formato DD-MM-YYYY.")

    fecha_excluir = input("Ingrese otro feriado o día no laboral para excluirlo del contador con el formato DD-MM-YYYY (presione 0 para finalizar): ")

print(fechas_excluidas_str)

# resultado de la fecha
fecha_resultado = Fecha_Finalizacion_Curso(dias_total, fecha_inicio, fechas_excluidas, dias_no_laboral)


# devolver el resultado de la fecha
print(f"La fecha de finalizacion del curso es: {fecha_resultado}")

# Devolver los dias que no se brindara clases en la semana
if len(dias_no_laboral_nombre) == 1:
    print(f"El dia de la semana que el docente no brindara clase : {dias_no_laboral_nombre}")
else:
    print(f"Los dias de la semana que el docente no brindara clases : {dias_no_laboral_nombre}")
    
    
# Devolver las fechas que no se brindaran clases
if len(fechas_excluidas_str) == 1:
    print(f"La fecha excluida que no se brindara clases sera: {fechas_excluidas_str}")
else:
    print(f"Las fechas excluidas que no se brindaran clases seran: {fechas_excluidas_str}")