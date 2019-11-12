import math
import random
import csv

import collections 

def readTrainingData():
    results = []
    with open("data_latih_opsi_2.txt") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
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
				if len(data) == len(dataValid) and len(data) == sum([1 for k, l in zip(data, dataValid) if k == l]): 
					fit+=1
				else: 
					pass
		listFitness.append((fit/80)*0.01)
		fit = 0

	return listFitness

def rouletteWheels(Fitness):
	sumFitness = sum(Fitness)
	countFitness = 0
	randomNumber = random.random()
	idx = 0
	for i in population:
		countFitness += Fitness[idx]
		if countFitness/sumFitness > randomNumber:
			return i
			break
		idx+=1

def crossOver(parent1,parent2):
	prx = []
	if len(parent1) >= len(parent2):
		prx = parent2
		anak1 = parent1
		anak2 = parent2
	else:
		prx = parent1
		anak1 = parent2
		anak2 = parent1		
	
	print("===")
	print(parent1,len(parent1))
	print(parent2,len(parent2))
	print("===")

	tipot1a  = random.randint(1,len(prx)-2)
	tipot1b = random.randint(tipot1a+1,len(prx)-1)
	p1 = [tipot1a,tipot1b]
	jmlgen = p1[1]-p1[0]
	gap = jmlgen % 5
	pc1,pc2,pc3,pc4 = [tipot1a,tipot1a+jmlgen],[tipot1a,tipot1a+gap],[tipot1b-jmlgen,tipot1b],[tipot1b-gap,tipot1b]
	
	if pc1 == pc2 == pc3 == pc4:
		arrProb = [pc1]
	else:
		arrProb = [pc1,pc2,pc3,pc4]

	p2 = random.choice(arrProb)
	print(p1,p2)
	print(p2[1]-p2[0])
	print(p2[0] % 5)

	if p1 == p2:
		tmp = anak1[p1[0]:p1[1]]
		anak1[p1[0]:p1[1]] = anak2[p1[0]:p1[1]]
		anak2[p1[0]:p1[1]] = tmp

	elif((p2[0] % 5 == 0) or ((p2[0] % 5 != 0) and (p2[1]-p2[0] > 2))): 	#rule lebih dari 1				
		arr = [[] for _ in range(len(anak2)+5)]
		print(arr,len(arr))
		pass

	else: #cuman 1 rule
		pass


if __name__ == '__main__':
	listFitness = []
	population = createPopulation(10)
	x = cekFitness(population)
	idx = 0
	for i in population:
		print(i," = ",x[idx])
	# 	idx+=1

	# parent1 = rouletteWheels(listFitness)
	# parent2 = rouletteWheels(listFitness)
	# crossOver(parent1,parent2)

# print(createPopulation(10))
# splitRule()

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
