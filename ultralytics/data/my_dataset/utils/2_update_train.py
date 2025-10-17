with open('../ImageSets/train.txt', 'w') as f:
    for i in range(0, 300+1):
        f.write(str(i) + '\n')

print("Done")