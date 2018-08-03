from pylab import *
from numpy import *
renglon=[]
archivo=open('tank-layout-03')
for i in range (300):
	linea=archivo.readline()
	renglon=linea.split()
	numero=int(renglon[1])
	x=float(renglon[2])
	y=float(renglon[3])
	z=float(renglon[4])
	print(x,y,z)

