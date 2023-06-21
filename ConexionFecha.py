#Año - InicioPrimerCuatrimestre - FinPrimerCuatrimestre - InicioSegundoCuatrimestre - FinSegundoCuatrimestre
import sqlite3


class fechaCursadas:
    def __init__(self,conexion, Año, InicioPrimerCuatri, FinPrimerCuatri, InicioSegundoCuatri, FinSegundoCautri):
        self.conect = conexion
        self.conexion = sqlite3.connect(conexion)
        self.cursor = self.conexion.cursor()
        
        self.Año = Año
        self.InicioPrimerCuatri = InicioPrimerCuatri
        self.FinPrimerCuatri = FinPrimerCuatri
        self.InicioSegundoCuatri = InicioSegundoCuatri
        self.FinSegundoCuatri = FinSegundoCautri
        
    
    def caracteristicas(self):
        print(f"Fechas de inicio y fin durante el año {self.Año}")
        print(f"Inicio del primer cuatrimestre: {self.InicioPrimerCuatri}")
        print(f"Finalizacion del primer cuatrimestre: {self.FinPrimerCuatri}")
        print(f"Inicio del segundo cuatrimestre: {self.FinSegundoCuatri}")
        print(f"Finalizacion del segundo cuatrimestre: {self.FinSegundoCuatri}")
        
        
    def conectar(self):
        self.conexion = sqlite3.connect(self.conect)
        
        self.cursor = self.conexion.cursor()
        
        return self.conexion, self.cursor
    
    
    def ingresarDatos(self):
        self.conectar()
        
        comando = f"""INSERT INTO Fecha (Año, InicioPrimerCuatrimestre, FinPrimerCuatrimestre, InicioSegundoCuatrimestre, FinSegundoCuatrimestre)
        VALUES ({self.Año},'{self.InicioPrimerCuatri}','{self.FinPrimerCuatri}','{self.InicioSegundoCuatri}','{self.FinSegundoCuatri}') """
        
        self.cursor.execute(comando)
        self.conexion.commit()
        self.conexion.close()
        
        

conexion = "C:/Users/ofern/OneDrive/Escritorio/Proyecto Oucra/proyecto_oucra/base de datos/BDtrabajoUocra.db"

PruebaFechas = fechaCursadas(conexion,2022,"02-01-2023","14-06-2023","03-07-2023","21-12-2023")
        
            
PruebaFechas.ingresarDatos()    