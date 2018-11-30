with open(r'file.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()

print(s1)
print(s2)

with open('file.txt', 'w') as ouf:
    ouf.write('fourth')
    ouf.write(str(25))







