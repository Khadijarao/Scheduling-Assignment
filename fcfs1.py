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
	total_w.append([])
	total_w[i].append(int(start_time-a[i][1]))
	start_time=start_time+a[i][2]

a.sort(key=lambda a:a[1])
print 'Process \t Arrival time \t Burst time \t waiting time'

for i in xrange(n):
	print a[i][0],' \t\t',a[i][1],' \t\t',a[i][2],' \t\t',total_w[i]

