# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:24:58 2021

@author: Luna_21
"""
import os
import math

dire=os.getcwd()

x=0.0
y=0.0
z=0.0

#convierte los archivos .AS en .o
"""for root, dirs, files in os.walk(dire):
    for archiv in files:
        if archiv.endswith(".AS"):
            os.system("teqc -O.dec 30 +obs {}.o {}".format(archiv.split("_")[0],archiv))"""

 

#imprime las coordenadas
for root, dirs, files in os.walk(dire):
    for archiv in files:
        if archiv.endswith(".o"):    
            with open(archiv) as f:
                lineas=f.readlines()[9:10]
            for lines in lineas:
                new_line=lines.strip().strip(" ")
                x=x+float(new_line[0:11])
                y=y+float(new_line[12:25])
                z=z+float(new_line[27:39])
                
X=x/31
Y=y/31
Z=z/31          
print(X,Y,Z)               

############################################
#Conversion de coordenadas
fors={'WGS 84':(6378137,6356752.314),'GRS80':(6378137,6356752.314),'CLARKE 1866':(6378206.4,6356583.8)}

print("Seleccione el elipsoide de transformación")
for nombre in fors.keys():
    print('\t {}'.format(nombre))

resp=input(">>>").upper()


    
def pexc(fors, resp):
  (a,b)=fors[resp]
  e=math.sqrt(((a**2)-(b**2))/(a**2))
  return e          
        
def segexc(fors,resp):
    (a,b)=fors[resp]
    e_prim=math.sqrt(((a**2)-(b**2))/(b**2))
    return e_prim
        
def pres(X,Y):   #El valor de p
            #(a,b)=fors[resp]
    x2=(X**2)
    y3=(Y**2)
    p=math.sqrt(x2+y3)
    return p
        
                        #def tetas(fors,resp,Z,X,Y):
                        #    (a,b)=fors[resp]
                        #    p=pres(X,Y)
                        #    teta=math.atan((Z*a)/(p*b))
                        #    return teta
    
def tetas(fors,resp,p,Z): #Originaaalll
    (a,b)=fors[resp]
    teta=math.atan((Z*a)/(p*b))
    return teta
        
def phil(fors,resp,tet,e1,Z):
    (a,b)=fors[resp]
    phi=math.atan((Z+(e2*b*pow(math.sin(tet),3)))/(p-e1*math.pow(math.cos(tet),3)))
    return phi
        

def ObtN(fors,resp,e1,phi):
    (a,b)=fors[resp]
    N=(a)/(math.sqrt(1-e1*math.sin(phi)))
    return N
        
def Obth(fors,resp,p,phi,N):
    (a,b)=fors[resp]
    h=(p/(math.cos(math.degrees(phi))))-N
    return h
        
def Landas(X,Y):
    l=math.atan(Y/X)
    return l
        
        
e1=pexc(fors,resp)
e2=segexc(fors,resp)
p=pres(X,Y)
tet=tetas(fors,resp,p,Z)
phi=phil(fors,resp,tet,e1,Z)
N=ObtN(fors,resp,e1,phi)
h=Obth(fors,resp,p,phi,N)
L=Landas(X,Y)



if resp in fors:
    print("Gracias escogiste",resp) 
    print("Coordenadas Geodesicas")
    print("φ =", math.degrees(phi))
    print("λ =",math.degrees(L))
    print("h =",h)
else: 
    print("Lo ingresado no está contenido en el programa")





