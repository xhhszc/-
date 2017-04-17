def getMostFrequency(attribute):
	setAttribute=set(attribute)
	m=0
	mostItem=""
	mostFrequency=0
	for item in setAttribute:
		itemFrequency=attribute.count(item)
		if m==0:
			mostItem=item
			mostFrequency=itemFrequency
			m=1
		elif itemFrequency>mostFrequency:
			mostItem=item
			mostFrequency=itemFrequency
	return mostItem

def getMostFrequencyList(Attribute):
	item=[]
	for i in range(28):
		item.append(getMostFrequency(Attribute[i]))
	return item

if __name__ == "__main__":
	#read file
	f=open('horse-colic.txt','r')
	Attribute=dict()
	# line=f.readline()
	for line in f:
		line=line.strip('\n')
		line=line.strip('\r')
		attribute=line.split(' ')
		for i in range(28):
			if i not in Attribute:
				Attribute[i]=[]
			if attribute[i]!='?':
				Attribute[i].append(attribute[i])
	f.close()
	itemFrequencyList=getMostFrequencyList(Attribute)
	f2=open('horse-colic-fillWithMostFrequency.txt','w')
	f=open('horse-colic.txt','r')
	for line in f:
		line=line.strip('\n')
		line=line.strip('\r')
		attribute=line.split(' ')
		if '?' not in attribute:
			f2.write(line+"\n")
		else:
			stringLine=""
			for i in range(28):
				if attribute[i]=='?':
					attribute[i]=itemFrequencyList[i]
				if i==0:
					stringLine=attribute[i]
				else:
					stringLine=stringLine+' '+attribute[i]
			f2.write(stringLine+"\n")
	f.close()
	f2.close()



