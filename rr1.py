a=[]
total_w=[]
r_burst=[]
finish=[]
total=0

qtm=int (raw_input('Enter time quantum: '))
n=int(raw_input('Total number of processes: '))



for i in xrange(n):
	a.append([])
	a[i].append(raw_input('enter process name: '))
	a[i].append(int(raw_input('enter arrival time: ')))
	a[i].append(int(raw_input('enter burst time: ')))
	a[i].append(a[i][2]) #remaining burst time
	total+=a[i][2] #total bt
	a[i].append(0) #ft

a.sort(key=lambda a:a[1])
x=0
current=a[x][1]
while total>0:
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
	if (x+1)<n:
		x=x+1
	else:
		x=0

print 'Process \t Arrival time \t Burst time \t waiting time'

for i in xrange(n):
	print a[i][0],' \t\t',a[i][1],' \t\t',a[i][2],' \t\t',a[i][4]-a[i][1]-a[i][2]
