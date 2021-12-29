answers = []
for a in range(1, 9999):
    for b in range(1, 9999):
        if a != b:
            allDigits = str(a*b) + str(a) + str(b)
            if ''.join(sorted(allDigits)) == '123456789':
                if a*b not in answers:
                    answers.append(a*b)
    print(a)
print('ans:', sum(answers))