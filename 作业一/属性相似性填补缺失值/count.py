	

if __name__ == "__main__":
	continuous= {4,5,6,16,19,20,22}
	#read file
	f=open('horse-colic.txt','r')
	Attribute=dict()
	missAllContinuous=0
	# line=f.readline()
	for line in f:
		miss=0
		line=line.strip('\n')
		line=line.strip('\r')
		attribute=line.split(' ')
		for i in range(28):
			if i not in Attribute:
				Attribute[i]=[]
			if attribute[i]!='?':
				Attribute[i].append(attribute[i])
			elif i+1 in continuous:
				miss=miss+1
		if miss == 7:
			missAllContinuous=missAllContinuous+1
	f.close()
	for i in range(28):
	 	print i+1," : ",len(Attribute[i])
	print missAllContinuous


