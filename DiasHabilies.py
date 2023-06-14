import requests
from datetime import datetime, timedelta, date, time 

class diasHabiles():
    def __init__(self, año):
        self.año = año
        self.diasUocra = None
        self.diasUocraSRT = None
        self.feriados = None
        self.feriadosSRT = None
    
    
    def Caracteristicas(self):
        print(f"El año es : {self.año}")

    
    def Feriados(self):
        def obtener_feriados(año): # a traves de la api de feriados argentinos obtengo los feriados.
            url = f"http://nolaborables.com.ar/api/v2/feriados/{año}"
            
            response = requests.get(url)
            feriados = response.json()
            
            return feriados


        año = self.año # indico el año del que voy a obtener los feriados
        feriados = obtener_feriados(año)

        fechasGuardadas = [] # Lista temporal para almacenar los datos que necesito de la api
        fechasFeriados = []  # lista final donde voy a guardar las fechas
        fechasFeriadosSTR = [] # Lista para guardar feriados STR
        for feriado in feriados: # recorro los diccionarios de la api y busco dia y mes para almacenar la fecha
            fechasGuardadas.append(feriado["dia"])
            fechasGuardadas.append(feriado["mes"])
            if len(fechasGuardadas) == 2: # si mi lista temporal almacena ya los 2 datos que necesito le indico que:
                feriado = (f"{fechasGuardadas[0]}-{fechasGuardadas[1]}-2023")  # me guarde la fecha de forma completa (str)
                fecha = datetime.strptime(feriado,"%d-%m-%Y").date() # me la transforme a fecha
                fechasFeriados.append(fecha) # me la almacene en mi lista final de feriados
                fechasGuardadas = [] # borro mi lista temporal para volver almacenar datos
        
        self.feriados = fechasFeriados

        for fecha in fechasFeriados: # corroboro con una impresion de los datos.
            fecha_str = fecha.strftime("%d-%m-%Y")
            fechasFeriadosSTR.append(fecha_str)
            print(fecha_str)
            
        print(fechasFeriadosSTR)    
        
        self.feriados = fechasFeriados
        self.feriadosSRT = fechasFeriadosSTR
    
        return
    
    def ImprimirFeriados(self):
        for i in self.feriadosSRT:
            print(f"Fecha : {i}")
    
    def ImprimirDiasUocra(self):
        for i in self.diasUocraSRT:
            print(f" Dia Uocra : {i}")
    
    def DiasUocra(self):
        diasUocra = [] # Lista para almacenar mis fechas con formato date.
        diasUocraSTR = [] # Lista para almacenar mis fechas con formato STR.

         #Preguntar si quiere ingresar una fecha.
        IngresarFecha = input("Le gustaria ingresar una fecha que no se encuentre dentro de los feriados ? Inque con Si o No \n").lower()
        def Modificar():
            
            for dia in diasUocraSTR:# Con un for recorro todas las fechas almacenadas en mi variable y pregunto uno por uno si quiere cambiarla
                Modificar = input(f"Modificar fecha : {dia} ? SI o NO\n").lower() #Pregunto si quiere modificar la fecha por cada recorrido en mi for
        
                if Modificar != "si" or Modificar != "no":  # Realizo una validacion por si ingresa algo distinto a si o no
                    while Modificar != "si" and Modificar != "no":
                        Modificar = input(f"Por favor indique de manera correcta con un SI o un NO si desea modificar la fecha {dia} \n")
                    
                if Modificar == "si":    #Si quiere modificar:
                    posicion = diasUocraSTR.index(dia) #Busco en mi lista STR la posicion para eliminarlo en mi lista con formato date. 
                    diasUocraSTR.remove(dia) # Remuevo la fecha en la lista STR.
                    del diasUocra[posicion] # con la posicion remuevo la fecha en mi lista con formato date.
                    IngresarFecha = input("Ingrese la fecha correcta (dia - mes - año) con el formato DD-MM-YYYY : \n")
                
                    try: # Utilizo para verificar si lo ingresado cumple con el formato de fecha
                        FechaExcluida = IngresarFecha
                        FechaExcluida = datetime.strptime(FechaExcluida, "%d-%m-%Y").date()
                        diasUocra.append(FechaExcluida)
                        diasUocraSTR.append(FechaExcluida.strftime("%d-%m-%Y"))
                        
                    except ValueError: # Si el mismo es incorrecto le indico que ingrese nuevamente con el formato pedido
                        print("Formato de fecha incorrecto, por favor ingrese el dia y el mes con el formato DD-MM-YYYY (DIA-MES-AÑO): \n")
                if Modificar == "no":
                    continue
                
        #Si desea ingresar una fecha: 
        while IngresarFecha == "si": # Realizo un bucle para poder convalidar otras modificaciones.
            
            if IngresarFecha == "si": # Si desea modificar una fecha
                
                FechaExcluida = input("Con el siguiente formato DD-MM-YYY ingrese la fecha: \n") # Le pido el ingreso de la fecha
                
                try: # a traves nuevamente de un try y un except verifico que ingrese el formato correcto de la fecha
                    FechaExcluida = datetime.strptime(FechaExcluida, "%d-%m-%Y").date()
                    diasUocra.append(FechaExcluida)
                    diasUocraSTR.append(FechaExcluida.strftime("%d-%m-%Y"))
                except ValueError:
                    print("Formato de fecha incorrecto, por favor ingrese el dia y el mes con el formato DD-MM (DIA-MES)")

                #Pregunto si quiere ingresar una nueva fecha.
                IngresarFecha = input("Desea ingresar otra fecha? Si para continuar ingresando fechas - No para finalizar con el ingreso de fechas\n")#
            
            
            if IngresarFecha == "no": # Si ingresa no, recorro las fechas ingresadas para corroborar que las mismas sean correctas.
                print("Perfecto, las fechas ingresadas fueron : ")
                for dias in diasUocraSTR:
                    print(f"Fecha :  {dias}")
            
                
                CorroborarFecha = input(""" 
                                            Si las fechas son correctas y no desea agregar mas fechas indique: Salir 
                                            Si desea agregar una fecha mas indique : Agregar 
                                            Si desea modificar alguna fecha indique : Modificar\n""").lower()
                
                if CorroborarFecha == "salir":#
                    print("Las fechas fueron almacenadas correctamente")
                    IngresarFecha = "no"
                elif CorroborarFecha == "agregar":#
                    IngresarFecha = "si"#
                elif CorroborarFecha == "modificar":#
                    abc = True # en una variable indico true para crear otro bucle (puse abc porque fue lo primero que se me vino xD)
                    while abc == True:
                        Modificar() # Llamo a mi funcion modificar 
                        print("Las fechas actualizadas quedaron de la siguiente mantera: ") #Una vez que sale de dicha funcion vuelvo a mostrar de que manera quedaron las fechas
                        
                        for dia in diasUocraSTR:
                            print(f"Fecha : {dia}")
                            
                        abc = input("""
                                        Si las fechas actaulizadas quedaron de forma correcta ingrese : CORRECTO
                                        Si desea agregar una fecha mas ingrese: AGREGAR
                                        Si desea Modificar las fechas ingrese : Modificar \n""").lower()
                        
                        #Dependiendo de la opcion que ingrese seguira con el bucle o saldra del mismo.
                        if abc == "correcto":
                            IngresarFecha = "no"
                            abc = False
                        elif abc == "agregar":
                            IngresarFecha = "si"
                            abc = False
                        elif abc == "modificar":
                            abc = True
        self.diasUocra = diasUocra
        self.diasUocraSRT = diasUocraSTR
        return self.diasUocra





prueba = diasHabiles(2023)                    

print(prueba.Caracteristicas())

prueba.Feriados()
prueba.DiasUocra()

prueba.ImprimirDiasUocra()
prueba.ImprimirFeriados()
