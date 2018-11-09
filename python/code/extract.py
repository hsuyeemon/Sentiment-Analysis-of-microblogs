#remove the duplicate words in list
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

#read from tokenized tweets
f = open('../data/output/tokenized.txt','r')
temp = f.readlines();
f.close();

#split the tokens,types,confidence and original text
tokens = []
#print(len(temp))
for i in range (len(temp)):
  tokens.append(temp[i].split('\t'))

#split the tokens and types into arrays
for i in range(len(tokens)):
    tokens[i][0]=tokens[i][0].split(" ")
    tokens[i][1]=tokens[i][1].split(" ")

#remove the non-content words
featurePosList = {'N','O','^','S','Z','V','A','R','!','#','E'}
extractedFeatures = []

for i in range(len(tokens)):
    str=""
    for j in range(len(tokens[i][1])):
        if(tokens[i][1][j] in featurePosList):
            str+=tokens[i][0][j]
            str+=" "
    #print(str);
    str=' '.join(unique_list(str.split()))
    extractedFeatures.append(str)

print("enter the original file name")
filename = input()

#relate with classes from original text file
f = open('../data/input/'+filename,'r')
lines = f.readlines()
f.close()

arr= [];
#print(len(lines))
for i in range ( len(lines) ): 
    arr.append(lines[i].split('\t'))

#write the extracted features
file = open('../data/output/extracted.txt','w') 
for  i  in  range (len(temp)): 
    text = arr[i][2];
    file.write(text);
    file.write('\t');
    file.write(extractedFeatures[i]);
    file.write('\n');
    
file.close() 