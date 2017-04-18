import numpy as np
import matplotlib as mpl  
import matplotlib.pyplot as plt  
import statsmodels.api as sm 

def getFrequency(attribute):
	setAttribute=set(attribute)
	res={}
	for item in setAttribute:
		res[item]=attribute.count(item)
	return res

def getMax(attribute):
	return max(attribute)

def getMin(attribute):
	return min(attribute)

def getAver(attribute):
	return sum(attribute)/len(attribute)

def getMedandQ(attribute):
	l=len(attribute)
	attribute.sort()
	MedandQ=[]
	if l%2==0:#median
		MedandQ.append((attribute[l/2]+attribute[l/2+1])/2)
	else:
		MedandQ.append(attribute[l/2+1])
	if (l+1)%4==0:#Q
		MedandQ.append(attribute[(l+1)/4])
		MedandQ.append(attribute[3*(l+1)/4])
	else:
		MedandQ.append((attribute[(l+1)/4]+attribute[(l+1)/4+1])/2)
		MedandQ.append((attribute[3*(l+1)/4]+attribute[3*(l+1)/4+1])/2)
	return MedandQ

def getMissCount(attribute):
	return 368-len(attribute)

def drawQQ(attribute,name):
	sm.qqplot(np.log(attribute),line='s') 
	stringname="qq"+name+".jpg"
	plt.savefig(stringname)
	plt.show()
def drawBox(attribute,name):
	#fig=plt.figure()
	plt.boxplot(attribute,notch=False,sym='rs',vert=True)
	plt.xlabel(name)
	plt.title('Box plot')
	stringname="box"+name+".jpg"
	plt.savefig(stringname)
	plt.show()
def drawHist(attribute,name):
	#mybins=np.arange(-100,100,5)#fixed bin size
	plt.xlim([min(attribute)-5,max(attribute)+5])
	plt.hist(attribute,alpha=0.5)
	plt.title('Histograms plot')
	plt.xlabel(name)
	plt.ylabel('count')
	stringname="hist"+name+".jpg"
	plt.savefig(stringname)
	plt.show()

if __name__ == "__main__":
	#read file
	f=open('horse-colic-dropMissingData.txt','r')
	Attribute=dict()
	discrete={1,2,3,7,8,9,10,11,12,13,14,15,17,18,21,23,24,25,26,27,28}
	# 3 is a continuous number but should be considered as a discrete number
	continuous= {4,5,6,16,19,20,22}
	AttributeName={1:'Surgery',2:'Age',3:'Hospital Number',4:'Rectal temperature',\
	5:'Pulse',6:'Respiratory rate',7:'Temperature extremities',8:'Peripheral pulse',\
	9:'Mucous membranes',10:'Capillary refill time',11:'Pain',12:'Peristalsis',\
	13:'Abdominal distension',14:'Nasogastric tube',15:'Nasogastric reflux',\
	16:'Asogastric reflux PH',17:'Rectal examination - feces',18:'Abdomen',\
	19:'Packed cell volume',20:'Total protein',21:'Abdominocentesis appearance',\
	22:'Abdomcentesis total protein',23:'Outcome',24:'Surgical lesion',\
	25:'Type of lesion',26:'Type of lesion',27:'Type of lesion',28:'cp_data'}
	# Surgery=[]#discrete Yes/not
	# Age=[]#Adult/Young
	# Hospital_Number=[]#the numeric id
	# Rectal_temperature=[]#continuous variable,
	# Pulse=[]#continuous variable,
	# Respiratory_rate=[]#continuous
	# Temperature_extremities=[]#discrete:Normal/Warm/Cool/Cold
	# Peripheral_pulse=[]#discrete:Normal/Increased/Reduced/Absent
	# Mucous_membranes=[]#discrete:Normal pink/bright pink/pale pink/pale cyanotic/bright red/dark cyanotic
	# capillary_efill_ime=[]#discrete:< 3 / >=3
	# Pain=[]#discrete:alert, no pain/depressed/intermittent mild pain/intermittent severe pain/continuous severe pain
	# Peristalsis=[]#hypermotile/normal/hypomotile/absent
	# line=f.readline()
	for line in f:
		line=line.strip('\n')
		line=line.strip('\r')
		attribute=line.split(' ')
		for i in range(28):
			if i not in Attribute:
				Attribute[i]=[]
			if attribute[i]!='?':
				if i+1 in continuous:
					Attribute[i].append(float(attribute[i]))
				else:
					Attribute[i].append(attribute[i])
	f.close()

	for i in range(28):
		#for j in range(len(Attribute[i])):
		if i+1 in discrete:# get frequency for discrete attribute
			frequency=getFrequency(Attribute[i])
			print AttributeName[i+1],"  The frequency of each value:",frequency
		else:
			print AttributeName[i+1],"  Max value:",getMax(Attribute[i]), "Min value:",getMin(Attribute[i]),\
			 "Average value:",getAver(Attribute[i]), "Median,Q1,Q3:",getMedandQ(Attribute[i]),\
			  "The number of Miss value:",getMissCount(Attribute[i])
			drawHist(Attribute[i],AttributeName[i+1])
			drawQQ(Attribute[i],AttributeName[i+1])
			drawBox(Attribute[i],AttributeName[i+1])
		#print Attribute[i]


