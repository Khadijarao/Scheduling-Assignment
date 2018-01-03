 # even numbered process goes for i/o ater 2 sec for 5 sec

a=[]
total=0

qtm=int (raw_input('Enter time quantum: '))
n=int(raw_input('Total number of processes: '))

for i in xrange(n):
	a.append([])
	a[i].append(int(raw_input('enter process name: ')))
	a[i].append(int(raw_input('enter arrival time: ')))
	a[i].append(int(raw_input('enter burst time: ')))
	a[i].append(a[i][2]) #remaining burst time
	total+=a[i][2] #total bt
	a[i].append(0) #ft
	a[i].append(0) #seconds left till it goes for i/o
	a[i].append(0) #remaining quantum time
	a[i].append(-1) #time that it will come back 

a.sort(key=lambda a:a[1])
x=0
current=a[x][1]
for i in xrange(n):
	if (a[i][0]%2==0):
		a[i][5]=2
while total>0:
	for i in xrange(n):	#checks auxiliary queue
		if a[i][7]<=current and a[i][6]!=0:
			total=total-a[i][6]
			current = current+a[i][6]
			a[i][3]=a[i][3]-a[i][6]
			a[i][7]=-1
			a[i][6]=0
			a[i][5]=5
			if a[i][3]==0:
				a[i][4]=current
			
	if (a[x][0]%2)!=0 :
		if a[x][3]<qtm and a[x][3]!=0 and a[x][1]<=current:
			total=total-a[x][3]
			current=current+a[x][3]
			a[x][4]=current
			a[x][3]=0
		elif a[x][3]>=qtm and a[x][1]<=current:
			a[x][3]=a[x][3]-qtm
			current=current+qtm
			total=total-qtm
			if a[x][3]==0:
				a[x][4]=current
			
	elif (a[x][0]%2)==0 and a[x][7]==-1 and a[x][1]<=current and a[x][3]!=0:
		if a[x][3]<=qtm :
			if a[x][5]>qtm:
				total=total-a[x][3]
				current=current+a[x][3]
				a[x][4]=current
				a[x][3]=0			
			elif a[x][5]<=qtm and a[x][5]<=a[x][3]:
				total=total-a[x][5]
				a[x][3]=a[x][3]-a[x][5]
				current=current+a[x][5]
				a[x][7]=current+5
				a[x][6]=qtm-a[x][5]
			elif a[x][5]<=qtm and a[x][5]>a[x][3]:
				total=total-a[x][3]
				current=current+a[x][3]
				a[x][3]=0	
		elif a[x][3]>qtm:
			if a[x][5]>qtm:
				total=total-qtm
				current=current+qtm
				a[x][3]=a[x][3]-qtm
				a[x][5]=a[x][5]-qtm
					
			else:
				total=total-a[x][5]
				current=current+a[x][5]
				a[x][3]=a[x][3]-a[x][5]
				a[x][7]=current+5
				a[x][6]=qtm-a[x][5]
				a[x][5]=5		
				
				
	if (x+1)<n:
		x=x+1
	else:
		x=0
	i=0
	flag1="true"
	while flag1=="true" and i<n:
		
		if (a[i][0]%2!=0):
			if (a[i][3]!=0):
				flag1="false"
		i=i+1
	if flag1=="true":
		i=0
		flag2="true"
		while flag2=="true" and i<n:
			
			if (a[i][7]!=-1):
				flag2="false"
			i=i+1
	if flag1=="true" and flag2=="false":
		current=current+1
	
print 'Process \t Arrival time \t Burst time \t waiting time'

for i in xrange(n):
	print a[i][0],' \t\t',a[i][1],' \t\t',a[i][2],' \t\t',a[i][4]-a[i][1]-a[i][2]
