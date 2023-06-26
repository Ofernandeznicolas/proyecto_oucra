"""Codigo para obtener los valores 
de mi base de datos, y luego los paso
a formato DATE para asi poder realizar los calculos"""

import sqlite3
from datetime import datetime, timedelta, date, time

class valoresBD:
    def __init__(self, conexion):
        self.conect = conexion
        self.conexion = sqlite3.connect(conexion)
        self.cursor = self.conexion.cursor()
        
        self.fechaInicioYfin = None
        self.FechasFeriadosDate = None
    
    """Metodo para conectarme con la BD"""    
    def conectar(self):
        self.conexion = sqlite3.connect(self.conect)
        
        self.cursor = self.conexion.cursor()
        
        return self.conexion, self.cursor        
    
    """Metodo para devolver los valores 
    de inicio y fin de cuatrimestre
    en formato DATE - Los mismos se almacenan
    en un diccionario con el año como clave
    para acceder a ellos"""
    def inicioYfinCuatrimestres(self):
        self.conectar()

        self.cursor.execute("SELECT * FROM Fecha")
        
        resultados = self.cursor.fetchall()
        diccionario = {}

        for fila in resultados:
            año = fila[0]
            inicio_1er_cuatriDATE = fila[1]
            inicio_1er_cuatriDATE = datetime.strptime(inicio_1er_cuatriDATE, "%d-%m-%Y").date()
            fin_1er_cuatriDATE = fila[2]
            fin_1er_cuatriDATE = datetime.strptime(fin_1er_cuatriDATE, "%d-%m-%Y").date()
            inicio_2do_cuatriDATE = fila[3]
            inicio_2do_cuatriDATE = datetime.strptime(inicio_2do_cuatriDATE, "%d-%m-%Y").date()
            fin_2do_cuatriDATE = fila[4]
            fin_2do_cuatriDATE = datetime.strptime(fin_2do_cuatriDATE, "%d-%m-%Y").date()
            
            diccionario[año] = {
                "inicio_primer_cuatrimestre" : inicio_1er_cuatriDATE,
                "fin_primer_cuatrimestre": fin_1er_cuatriDATE,
                "inicio_segundo_cuatrimestre": inicio_2do_cuatriDATE,
                "fin_segundo_cuatrimestre": fin_2do_cuatriDATE      
            }
        
        self.conexion.close()      
                
        self.fechaInicioYfin = diccionario
        
        return self.fechaInicioYfin 
    
    """Metodo para devolver los feriados en formato DATE
    para el calculo de dias"""
    def feriados(self):
        self.conectar()
        
        self.cursor.execute("SELECT FechaFeriado FROM TablaFeriados")
        
        resultado = self.cursor.fetchall()
        fechasFeriados = []
        
        for fila in resultado:
            fecha = fila[0]
            fechasFeriados.append(fecha)
            
        print(fechasFeriados)
        self.conexion.close()
        
        fechasFeriadosDATE = []
        
        for i in fechasFeriados:
            fecha = i
            fecha = datetime.strptime(fecha, "%d-%m-%Y").date()
            fechasFeriadosDATE.append(fecha)
        
        self.FechasFeriadosDate = fechasFeriadosDATE
        
        print(fechasFeriadosDATE)
        return self.FechasFeriadosDate
    
"""Asigno una variable con la direccion de la Base de Datos"""        
conexion = "C:/Users/ofern/OneDrive/Escritorio/Proyecto Oucra/proyecto_oucra/base de datos/BDtrabajoUocra.db"

"""Asigno una variable con la clase que me va a devolver los resultados
que necesito en formato DATE"""
Prueba3 = valoresBD(conexion)

"""Llamo a el metodo que ejecuta la accion de devolverme
los inicios y fin de cuatrimestre"""
Prueba3.inicioYfinCuatrimestres()

"""Llamo al metodo para devolverme los feriados"""
Prueba3.feriados()

"""Imprimo ambos metodos para obtener los resultados
y saber sus repectivos valores"""
print(Prueba3.fechaInicioYfin)
print(Prueba3.FechasFeriadosDate)
