import sqlite3
from datetime import datetime, timedelta, date, time

class valoresBD:
    def __init__(self, conexion):
        self.conect = conexion
        self.conexion = sqlite3.connect(conexion)
        self.cursor = self.conexion.cursor()
        
        self.FechasFeriadosDate = None
    
    """Metodo para conectarme con la BD"""    
    def conectar(self):
        self.conexion = sqlite3.connect(self.conect)
        
        self.cursor = self.conexion.cursor()
        
        return self.conexion, self.cursor        
    
    """Metodo para devolver los valores 
    de inicio y fin de cuatrimestre
    consultar por inicios de curso a mitad
    de año que duran 1 año"""
    def inicioYfinCuatrimestres(self):
        self.conectar()

        self.cursor.execute("SELECT * FROM Fecha")
        
        resultados = self.cursor.fetchall()
        diccionario = {}

        for fila in resultados:
            Año = fila[0]
            diccionario[Año] = fila
        
        self.conexion.close()       
    
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
    
        
conexion = "C:/Users/ofern/OneDrive/Escritorio/Proyecto Oucra/proyecto_oucra/base de datos/BDtrabajoUocra.db"

Prueba3 = valoresBD(conexion)

Prueba3.feriados()