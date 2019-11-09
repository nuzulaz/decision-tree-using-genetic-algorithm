import math
import random
import csv
import itertools
from itertools import permutations   
from itertools import combinations 
import collections 

def readTrainingData():
    results = []
    with open("datatraining.txt") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(row)
    results.remove(results[0])
    return results

def setRangeKromosom():
	tmp = []
	arrKromosom = []
	for i in range(1,100):
		if i % 15 == 0:
			tmp.append(i)
	return tmp

def createChromosome(arr):
	ruleRange = random.choice(arr)
	arrKromosom = []
	for i in range(1,ruleRange+1):
		arrKromosom.append(random.randint(0,1))		
	print(len(arrKromosom))
	return arrKromosom
	
def createPopulation(N):
	population = []
	for i in range(1,N+1):
		population.append(createChromosome(setRangeKromosom()))
	return population

def splitRule(arrKromosom):
    for i in range(0, len(arrKromosom),15):
        yield arrKromosom[i:i+15]

def rSubset(arr, r): 
    return list(combinations(arr, r)) 

def decodeChromosome(chromosome):
	# rule = list(splitRule(chromosome))
	dataUji = readTrainingData()
	# for i in rule:
	suhu = chromosome[0:3]
	waktu = chromosome[3:7]
	langit = chromosome[7:11]
	lembap = chromosome[11:14]
	status = chromosome[14]
	cekSL = (list(itertools.product([1, 0], repeat=3)))
	cekWL = (list(itertools.product([1, 0], repeat=4)))
	x = 0
	for i in cekWL:
		print(x,i)
		x+=1
		

	if suhu == list(cekSL[0]):
		print("n t r")
	elif suhu == list(cekSL[1]):
		print("n t")
	elif suhu == list(cekSL[2]):
		print("t r")
	elif suhu == list(cekSL[3]):
		print("t")
	elif suhu == list(cekSL[4]):
		print("n r")
	elif suhu == list(cekSL[5]):
		print("n")
	elif suhu == list(cekSL[6]):
		print("r")

	

	if waktu == list(cekWL[0]):
		print("p si so m")
	elif waktu == list(cekWL[1]):
		print("p si so")
	elif waktu == list(cekWL[2]):
		print("p si m")
	elif waktu == list(cekWL[3]):
		print("p si")
	elif waktu == list(cekWL[4]):
		print("p so m")
	elif waktu == list(cekWL[5]):
		print("p so")
	elif waktu == list(cekWL[6]):
		print("p m")	
	elif waktu == list(cekWL[7]):
		print("p")
	elif waktu == list(cekWL[8]):
		print("si so m")
	elif waktu == list(cekWL[9]):
		print("si so")
	elif waktu == list(cekWL[10]):
		print("si m")
	elif waktu == list(cekWL[11]):
		print("si")
	elif waktu == list(cekSL[12]):
		print("so m")
	elif waktu == list(cekSL[13]):
		print("so")
	elif waktu == list(cekSL[14]):
		print("m")



	if lembap == list(cekSL[0]):
		print("n t r")
	elif lembap == list(cekSL[1]):
		print("n t")
	elif lembap == list(cekSL[2]):
		print("t r")
	elif lembap == list(cekSL[3]):
		print("t")
	elif lembap == list(cekSL[4]):
		print("n r")
	elif lembap == list(cekSL[5]):
		print("n")
	elif lembap == list(cekSL[6]):
		print("r")


	





krom = [0,1,1,0,0,0,1,0,1,0,1,0,1,0,0]
decodeChromosome(krom)

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
		x =p1[1]-p1[0]
		
		if (p2[1]-p2[0] > 5):
			while x % 5 != 0:
				print(x)
				x-+1


		arr = [[] for _ in range(len(anak2)+x)]
		print(arr,len(arr))
		pass

	else: #cuman 1 rule
		pass


# if __name__ == '__main__':
# 	listFitness = []
# 	population = createPopulation(10)
# 	print(population)
	# x = cekFitness(population)
	# idx = 0
	# for i in population:
	# 	print(i," = ",x[idx])
	# 	idx+=1

	# parent1 = rouletteWheels(listFitness)
	# parent2 = rouletteWheels(listFitness)
	# crossOver(parent1,parent2)

# print(createPopulation(10))
# splitRule()
def encodeTrainingData(training):	
	# data[0] = suhu, data[1] = waktu, data[2] = langit, data[3] = kelembapan, data[4] = terbang
	dataTrain = []
	for data in training:	
		suhu,waktu,langit,lembap,status = "","","","",""
		if (data[0] == "Rendah"):
			suhu = "001"		
		elif (data[0] == "Normal"):		
			suhu = "010"		
		elif (data[0] == "Tinggi"):		
			suhu = "100"

		if (data[1] == "Pagi"):
			waktu = "1000"		
		elif (data[1] == "Siang"):		
			waktu = "0100"		
		elif (data[1] == "Sore"):		
			waktu = "0010"	
		elif (data[1] == "Malam"):		
			waktu = "0001"

		if (data[2] == "Berawan"):
			langit = "1000"		
		elif (data[2] == "Cerah"):		
			langit = "0100"		
		elif (data[2] == "Hujan"):		
			langit = "0010"	
		elif (data[2] == "Rintik"):		
			langit = "0001"

		if (data[3] == "Rendah"):
			lembap = "001"		
		elif (data[3] == "Normal"):		
			lembap = "010"		
		elif (data[3] == "Tinggi"):		
			lembap = "100"

		if data[4] == "Ya":
			terbang = "1"
		else:
			terbang = "0"

		genTraining = suhu+waktu+langit+lembap+terbang
		dataTrain.append(genTraining)

	del dataTrain[0]
	return dataTrain


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
