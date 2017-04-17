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

if __name__ == "__main__":
	#don't consider 3:  Hospital Number, 28: cp_data, 25, 26, 27: type of lesion, 23: outcome,
	#24: surgical lesion,1:  surgery, 10: capillary refill time,11: pain,14: nasogastric tube,
 	#15: nasogastric reflux, 18: abdomen,9:  mucous membranes, 12: peristalsis,8:  peripheral pulse
 	#21: abdominocentesis appearance,17: rectal examination - feces
 	
 	#only consider 2:  Age, 7: temperature of extremities, 13:abdominal distension
	discrete={2,7,13}
	#read file and get data to horses
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
	print "hello"
	# print len(horses)
	# for i in range(len(horses)):
	# 	horses[i].printHorse()

	f=open('horse-colic-fillWithRelativity.txt','w')
	for H in range(len(horses)):
		#horses[H].printHorse()
		line=""
		#get the all the attribute values that not equal '?'
		attributes=dict()
		for i in discrete:
			attribute=horses[H].getIthAtribute(i-1)
			if attribute != '?' :
				attributes[i-1]=attribute
		#find the horses that have same attributes
		horsesSameAttributes=[]
		if len(attributes)!=28:
			for h in range(len(horses)):
				sign=0 #sign=0 means h's all attributes not equal horse's attributes
				for item in attributes:
					#print item
					if attributes[item]== horses[h].getIthAtribute(item):
						#add to horsesSameAttributes only if there is one same item attribute
						# if item!=2:#Hospital Number can be different
						sign=1
						break
				if sign==1:
					horsesSameAttributes.append(horses[h])
			print len(horsesSameAttributes)
			for i in range(len(horsesSameAttributes)):
				horsesSameAttributes[i].printHorse()
		for i in range(28):
			attribute=horses[H].getIthAtribute(i)
			#print "attribute:"
			#print attribute
			if attribute=='?':
				#get the i-th attribute set of horsesSameAttributes
				atts=[]
				for h in range(len(horsesSameAttributes)):
					att=horsesSameAttributes[h].getIthAtribute(i)
					if att!='?':
						atts.append(att)
				#get the value which most frequency for i-th attribute
				setAtts=set(atts)
				mostFrequency=0
				mostR=""
				sign0=0
				for r in setAtts:
					frequency=atts.count(r)
					if sign0==0:
						mostFrequency=frequency
						mostR=r
						sign0=1
					elif frequency>mostFrequency:
						mostFrequency=frequency
						mostR=r
				attribute=mostR
			if i==0:
				line=attribute
			else:
				line=line+' '+attribute
		#print "line"
		#print line
		f.write(line+"\n")
	f.close()



