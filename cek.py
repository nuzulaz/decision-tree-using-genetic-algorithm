import random
# [p1[0]:p1[1]]

arrNew = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
arr = [0,0,0,0,0,0,0,0,0,0,0,0]
x = random.randint(1,len(arr)-2)
y = random.randint(x,len(arr)-1)


if y-x > 5:
	z = arr[x:len(arr)]
	k = arrNew[x:y]
	arr[x:y] = k
	print(len(arr[0:y]))
	g = len(arr[0:y]) + len(z)
	q = g % 5
	print(g)
	while g % 5 != 0:
		g-=1	
	print(g,q)
	print((arr[0:y]))
	print(len(z),z)
	arr[y:len(arr)] = z[-(len(z)-q):]
	print(arr,len(arr))
else:
	pass
	



def cekFitnessKromosom(kromosom):
	dataUji = readTrainingData() 
	fit = 0
	tmp = 0
	count = 0
	listFitness = []
	cekStatus = kromosom
	s = cekStatus[0].split(",")
	w = cekStatus[1].split(",")
	l = cekStatus[2].split(",")
	k = cekStatus[3].split(",")
	status = cekStatus[4]
	for data in dataUji:
		for i in s:
			if i == data[0]:
				count += 1
				break
		for i in w:
			if i == data[1]:
				count += 1
				break
		for i in l:
			if i == data[2]:
				count += 1
				break
		for i in k:
			if i == data[3]:
				count += 1
				break
		if status == data[4]:
				count += 1
		if count == 5:
			fit += 1
		count = 0
	
	listFitness.append(fit)
	fit = 0

	return listFitness
([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1], 16)
([1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0], 20)
([1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0], 20)

# def crossOver(parent1,parent2):
# 	pass
# 	prx = []
# 	if len(parent1) == len(parent2):
# 		# tipot1a  = random.randint(1,len(parent1)-2)
# 		tipot1a = 2
# 		tipot1b = 20
# 		p1 = [tipot1a,tipot1b]
# 		pc1 = tipot1a % 15	
# 		pc2 = tipot1b % 15	
# 		# if pc2 > pc1:
# 		# 	arr = [[pc1,pc2],[pc1,tipot1b]]
# 		# 	if tipot1a >= pc2:
# 		# 		arr.append([pc2,tipot1a])
# 		# 	else:
# 		# 		arr.append([tipot1a,pc2])
# 		# elif pc2 < pc1:
# 		# 	arr = [[pc2,pc1],[pc1,tipot1b],[pc2,tipot1a]]
# 		# else:
# 		# 	arr = [[pc1,pc2],[pc1,tipot1b],[pc2,tipot1a]]
		
# 		arr = [[pc1,pc2],[pc1,15+pc2],[pc1+15,pc2+15]]
		
# 		p2 = random.choice(arr)
# 		print(arr)
# 		print(p1,p2)
# 		# ambilnilai tampungan parent 1
# 		tmpP1 = parent1[p1[0]:p1[1]]
# 		tmp1 = parent1[p1[1]:len(parent1)]
		
# 		# ambil nilai tampungan parent 2
# 		tmpP2 = parent2[p2[0]:p2[1]]
# 		tmp2 = parent2[p2[1]:len(parent2)]

# # 		persiapan pindah data dengan cara delete data parent sebelumnya
# 		del parent1[p1[0]:p1[1]]
# 		del parent2[p2[0]:p2[1]]

# # 		TUkar Data
# 		parent1[p2[0]:p2[1]] = tmpP2
# 		parent1[p2[1]:] = tmp1
# 		parent2[p1[0]:p1[1]] = tmpP1
# 		parent2[p1[1]:] = tmp2

# #		ambil nilai mod, untuk menyesuaikan dengan panjang rulenya
# 		fitGenRule1 = len(parent1) % 15
# 		fitGenRule2 = len(parent2) % 15

# #		penyesuaian panjang rule dengan gen 	
# 		print(fitGenRule1)
# 		print(fitGenRule2)

# 		print(parent1,len(parent1))
# 		print(parent2,len(parent2))

# 		print(tmpP1,tmpP2)

# if y-x > 5:
# 	z = arr[x:len(arr)]
# 	k = arrNew[x:y]
# 	arr[x:y] = k
# 	print(len(arr[0:y]))
# 	q = len(arr[0:y]) % 5
# 	if q != 0:
# 		print(q)
# 		print((arr[0:y]))
# 		print(z)
# 		arr[y:len(arr)] = z[-(5-q):]
# 	else:
# 		arr[y:len(arr)] = z

# 	print(arr,len(arr))
# else:
# 	pass
	

