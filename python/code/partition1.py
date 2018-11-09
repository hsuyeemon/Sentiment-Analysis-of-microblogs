import numpy as np
from sklearn.model_selection import KFold
import pandas as pd

f = open('../data/output/extracted.txt', 'r')
lines = f.readlines()
f.close()
arr= [];
#print(len(lines))
for  i  in  range ( len(lines) ): 
    arr.append(lines[i].split('\t'))

print(arr[0])

#topics
print("enter the original file name")
filename = input()
f1 = open('../data/input/'+filename, 'r')
l = f1.readlines()
f1.close()

filename = filename[:-4]
#print(filename)

a= [];
#print(len(l))
for  j  in  range ( len(l) ): 
    a.append(l[j].split('\t'))

#print(len(a))

cleanlist = []
for j in range (len(a)):
    if a[j][1] not in cleanlist :
        cleanlist.append(a[j][1])

#print(len(cleanlist))
X=[]
Y=[]
for i in range(len(cleanlist)):
    XX = []
    YY = []
    for j in range(len(a)-1):
        if a[j][1] == cleanlist[i] :
            #print(arr[j])
            #XX.append(arr[j][1])
            XX.append(arr[j])
            YY.append(arr[j][0])
    
    X.append(XX)
    Y.append(len(XX))


###data set 1
b = []
maxim = max(Y)
i = 0
for j in range (maxim):
    bb = []
    for k in range (len(cleanlist)):
        try:
            bb.append(X[k][j])
        except IndexError:continue
    b.append(bb)

kf = KFold(n_splits=10)
i = 0;
trainIndex = []
testIndex = []

for train, test in kf.split (b):
    trainIndex.append(train)
    testIndex.append(test)
    #print('train index',train)
    #print('test index',test)

for i in range(10):
    f1 = open('../data/dataset1_'+filename+'/train'+str(i)+'.txt',"w") 
    f2 = open('../data/dataset1_'+filename+'/test'+str(i)+'.txt',"w")
    for j in range (len(trainIndex[i])):
        ti = trainIndex[i][j]
        for k in range (len(b[ti])):
            print(trainIndex[i][j])
        
            print(i,j)
            print(b[ti][k][0])
            f1.write(str(b[ti][k][0]))
            f1.write("\t")
            f1.write(str(b[ti][k][1]))
    for j in range (len(testIndex[i])):
        ti = testIndex[i][j]
        for k in range (len(b[ti])):
            print(testIndex[i][j])
        
            print(i,j)
            print(b[ti][k][0])
            f2.write(str(b[ti][k][0]))
            f2.write("\t")
            f2.write(str(b[ti][k][1]))
    
    f1.close();
    f2.close();

####data set 2

kf = KFold(n_splits=10)
i = 0;
trainIndex = []
testIndex = []

for train, test in kf.split (cleanlist):
    trainIndex.append(train)
    testIndex.append(test)
    
    # If this is the case,
    print('train index',train)
    print('test index',test)

for i in range(10):
    f1 = open('../data/dataset2_'+filename+'/train'+str(i)+'.txt',"w") 
    f2 = open('../data/dataset2_'+filename+'/test'+str(i)+'.txt',"w")
    for j in range (len(trainIndex[i])):
        ti = trainIndex[i][j]
        for k in range (len(X[ti])):
            print(trainIndex[i][j])
        
            print(i,j)
            print(X[ti][k][0])
            f1.write(str(X[ti][k][0]))
            f1.write("\t")
            f1.write(str(X[ti][k][1]))
    for l in range (len(testIndex[i])):
        ti = testIndex[i][l]
        for m in range (len(X[ti])):
            print(testIndex[i][l])
        
            print(i,l)
            print(X[ti][m][0])
            f2.write(str(X[ti][m][0]))
            f2.write("\t")
            f2.write(str(X[ti][m][1]))

    f1.close()
    f2.close()