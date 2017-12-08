import func_bsearch
 def count(a, q):
 	p = func_bsearch.bsearch(a, q)
 	thicc = func_bsearch.bsearch(a, (q+1))
 	return thicc - p