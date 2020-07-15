def treeSort(arr):
	l=[]
	r=[]
	c=[arr[0]] # Node
	for item in arr:
		if item<arr[0]:
			l.append(item) # Left Branch of the Node
		if item>arr[0]:
			r.append(item) # Right branch of the Node
	# print(l)
	# print(c)
	# print(r)
	if len(l)>1:
		l= treeSort(l) # Recursion for making the left branch 

	if len(r)>1:
		r= treeSort(r) # Recursion for making the Right branch

	return l+c+r  #Return the concatinated array  

x=[2,6,3,4,8,67,44,32,12,7]

x=treeSort(x)

print(x)