cur = 1
prev = 0
i = 1
while True:
    if len(str(cur)) == 1000:
        print('Answer is:', i)
        break
    i += 1
    cur, prev = cur + prev, cur