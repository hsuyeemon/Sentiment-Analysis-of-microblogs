print("please enter the original file name")
filename = input()
print(filename)

f = open('../data/input/'+filename,"r")
lines = f.readlines()
f.close()



#print(lines)

arr= []
for  i  in  range ( len(lines) ): 
    arr.append(lines[i].split('\t'))
#print(len(lines))


filename = filename[:-4]
file = open('../data/output/tweets'+filename+'.txt','w+') 
for  i  in  range (len(lines)): 
    #print(i)
    text = arr[i][3]
    file.write(text) 
file.close() 



