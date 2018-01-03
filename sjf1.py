a=[]
total_w=[]
n=int(raw_input('Total number of processes: '))
start_time=0
total=0

for i in xrange(n):
	a.append([])
	a[i].append(raw_input('enter process name: '))
	a[i].append(int(raw_input('enter arrival time: ')))
	a[i].append(int(raw_input('enter burst time: ')))
#selection sort
for i in xrange (n):
	pos=i
	j=i+1
	while j<n:
		if a[j][2] < a[pos][2]:
			pos=j
		j=j+1
	temp=a[i][2]
	a[i][2]=a[pos][2]
	a[pos][2]=temp
	
	temp=a[i][0]
	a[i][0]=a[pos][0]
	a[pos][0]=temp

	temp=a[i][1]
	a[i][1]=a[pos][1]
	a[pos][1]=temp

start_time=0
for i in xrange(n):
	total_w.append([])
	total_w[i].append(int(start_time-a[i][1]))
	start_time=start_time+a[i][2]


print 'Process \t Arrival time \t Burst time \t waiting time'

for i in xrange(n):
	print a[i][0],' \t\t',a[i][1],' \t\t',a[i][2],' \t\t',total_w[i]

