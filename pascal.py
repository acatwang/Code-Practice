def triangle(n, lol=None):
	print 'N: ', n
	if lol is None: lol = [[1]]
	if n == 1: return lol
	else:
   		print "lol: ",lol
    	prev_row = lol[-1]
    	new_row = [1] + [sum(i) for i in zip(prev_row, prev_row[1:])] + [1]
    	return triangle(n - 1, lol + [new_row])

print triangle(5)