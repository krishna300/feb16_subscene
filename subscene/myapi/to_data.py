




def to_data(file):
	file="media/"+file

	with open(file ,'r') as f:
		d=f.read()
	# data1=list()

	data2=d.split("\n")
	# key=1

	e1=[]
	key=0
	e1.append(list())

	for i in data2:
		if i!='':
			e1[key].append(i)
			continue
		if i=='':
			e1.append([])
			key +=1
	return e1