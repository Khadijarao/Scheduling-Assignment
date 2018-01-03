a=[]
finish=[]
total=0
current=0

n=int(raw_input('Total number of processes: '))

for i in xrange(n):
	a.append([])
	a[i].append(raw_input('enter process name: '))
	a[i].append(int(raw_input('enter arrival time: ')))
	a[i].append(int(raw_input('enter burst time: ')))
	a[i].append(a[i][2]) #remaining burst time
	a[i].append(0) #finish time
	total+=a[i][2] #total burst time


x=0
while total>0:
	flag=0
	y=0
	while y<n and flag==0: #if another process entered with smaller burst time
		if current==a[y][1] and a[y][3]<a[x][3] and a[y][3]!=0:
			flag=1			
			x=y
		y=y+1
	if a[x][3]>0:	#process is running
		total=total-1
		a[x][3]=a[x][3]-1
		current=current+1
		if a[x][3]==0:
			a[x][4]=current
	elif (x+1)<n:
		x=x+1
	else:
		a.sort(key=lambda a:a[3]) #else if all processes have entered and x is at n then order by remaining bt
		q=0
		flag2=0
		while q<n and flag2==0:
			if a[q][3]>0 and a[q][1]<=current:
				flag2=1
				x=q
			q=q+1

a.sort(key=lambda a:a[1])
print 'Process \t Arrival time \t Burst time \t waiting time'

for i in xrange(n):
	print a[i][0],' \t\t',a[i][1],' \t\t',a[i][2],' \t\t',a[i][4]-a[i][1]-a[i][2] #ft-at-bt
