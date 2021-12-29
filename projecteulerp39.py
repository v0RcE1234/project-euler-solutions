def is_pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False

def most_frequent(List):
    return max(set(List), key = List.count)

pythagoreanTriples = set()
for c in range(1, 500):
    for a in range(1, c):
        for b in range(c-a+1, c):
            if a < b:
                if is_pythagorean_triple(a, b, c):
                    pythagoreanTriples.add((a, b, c))

pPythagoreanTriples = []
for i in pythagoreanTriples:
    p = sum(i)
    if p < 1001:
        pPythagoreanTriples.append(p)

ans = most_frequent(pPythagoreanTriples)
print(ans)