text=open('mytext.txt','w')
x=text.write("I like coding\nit is a new part\nof my life!!!")
text=open('mytext.txt')
read=text.readlines()
i=0
counter=0
total=0
print("number of lines :"+str(len(read)))

while i<=len(read)-1:
    counter=counter+read[i].count('\n') + read[i].count(' ')
    total+=len(read[i])-read[i].count('\n') - read[i].count(' ')
    i+=1
counter+=1
print('Number of words is :'+str(counter))
print('total number of letters are :' +str(total))