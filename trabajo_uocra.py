from datetime import datetime, timedelta, date, time  # Biblioteca datetime para fechas.

# Ingreso de Nombre del curso, profesor, cantidad de horas
nombre_curso = input("Ingrese el nombre del curso : \n")

nombre_docente =input("Ingresar nombre del/de la docente : \n")

horas_total_curso = int(input("Ingrese la cantidad total de horas del curso : "))
horas_total_curso2 = horas_total_curso
horas_total_curso = timedelta(hours=horas_total_curso)

condicion = True  # Ingreso del tipo de hora Catedra - Practica con una validacion si el mismo es incorrecto
while condicion == True:
    tipo_curso = input("Ingrese que tipo de hora corresponde al curso PRACTICA o CATEDRA : \n")
    if tipo_curso.lower() != "catedra" and tipo_curso.lower() != "practica":
        tipo_curso = ("Por favor ingrese de forma correcta el tipo de hora que corresponde al curso : PRACTICA o CATEDRA \n")
    else:
        condicion = False
 

# cantidad de horas por dia que brindara clases dependiendo del tipo de horas
def cantidad_dias_curso(tipo_curso):
    
    horas_dia = int(input(f"Ingrese la cantidad de horas {tipo_curso.lower()} por dia que puede brindar clases: "))
    
    if tipo_curso.lower() == "catedra":
        horas_dias2 = timedelta(minutes= 40 * horas_dia)
        cantidad_dias = horas_total_curso / horas_dias2
        

        if isinstance(cantidad_dias, float):
         cantidad_dias = int(cantidad_dias) + 1
    #
    #
    elif tipo_curso.lower() == "practica":
        horas_dias2 = timedelta(minutes= 60 * horas_dia)
        cantidad_dias = horas_total_curso / horas_dias2
    
    print(f"El curso de {nombre_curso} se brindara en un total de {cantidad_dias} dias")
    return cantidad_dias


cantidad_dias = cantidad_dias_curso(tipo_curso)


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
continuar = True

while continuar == True:
    utilizar_calculo_dias = input("Desea utilizar la cantidad de dias obtenidos para calcular la finalizacion del curso? : ")
    
    if utilizar_calculo_dias.lower() == "si":
        dias_total = cantidad_dias
        continuar = False
    elif utilizar_calculo_dias.lower() == "no":
        opcion_dias = input("Si quiere ingresar de forma manual la cantidad dias del curso ingrese :'Manual' \n Si quiere volver a realizar el calculo de dias ingrese: 'Calculo'")
        if opcion_dias.lower() == "manual":
            dias_total = int(input("Ingrese la cantidad de dias con la cual quisiera calcular la finalizacion del curso: "))
            continuar = False
        elif opcion_dias.lower() == "calculo":
            cantidad_dias = cantidad_dias_curso(tipo_curso)
            
        


fecha_inicio = datetime.strptime(input("Ingrese la fecha para iniciar el curso (DD-MM-YYYY): "), "%d-%m-%Y").date()

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

#print(fechas_excluidas_str)


# resultado de la fecha
fecha_resultado = Fecha_Finalizacion_Curso(dias_total, fecha_inicio, fechas_excluidas, dias_no_laboral)


# devolver el resultado de la fecha

print(f"El/La Docente {nombre_docente} correspondiente al curso {nombre_curso} de {horas_total_curso2} hs total \n")

if tipo_curso.lower() == "catedra":
    hora_catedra = timedelta(minutes=40)
    total_horas_catedra = horas_total_curso / hora_catedra
    print(f"Tipo hora : Catedra \n Total de horas catedra: {total_horas_catedra} \n ")

print(f"La fecha de inicio del curso es: {fecha_inicio} \n")    
print(f"La fecha de finalizacion del curso es: {fecha_resultado} \n")


# Devolver los dias que no se brindara clases en la semana
# if len(dias_no_laboral_nombre) == 1:
#     print(f"El/La docente no brindara clase los dias : {dias_no_laboral_nombre} \n")
# else:
#     print(f"Los dias de la semana que la/el docente no brindara clases : {dias_no_laboral_nombre} \n")
 
print(f"El/La docente no brindara clase los dias : {dias_no_laboral_nombre} \n")    
    
# Devolver las fechas que no se brindaran clases
if len(fechas_excluidas_str) == 1:
    print(f"La fecha excluida que no se brindara clases sera: {fechas_excluidas_str} \n")
else:
    print(f"Las fechas excluidas que no se brindaran clases seran: {fechas_excluidas_str} \n")
    
    
####### obtener feriados ###


import requests

def obtener_feriados(año, incluir_opcional=False):
    url = f"http://nolaborables.com.ar/api/v2/feriados/{año}"
    
    if incluir_opcional:
        url += "?incluir=opcional"
    
    response = requests.get(url)
    feriados = response.json()
    
    return feriados


año = 2023
feriados = obtener_feriados(año)

for feriado in feriados:
    motivo = feriado["motivo"]
    tipo = feriado["tipo"]
    dia = feriado["dia"]
    mes = feriado["mes"]
    id_feriado = feriado["id"]
    
    print(f"Motivo: {motivo}")
    print(f"Tipo: {tipo}")
    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"ID: {id_feriado}")
    print("-------------------------")
    




print(feriados)