'''
Function to determine if a number is a Gaussian Prime

'''
from math import sqrt
from math import ceil


def chi(x):
	if(x % 4 == 1):
		# not Gaussian Prime
		return 1 
	elif(x % 4 == 3):
		# is Gaussian Prime
		return -1
	else:
		# is even 
		return 0

def factors_freq(x):	
	factor = 2 			# start at 2
	cnt = 0 			# count of that factor
	fact_freq = []		# declare list
	while(x > 1):			# while x is greater than 1
		if(x % factor == 0):
		# x is divisible by factor
			cnt += 1	 	# increase that factor's count
			x /= factor  	# adjust x
		else:
		# x is not / no longer divisible by factor
			if cnt > 0:
				# we have some count of that factor
				fact_freq.append((factor, cnt)) #add to list as tuple
			
			cnt = 0		# reset frequency count 
			factor += 1		# check the next number
	if cnt > 0:
		# we have some count of that final factor to append as tuple
		fact_freq.append((factor, cnt))

	return fact_freq 

def num_gridpoints(radius):
	# find the number of grid points intersected by a circle
	# with some given radius
	fact_freq = factors_freq(radius ** 2)
	num_gp = 1		
	for (factor, count) in fact_freq:
		# add the chi function of each of its factors:
		factor_sum = 0
		for i in range(count + 1): 
			factor_sum += chi(factor ** i)
		num_gp *= factor_sum

	return 4 * num_gp


def is_hypotenuse(x):
	if (x == 0):
		return False
	# x could be a hyp if the circle made by radius x
	# intersects more than the 4 axis grid points
	if(num_gridpoints(x) > 4):
		return True
	else:
		return False



def get_triples(c):
	# list of triples to return
	triples = []

	start = ceil(c / sqrt(2))
	end = c
	for a in range(start,end):
		b = sqrt(c ** 2 - a ** 2)
		if (b).is_integer():
			triples.append((a, int(b)))

	return triples



def has_Ptriple(inputList):
	
	trip = []
	for n in inputList:
		if(is_hypotenuse(n)):
			# n is a hypotenuse; find its triples
			trip.extend(get_triples(n))
	
	if len(trip) == 0:
		return False

	# list has some hypotenuses-> check if the full triple is there
	input_hash = dict.fromkeys(inputList, 0)
	
	for (a, b) in trip:
		if a in input_hash.keys() and b in input_hash.keys():
			return True

	return False



inputList = [5,6,12,98,670,1001,800,600]
print(has_Ptriple(inputList))

