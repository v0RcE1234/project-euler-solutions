
import itertools

def compute():
	arr = list(range(10))
	temp = itertools.islice(itertools.permutations(arr), 999999, None)
	return "".join(str(x) for x in next(temp))

print(compute())