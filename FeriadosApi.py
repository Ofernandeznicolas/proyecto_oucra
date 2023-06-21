import requests
from datetime import datetime, timedelta, date, time


class datosApi:
    def __init__(self, año):
        self.año = año
        self.resultado = None
        self.resultadoConFechas = None
        self.fechasFeriadoSTR = None
        self.fechasFeriadosDATE = None
        self.feriadosParaBD = None
    
    """ Traigo los resultados de la API"""
    def resultadosApi(self):
        año = self.año
        
        url = f"http://nolaborables.com.ar/api/v2/feriados/{año}"
        
        respuesta = requests.get(url)
        resultados = respuesta.json()
        self.resultado = resultados
        
        return self.resultado
    
    """Agrego la fecha completa a cada diccionario 
       para utilizarla en otras funciones (BD - Calculadora)"""
    def añadirFechasResultado(self): 
        
        """En todas los metodos agrego un if 
        para que si mi atributo no tenga valor ejecute
        su metodo correspondiente"""
        
        if self.resultado == None:
            self.resultadosApi()
        
        resultadoConFechas = self.resultado
        
        año = str(self.año)
        
        for dias in resultadoConFechas:
            dias["FechaFeriado"]=dias["dia"]+dias["mes"]+self.año
            dias["FechaFeriado"]=f'{dias["dia"]}-{dias["mes"]}-{año}'
            self.resultadoConFechas = resultadoConFechas
        
        return self.resultadoConFechas    
    
    """Metodo para almacenar las fechas en formato STR"""
    def feriadosFechasSTR(self):  
        if self.resultadoConFechas == None:
            self.añadirFechasResultado()
        
        fechasFeriados = []
        
        for fechas in self.resultadoConFechas:
            fechasFeriados.append(fechas["fecha"])
        
        self.fechasFeriadoSTR = fechasFeriados
        return self.fechasFeriadoSTR
              
    
    """Metodo para almacenar las fechas en formato DATE"""
    def feriadosFechasDATE(self): #
        if self.fechasFeriadoSTR == None:
            self.feriadosFechasSTR()
        
        fechasFeriadosDATE = []
        
        for i in self.fechasFeriadoSTR:
            fecha = i
            fecha = datetime.strptime(fecha, "%d-%m-%Y").date()
            fechasFeriadosDATE.append(fecha)
            
        self.fechasFeriadosDATE = fechasFeriadosDATE
    
    """Metodo para almacenar y transformar cada fecha 
    con su dia correspondiente"""
    def nombreDia(self):
        if self.resultadoConFechas == None:
            self.añadirFechasResultado()
        
        
        for i in self.resultadoConFechas:
            
            fecha = i["FechaFeriado"]
            fecha = datetime.strptime(fecha, "%d-%m-%Y")
            if fecha.weekday() == 0:
                i["DiaFeriado"] = "Lunes"
            elif fecha.weekday() == 1:
                i["DiaFeriado"] = "Martes"
            elif fecha.weekday() == 2:
                i["DiaFeriado"] = "Miercoles"
            elif fecha.weekday() == 3:
                i["DiaFeriado"] = "Jueves"
            elif fecha.weekday() == 4:
                i["DiaFeriado"] = "Viernes"
            elif fecha.weekday() == 5:
                i["DiaFeriado"] = "Sabado"
            elif fecha.weekday() == 6:
                i["DiaFeriado"] = "Domingo"

        return self.resultadoConFechas
    
    """Metodo para Almacenar los datos 
    y cargarlos en la BD de feriados."""    
    def feriadosBD(self): 
        if self.resultadoConFechas == None:
            self.añadirFechasResultado()
        
        if "DiaFeriado" not in self.resultadoConFechas:
            self.nombreDia() 
            
        feriadosParaBD = self.resultadoConFechas
        
        caracterizticasEliminar = ["id","dia","mes","info","original"]
        
        """A traves de un for modifico los nombres 
        para que sean los mismos que mi base de datos
        y elimino los elementos que no me interesan"""
        for dias in feriadosParaBD: 
            
            variableMomentanea = dias["motivo"] 
            dias["MotivoFeriado"] = variableMomentanea
            del dias["motivo"]
            
            variableMomentanea = dias["tipo"] 
            dias["TipoFeriado"] = variableMomentanea
            del dias ["tipo"]
            
            for caracteriztica in caracterizticasEliminar:
                dias.pop(caracteriztica, None)
        
        
        self.feriadosParaBD = feriadosParaBD            
                    
        return self.feriadosParaBD
    

