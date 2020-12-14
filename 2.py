import requests
import json
from datetime import date
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql import functions as F


spark = SparkSession.builder.appName('Ejercicio 2 Equipo cafe').getOrCreate()
sc = spark.sparkContext

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


def main():
	print("###################################")
	print("###          Servo1             ###")
	print("###################################")
	interruptores = getData()
	print("###################################")
	print("###         Minimo              ###")
	print("###################################")
	print("min: ", interruptores.select("gra").rdd.min()[0])
	print("###################################")
	print("###         Maximo              ###")
	print("###################################")
	print("max: ", interruptores.select("gra").rdd.max()[0])
	print("###################################")
	print("###         Promedio            ###")
	print("###################################")
	print(interruptores.select("gra").agg(F.avg(interruptores["gra"])).show())
	print("###################################")
	print("###          Servo2             ###")
	print("###################################")
	print("###################################")
	print("###         Minimo              ###")
	print("###################################")
	print("min: ", interruptores.select("grad").rdd.min()[0])
	print("###################################")
	print("###         Maximo              ###")
	print("###################################")
	print("max: ", interruptores.select("grad").rdd.max()[0])
	print("###################################")
	print("###         Promedio            ###")
	print("###################################")
	print(interruptores.select("grad").agg(F.avg(interruptores["grad"])).show())


if __name__ == '__main__':
	main()



