import math
import random
import csv

import collections 

def readTrainingData():
    results = []
    with open("data_latih_opsi_2.txt") as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            row[0] = int(row[0])
            row[1] = int(row[1])
            row[2] = int(row[2])
            row[3] = int(row[3])
            row[4] = int(row[4])
            results.append(row)
            
    return results


def setRangeKromosom():
	tmp = []
	arrKromosom = []
	for i in range(1,50):
		if i % 5 == 0:
			tmp.append(i)
	return tmp

def createChromosome(arr):
	ruleRange = random.choice(arr)
	arrKromosom = []
	for i in range(1,ruleRange+1):
		if i % 5 == 0:
			arrKromosom.append(random.randint(0,2))
			arrKromosom.append(random.randint(0,3))
			arrKromosom.append(random.randint(0,3))
			arrKromosom.append(random.randint(0,2))
			arrKromosom.append(random.randint(0,1))
	return arrKromosom
	
def createPopulation(N):
	population = []
	for i in range(1,N+1):
		population.append(createChromosome(setRangeKromosom()))
	return population


def splitRule(arrKromosom):
    for i in range(0, len(arrKromosom),5):
        yield arrKromosom[i:i+5]

def cekFitness(population):
	dataUji = readTrainingData() 
	fit = 0
	for i in range(0,len(population)):
		rule = list(splitRule(population[i]))
		for dataValid in rule:
			for data in dataUji:
				if len(data)== len(dataValid) and len(data) == sum([1 for k, l in zip(data, dataValid) if k == l]): 
					fit+=1
				else: 
					pass
		listFitness.append((fit/80)*0.01)
		fit = 0

	return listFitness

def rouletteWheels(Fitness):
	sumFitness = sum(Fitness)
	print(sumFitness)
	countFitness = 0
	randomNumber = random.random()

	idx = 0
	for i in population:
		countFitness += Fitness[idx]
		if countFitness/sumFitness > randomNumber:
			return i,listFitness[idx]
			break
		idx+=1


listFitness = []
population = createPopulation(10)
x = cekFitness(population)
idx = 0
for i in population:
	print(i," = ",x[idx])
	idx+=1

print(rouletteWheels(listFitness))
# print(createPopulation(10))
# splitRule()
# def encodeTrainingData(training):	
# 	# data[0] = suhu, data[1] = waktu, data[2] = langit, data[3] = kelembapan, data[4] = terbang
# 	dataTrain = []
# 	for data in training:	
# 		suhu,waktu,langit,lembap,status = "","","","",""
# 		if (data[0] == "Rendah"):
# 			suhu = "001"		
# 		elif (data[0] == "Normal"):		
# 			suhu = "010"		
# 		elif (data[0] == "Tinggi"):		
# 			suhu = "100"

# 		if (data[1] == "Pagi"):
# 			waktu = "1000"		
# 		elif (data[1] == "Siang"):		
# 			waktu = "0100"		
# 		elif (data[1] == "Sore"):		
# 			waktu = "0010"	
# 		elif (data[1] == "Malam"):		
# 			waktu = "0001"

# 		if (data[2] == "Berawan"):
# 			langit = "1000"		
# 		elif (data[2] == "Cerah"):		
# 			langit = "0100"		
# 		elif (data[2] == "Hujan"):		
# 			langit = "0010"	
# 		elif (data[2] == "Rintik"):		
# 			langit = "0001"

# 		if (data[3] == "Rendah"):
# 			lembap = "001"		
# 		elif (data[3] == "Normal"):		
# 			lembap = "010"		
# 		elif (data[3] == "Tinggi"):		
# 			lembap = "100"

# 		if data[4] == "Ya":
# 			terbang = "1"
# 		else:
# 			terbang = "0"

# 		genTraining = suhu+waktu+langit+lembap+terbang
# 		dataTrain.append(genTraining)

# 	del dataTrain[0]
# 	return dataTrain


# def getFitness(x1,x2):
# 	h = (((4-2.1*1*(pow(x1,2)))+(pow(x1,4))/3)*pow(x1,2))+x1*x2+(((-4)+4*pow(x2,2)))*pow(x2,2)
# 	return 1/(h+1.5)

# def cekNilai(x1,x2):
# 	return (((4-2.1*1*(pow(x1,2)))+(pow(x1,4))/3)*pow(x1,2))+x1*x2+(((-4)+4*pow(x2,2)))*pow(x2,2)

# def bestFitness(population):
# 	max = 0
# 	idx = -1
# 	for i in population:
# 		x1 = decodeChromosome(-3,3,i,0,8)
# 		x2 = decodeChromosome(-2,2,i,8,16)
# 		cek = getFitness(x1,x2)
# 		if cek>max:
# 			max = cek
# 			idx = i
# 	return max,idx


# def mate(parent1,parent2):
# 	cp = random.randint(1,8)
# 	child1 = []
# 	child2 = []
# 	for i in range(0,cp):
# 		child1.append(parent1[i])
# 		child2.append(parent2[i])
# 	for i in range(cp,16):
# 		child1.append(parent2[i])
# 		child2.append(parent1[i])

# 	child = [child1,child2]
# 	return child

# def mutate(child):
# 	for i in range(0,len(child)):
# 		prob = random.random()
# 		if prob<0.5:
# 			child[i] = random.randint(0,9)
# 	return child

# def elitism(population):
# 	bestLokal = []
# 	bestLokal = bestFitness(population)
# 	return bestLokal


# #WORK 
# population,child= [],[]
# population = createPopulation(16,10)
# generasi = 1
# variansiFitnes = 0
# stagnantCek = [True,0,0]
# while (generasi <= 10000) and (stagnantCek[0]):
# 	newPop = []
# 	for i in range(0,4):
# 		parent1 = rouletteWheels(population)
# 		parent2 = rouletteWheels(population)
# 		child = mate(parent1,parent2)
# 		for gen in child:
# 			gen = mutate(gen)
# 			newPop.append(gen)
	
# 	bestLokal = elitism(population)
# 	newPop.append(bestLokal[1])
# 	population = newPop

# 	if stagnantCek[1] == bestLokal[0]:
# 		stagnantCek[2]+=1
# 		if stagnantCek[2] >= 500:
# 			stagnantCek[0] = False
# 	else:
# 		stagnantCek[1] = bestLokal[0]
# 		stagnantCek[2] = 0
# 		variansiFitnes += 1

# 	generasi+=1


# x1 = decodeChromosome(-3,3,bestLokal[1],0,8)
# x2 = decodeChromosome(-2,2,bestLokal[1],8,16)
# print("Nilai Terkecil : ",cekNilai(x1,x2))
# print("Fenotype :",x1,x2)
# print("Gen :",bestLokal[1])
# print("Fitness :,",bestLokal[0])
# print("Variansi Fitness :",variansiFitnes)
# print("Total Generasi :",generasi)
