ans = 1
for onepound in range(3):
    for fiftypence in range(5-2*onepound):
        for twentypence in range(11-5*onepound):
            for tenpence in range(21-10*onepound):
                for fivepence in range(41-20*onepound):
                    for twopence in range(101-50*onepound):
                        for onepence in range(201-100*onepound):
                            if 1*onepence+2*twopence+5*fivepence+10*tenpence+20*twentypence+50*fiftypence+100*onepound == 200:
                                ans += 1
            print(onepound)
print('ans:', ans)