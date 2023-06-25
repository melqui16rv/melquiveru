class Cargo:
    def __init__ (self,COUC,tiempo,contrato,lugar,vacantes,postulante,fecha,cierre):
        self.__COUC=COUC
        self.__tiempo=tiempo
        self.__contrato=contrato
        self.__lugar=lugar
        self.__vacantes=vacantes
        self.__postulante=postulante
        self.__fecha=fecha
        self.__cierre=cierre
        COUC=[]
    def setTiempo(self,tiempo):
        self.__tiempo=tiempo
    def getTiempo(self):
        return self.__tiempo
    def setContrato(self,contrato):
        self.__contrato=contrato
    def getContrato(self):
        return self.__contrato
    def setLugar(self,lugar):
        self.__lugar=lugar
    def getLugar(self):
        return self.__lugar
    def setVacante(self,vacantes):
        self.__vacantes=vacantes
    def getVacante(self):
        return self.__vacantes
    def setPostulante(self,postulante): 
        self.__postulante=postulante
    def getPostulante(self):
        return self.__postulante
    def setFecha(self,fecha):
        self.__fecha=fecha
    def getFecha(self):
        return self.__fecha
    def setCierre(self,cierre):
        self.__cierre=cierre
    def getCierre(self):
        return self.__cierre
    
    
    def Tiempo(self):
        TiempoExperiencia=int(input("digite cuantos años de experiencia tiene"))
        return TiempoExperiencia
      
    def Tcontrato(self,contrato):
        c=input("digite el cargo al que quiere aplicar")
        if c in contrato:
            print("cuantos años de experiencia a tenido con ese cargo")
            ca=input()
        else:
            print("ese cargo alegido ya esta ocupado")
    def Lugar(self):
        l=["soacha","cauca","boyaca","manizales","arauca"]
        lugar=input("que hubicacion desea buscar")
        if l in lugar:
            print("continue con su postulacion")
        else:
            print("ese hubicacion no esta disponible")
    def menu(self):
        while True:
            print("1.Ingrese la experiencia laboral")
            print("2.Ingrese el tipo de contrato a aplicar")
            print("3.Elija un lugar donde desea trabajar")
            print("4.Salir")
        
            eleccion= input("digite su eleccion:")  
           
            if eleccion == "1":
                TiempoExperiencia
            elif eleccion =="2":
            
            elif eleccion =="3":
                
            elif eleccion =="4":
                break
            else:
                print ("la seleccion marcada no corresponde intentelo de nuevo")
    


