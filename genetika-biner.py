import math
import random
import csv
import itertools
from itertools import permutations   
from itertools import combinations 
from tqdm import tqdm
import collections

def readTrainingData():
    results = []
    with open("data_latih_opsi_1.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(row)
    results.remove(results[0])
    return results

def setRangeKromosom():
	tmp = []
	arrKromosom = []
	for i in range(1,75):
		if i % 15 == 0:
			tmp.append(i)
	return tmp

def createChromosome(arr):
	ruleRange = random.choice(arr)
	arrKromosom = []
	for i in range(1,ruleRange+1):
		arrKromosom.append(random.randint(0,1))	
	return arrKromosom
	
def createPopulation(N):
	population = []
	for i in range(1,N+1):
		population.append(createChromosome(setRangeKromosom()))
	return population

def splitRule(arrKromosom):
    for i in range(0, len(arrKromosom),15):
        yield arrKromosom[i:i+15] 

def decodeChromosome(chromosome):
	tmp = []
	suhu = chromosome[0:3]
	waktu = chromosome[3:7]
	langit = chromosome[7:11]
	lembap = chromosome[11:14]
	status = chromosome[14]
	cekSL = (list(itertools.product([1, 0], repeat=3)))
	cekWL = (list(itertools.product([1, 0], repeat=4)))
	# print(suhu,waktu,langit,lembap,status)
	if ((suhu == [1,1,1] and waktu == [1,1,1,1] and langit == [1,1,1,1] and lembap == [1,1,1]) or ((suhu == [0,0,0] or waktu == [0,0,0,0] or langit ==[0,0,0,0] or lembap == [0,0,0]))):
		tmp.append("S")
		tmp.append("S")
		tmp.append("S")
		tmp.append("S")
		tmp.append("S")
	else:
		if suhu == list(cekSL[0]):
			tmp.append("normal,tinggi,rendah")
		elif suhu == list(cekSL[1]):
			tmp.append("normal,tinggi")
		elif suhu == list(cekSL[2]):
			tmp.append("tinggi,rendah")
		elif suhu == list(cekSL[3]):
			tmp.append("tinggi")
		elif suhu == list(cekSL[4]):
			tmp.append("normal,rendah")
		elif suhu == list(cekSL[5]):
			tmp.append("normal")
		elif suhu == list(cekSL[6]):
			tmp.append("rendah")
		elif suhu == list(cekSL[7]):
			tmp.append("rendah")

		if waktu == list(cekWL[0]):
			tmp.append("pagi,siang,sore,malam")
		elif waktu == list(cekWL[1]):
			tmp.append("pagi,siang,sore")
		elif waktu == list(cekWL[2]):
			tmp.append("pagi,siang,malam")
		elif waktu == list(cekWL[3]):
			tmp.append("pagi,siang")
		elif waktu == list(cekWL[4]):
			tmp.append("pagi,sore,malam")
		elif waktu == list(cekWL[5]):
			tmp.append("pagi,sore")
		elif waktu == list(cekWL[6]):
			tmp.append("pagi,malam")	
		elif waktu == list(cekWL[7]):
			tmp.append("pagi")
		elif waktu == list(cekWL[8]):
			tmp.append("siang,sore,malam")
		elif waktu == list(cekWL[9]):
			tmp.append("siang,sore")
		elif waktu == list(cekWL[10]):
			tmp.append("siang,malam")
		elif waktu == list(cekWL[11]):
			tmp.append("siang")
		elif waktu == list(cekWL[12]):
			tmp.append("sore,malam")
		elif waktu == list(cekWL[13]):
			tmp.append("sore")
		elif waktu == list(cekWL[14]):
			tmp.append("malam")
		elif waktu == list(cekWL[15]):
			tmp.append("pagi")		

		if langit == list(cekWL[0]):
			tmp.append("berawan,cerah,hujan,rintik")
		elif langit == list(cekWL[1]):
			tmp.append("berawan,cerah,hujan")
		elif langit == list(cekWL[2]):
			tmp.append("berawan,cerah,rintik")
		elif langit == list(cekWL[3]):
			tmp.append("berawan,cerah")
		elif langit == list(cekWL[4]):
			tmp.append("berawan,hujan,rintik")
		elif langit == list(cekWL[5]):
			tmp.append("berawan,hujan")
		elif langit == list(cekWL[6]):
			tmp.append("berawan,rintik")	
		elif langit == list(cekWL[7]):
			tmp.append("berawan")
		elif langit == list(cekWL[8]):
			tmp.append("cerah,hujan,rintik")
		elif langit == list(cekWL[9]):
			tmp.append("cerah,hujan")
		elif langit == list(cekWL[10]):
			tmp.append("cerah,rintik")
		elif langit == list(cekWL[11]):
			tmp.append("cerah")
		elif langit == list(cekWL[12]):
			tmp.append("hujan,rintik")
		elif langit == list(cekWL[13]):
			tmp.append("hujan")
		elif langit == list(cekWL[14]):
			tmp.append("rintik")
		elif langit == list(cekWL[15]):
			tmp.append("berawan")

		if lembap == list(cekSL[0]):
			tmp.append("normal,tinggi,rendah")
		elif lembap == list(cekSL[1]):
			tmp.append("normal,tinggi")
		elif lembap == list(cekSL[2]):
			tmp.append("tinggi,rendah")
		elif lembap == list(cekSL[3]):
			tmp.append("tinggi")
		elif lembap == list(cekSL[4]):
			tmp.append("normal,rendah")
		elif lembap == list(cekSL[5]):
			tmp.append("normal")
		elif lembap == list(cekSL[6]):
			tmp.append("rendah")
		elif lembap == list(cekSL[7]):
			tmp.append("rendah")

		if (status == 1):
			tmp.append("ya")
		else:
			tmp.append("tidak")

	# print(tmp,chromosome)
	return tmp

def cekFitness(population,dataUji):
	tmp = 0
	count = 0
	listFitness = []
	for kromosom in population:
		dataRule =  list(splitRule(kromosom))
		fit = 0
		for data in dataUji:
			for drule in dataRule:
				cekStatus = decodeChromosome(drule)
				sh,wk,ln,kl,sts = False,False,False,False,False
				s = cekStatus[0].split(",")
				w = cekStatus[1].split(",")
				l = cekStatus[2].split(",")
				k = cekStatus[3].split(",")		
				status = cekStatus[4]
				
				if data[0] in s:
					sh = True
				if data[1] in w:
					wk = True
				if data[2] in l:
					ln = True
				if data[3] in k:
					kl = True
				if status == data[4]:
					sts = True
				 
				if sh and wk and ln and kl and sts:
					fit += 1
					break

		fitness = fit/80
		listFitness.append(fitness)
	return listFitness

def rouletteWheels(FitnessPopulasi):
	count = 0
	totalSemuaFitness = sum(FitnessPopulasi)
	randomNumber = random.random()
	idx = 0
	for individu in population:
		count += FitnessPopulasi[idx]
		if count/totalSemuaFitness > randomNumber:
			return individu
			break
		idx+=1

def crossOverNew(parent1,parent2):
	arr = []
	jumlahAturan = len(parent2) // 15
	for x in range(0,len(parent2)):
		if len(arr)==0:
			tipot1a  = random.randint(1,len(parent1)-2)
			tipot1b = random.randint(tipot1a+1,len(parent1)-1)
			tp1 = [tipot1a,tipot1b]
			pc1 = tipot1a % 15	
			pc2 = tipot1b % 15	
			for i in range(jumlahAturan):
				for j in range(i,jumlahAturan):
					x = i *15 + pc1		
					y = j *15 + pc2
					if (x > y):
						break
					arr.append([x,y])
		else:
			break
			
	tp2 = random.choice(arr)
	anak1 = (parent1[:tp1[0]]+parent2[tp2[0]:tp2[1]]+parent1[tp1[1]:])
	anak2 = (parent2[:tp2[0]]+parent1[tp1[0]:tp1[1]]+parent2[tp2[1]:])
	anak = [anak1,anak2]
	return anak

def mutate(child):
	for i in range(0,len(child)):
		prob = random.random()
		if prob<0.8:
			child[i] = random.randint(0,1)
	return child

def fitnessTerbaik(listFitness):
	x = max(listFitness)
	for i in range(len(listFitness)):
		if (listFitness[i]==x):
			return i

def readDataUji():
    results = []
    with open("data_uji_opsi_1.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tmp=[]
            for i in row:
            	tmp.append(i.lower())
            results.append(tmp)
    return results

def elitism(listFitness):
	bestLokal = fitnessTerbaik(listFitness)
	return bestLokal

def hasilTxt(decodeFix,dataUji):
	listHasil=[]
	print(dataUji)
	for data in dataUji:
		count = 0
		for rule in decodeFix:
			sh,wk,ln,kl,sts = False,False,False,False,False
			s = rule[0].split(",")
			w = rule[1].split(",")
			l = rule[2].split(",")
			k = rule[3].split(",")		
			
			print(s,w,l,k)			
			if data[0] in s:
				sh = True
			if data[1] in w:
				wk = True
			if data[2] in l:
				ln = True
			if data[3] in k:
				kl = True
			 
			if sh and wk and ln and kl:
				count += 1 
				listHasil.append(rule[4])
				break
		
		if count == 0:
			print("q")
			listHasil.append("ya")

	return listHasil
			
def tulisData(listHasil):
	f = open("hasil.txt","w+")
	for i in range(20):
		f.write(listHasil[i]+"\r\n")
	f.close()
    


if __name__ == '__main__':
	dataUji = readTrainingData() 
	listFitness = []
	population = createPopulation(20)
	listFitness = cekFitness(population,dataUji)
	generasi = 0
	idx = 0

	print("==============================================")


	for i in tqdm(range(100)):
		
		newPop,newFit = [],[]
		for i in (range(0,10)):
			parent1 = rouletteWheels(listFitness)
			parent2 = rouletteWheels(listFitness)
			anak = crossOverNew(parent1,parent2)
# 			================================ 	
			for gen in anak:
				gen = mutate(gen)
				newPop.append(gen)
			
			newFit = cekFitness(newPop,dataUji)
			# for i in newPop:
			# 	print(i,newFit[idx])
			# 	idx+=1
# 			=================================
			bestLokal = elitism(listFitness)
			newFit.append(listFitness[bestLokal])
			newPop.append(population[bestLokal])
			population = newPop
			listFitness = newFit
			
		if (listFitness[bestLokal] == 1) or (len(population[bestLokal])/15 >= 50):
			print(listFitness[bestLokal])
			break

	z = readDataUji()
	idxBest = fitnessTerbaik(listFitness)
	ruleKrom = list(splitRule(population[idxBest]))
	decodeBest,decodeFix = [],[]

	for rule in ruleKrom:
		decodeBest.append(decodeChromosome(rule))


	for i in decodeBest:
		if i != ['S','S','S','S','S']:
			decodeFix.append(i)


	print("Kromosom Terbaik : ",population[idxBest])
	print("Fitness : ",listFitness[idxBest])
	print("Rule : ",decodeFix)

	print("=====")
	print(z)

	tulisData(hasilTxt(decodeFix,z))














