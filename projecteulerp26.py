def recurring_cycle_len(dividend, divisor):
    prevDividends = {dividend: 0}
    i = 1
    while True:
        dividend = dividend % divisor
        if dividend == 0:
            return 0
        while dividend < divisor:
            dividend = dividend*10
        if dividend in prevDividends:
            recurringCycleLen = i - prevDividends[dividend]
            return recurringCycleLen
        prevDividends[dividend] = i
        i += 1

ans = 0

for d in range(2, 1000):
    if recurring_cycle_len(1, d) > ans:
        ans = recurring_cycle_len(1, d)
        highD = d

print('rec_len:', ans, 'd:', highD)