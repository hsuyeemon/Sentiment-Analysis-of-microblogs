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

file = open('../data/output/tweets.txt','w+') 
for  i  in  range (len(lines)): 
    #print(i)
    text = arr[i][3]
    file.write(text) 
file.close() 



