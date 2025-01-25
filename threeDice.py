d = { x:0 for x in range(3,19)}
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            d[i+j+k] += 1

print(d)
