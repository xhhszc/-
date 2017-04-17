import math
class HORSE:
	
	def __init__(self):
		self.__Attributes=dict()
		for i in range(28):
			self.__Attributes[i]=[]
	def setIthAttribute(self,i,value):
		self.__Attributes[i].append(value)
	def getIthAtribute(self,i):
		return self.__Attributes[i][0]
	def printHorse(self):
		string=""
		for i in range(28):
			if i==0:
				string=self.__Attributes[i][0]
			else:
				string=string+' '+self.__Attributes[i][0]
		print string

def hammingDist(x,y):
	if len(x) != len(y):
		return 1000
	count=0
	for i in range(len(x)):
		if x[i] != y[i]:
			count=count+1
	return count


if __name__ == "__main__":
	continuous= {4,5,6,16,19,20,22}
	attribute368={2,24,25,26,27,28}
	#read file and load data to horses
	f=open('horse-colic.txt','r')
	horses=[]
	# line=f.readline()
	for line in f:
		horse=HORSE()
		line=line.strip('\n')
		line=line.strip('\r')
		attribute=line.split(' ')
		for i in range(28):
			horse.setIthAttribute(i,attribute[i])
		#horse.printHorse()
		horses.append(horse)
	f.close()

	f=open('horse-colic-fillWithSimilarity.txt','w')
	for H in range(len(horses)):
		#find the top-1 nearest horses
		dist=dict()
		#get the distance for all sample except H(itself)
		for h in range(len(horses)):
			if h != H:
				# distance for continuous
				dist1=0
				count=0
				for i in continuous:
					hAtt=horses[h].getIthAtribute(i-1)
					HAtt=horses[H].getIthAtribute(i-1)
					if hAtt != '?' and HAtt != '?':
						dist1=dist1+math.pow((float(hAtt)-float(HAtt)),2)
						count=count+1
				if count!=0:
					dist1=dist1/count
				#(hamming) distance for attribute368(discret)
				dist2=0
				for j in attribute368:
					hAtt=horses[h].getIthAtribute(j-1)
					HAtt=horses[H].getIthAtribute(j-1)
					if hAtt != '?' and HAtt != '?':
						dist2=dist2+hammingDist(hAtt,HAtt)
				dist[h]=dist1+dist2
		# range by value de and got the top-1 nearest samples
		distRange=sorted(dist.iteritems(),key=lambda d:d[1])
		#fill the missing value of H-th sample
		line=""
		for i in range(28):
			H_ithAtt=horses[H].getIthAtribute(i)
			#fill i-th attribute
			if H_ithAtt == '?':
				for r in range(len(distRange)):
					k=distRange[r][0]
					h_ithAtt=horses[k].getIthAtribute(i)
					if h_ithAtt != '?':
						H_ithAtt=h_ithAtt
						break
			if i == 0:
				line=H_ithAtt
			else:
				line=line+' '+H_ithAtt
		f.write(line+"\n")
	f.close()