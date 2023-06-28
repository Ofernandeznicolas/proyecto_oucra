"""Codigo para la obtencion de cantidad de cada dias
de la semana(lunes a viernes) pasandole desde que fecha
hasta que fecha sin contar los feriados"""


from datetime import datetime, timedelta, date, time 
import requests

class CalculoDias:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
        self.año = None
        self.feriados = None
        self.lista = None
    
    
    def __str__(self):
        return "Clase para almacenar la cantidad de dias de la semana en una lista"
    
    def get_lista(self):
        return self.lista
    
    def CalculoAño(self):
        año1 = self.inicio[-4:]
        self.año = año1
            
    
    def formatoDATE(self):
        inicio = self.inicio
        inicio = datetime.strptime(inicio, "%d-%m-%Y").date()
        
        fin = self.fin
        fin = datetime.strptime(fin, "%d-%m-%Y").date()
        
        self.inicio = inicio
        self.fin = fin
        
        print(inicio)
        print(fin)
        return self.inicio, self.fin
    
    def Feriados (self):
        self.CalculoAño()
        
        año = self.año
        url = f"http://nolaborables.com.ar/api/v2/feriados/{año}"
        
        respuesta = requests.get(url)
        resultado = respuesta.json()
        
        feriados = []
        año =str(año)
        
        for i in resultado:
            dia = str(i["dia"])
            mes = str(i["mes"])
            fecha = f"{dia}-{mes}-{año}"
            fecha = datetime.strptime(fecha, "%d-%m-%Y").date()
            feriados.append(fecha)
        
        self.feriados = feriados
        return self.feriados
    
    
    def CalcularDias(self):
        self.Feriados()
        self.formatoDATE()           
        
        Dias = []
        lunes = 0
        martes = 0
        miercoles = 0
        jueves = 0
        viernes = 0
        
        contador = self.inicio    
        
        while contador != self.fin:
            if contador.weekday() == 0 and contador not in self.feriados:
                lunes += 1
            elif contador.weekday() == 1 and contador not in self.feriados:
                martes += 1
            elif contador.weekday() == 2 and contador not in self.feriados:
                miercoles += 1
            elif contador.weekday() == 3 and contador not in self.feriados:
                jueves += 1
            elif contador.weekday() == 4 and contador not in self.feriados:
                viernes += 1
        
            contador += timedelta(days=1)      
        
        Dias.append(lunes)
        Dias.append(martes)
        Dias.append(miercoles)
        Dias.append(jueves)
        Dias.append(viernes)
        
        self.lista = Dias
        return self.lista            

        
"""Realizar un imput para la entrada de 
fecha inicial y final"""

# inicial = input("Ingrese dia inicial formato dd-mm-yyyy")
# final = input ("Ingrese dia final con el formato dd-mm-yyyy")


def ObtenerLista(inicial="01-08-2023", final="31-08-2023"):
    prueba = CalculoDias(inicial,final)
    prueba.CalcularDias()  
    lista = prueba.get_lista()
    return lista

lista = ObtenerLista()

print(lista)
