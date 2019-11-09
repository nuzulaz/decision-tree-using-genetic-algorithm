import random
# [p1[0]:p1[1]]

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
arrNew = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
	

