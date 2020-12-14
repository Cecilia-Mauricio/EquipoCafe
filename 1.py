import requests
import json
from dateutil import parser
import statistics as stats
from datetime import date
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql import functions as F



spark = SparkSession.builder.appName('Ejercicio 1 Equipo cafe').getOrCreate()
sc = spark.sparkContext
fecha_inicial = False
fecha_final = False 

def getDate(msj):
	print(msj)
	dateInput=(raw_input("Ingresa la fecha con el siguiente formato (YYYY-MM-DD): "))
	Fecha = False
	try:
		fecha=datetime.strptime(dateInput,"%Y-%m-%d")
	except Exception as e:
		print("Algo salio mal, ingresaste valores correctos?. Error: ",e)
	return  fecha

def validateDate(f_i,f_f):
	if f_i>f_f:
		print("La fehca incial no puede ser mayor que la fecha final")
		return False
	else:
		return True

def getData():
	url = "http://144.202.34.148:3340/interruptores"
	response = requests.get(url)
	data = response.text
	json_rdd = spark.sparkContext.parallelize([response.text])
	parsed = json.loads(data)
	return spark.read.json(json_rdd)


def lista(x,L):
	if L:
		L.append(x)
	return L

def getFech(fech):
        fechas = parser.parse(fech).strftime('%Y-%m-%d')
        return fecha_inicial <= fechas <= fecha_final

def main():
	global fecha_inicial
	global fecha_final
	#run = True
	interruptores = getData()
	fecha_inicial = getDate("Fecha incial:\n")
	fecha_final = getDate("Fecha final:\n")
	while run:
		if(validateDate(fecha_inicial,fecha_final)):
			print("###################################")
			print("###         Minimo              ###")
			print("###################################")
			print("min: ", interruptores.select("gra").filter(getFech(interruptores["fecha"]).rdd.min()[0])
			print("###################################")
			print("###         Maximo              ###")
			print("###################################")
			print("max: ", interruptores.select("gra").filter(getFech(interruptores["fecha"]).rdd.max()[0])
			print("###################################")
			print("###         Promedio            ###")
			print("###################################")
			print(interruptores.select("gra").filter(getFech(interruptores["fecha"]).agg(F.avg(interruptores["gra"])).show())
		run=False


if __name__ == '__main__':
	main()

