from encodings.punycode import selective_find

__author__ = 'jor'
import re
class Clien:
    nombre=""
    apellido=""
    dni=""
    quenta=""
    maill=""
    telef=""
    sexo=""
    def __init__(self,nombre,apellido,dni,telef,sexo="H",quenta="",maill=""):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.quenta=quenta
        self.maill=maill
        self.telef=telef
        self.sexo=sexo
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getDni(self):
        return self.dni
    def getQuenta(self,dni,contact):
        misatge="el parametro de"
        if self.dni == dni:

            if re.search(self.maill,contact) or re.search(self.telef,contact):
                  return self.quenta
            else:
             misatge+=" recuperacion no es correcto."
        else:
               misatge+="el dni es incorrect."
        return  misatge

    def getMaill(self):
        return self.maill
    def getTelef(self):
        return self.telef
    def getSexo(self):
        return self.sexo

    def setTelef(self):
       if self.telef==input("insrte el telefono antiguo"):

           self.telef=input("insrte el nuebo numero de telefono")
           return "canbio realizado telefono actual : "+self.telef
       else:
            return "no se realizo ningun cambio, telefono antigui inbalido"

    def setMaill(self):
       if self.maill==input("insrte el maill antiguo"):

           self.maill=input("insrte el nuevo maill")
           return "canbio realizado maill actual : "+self.maill
       else:
            return "no se realizo ningun cambio, maill antigui inbalido"

    def setQuenta(self,dni):
        misatge="el parametro de"
        if self.dni == dni:
            contact=input("referencia de la persona (telefono o meil):")
            if re.search(self.maill,contact) or re.search(self.telef,contact):
                 oll =input("inserte quenta antugua:")
                 misatge+="quenta "
                 if re.search(self.quenta,oll):
                     self.quenta=input("inserte nuewa cuenta: ")
                     misatge+=" actualitzada "
                 else:
                     misatge+=" quenta invalida"
            else:
             misatge+=" recuperacion no es correcto."
        else:
               misatge+="el dni es incorrect."
        return  misatge