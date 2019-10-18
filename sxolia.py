input_program = input("Enter name of C++ program: ")
text =open(input_program,'r')
text=text.read()

j=1
posA=0
posB=0
#Xwrizw ana grammh kai elegxw arxika gia sxolia mias grammhs
print ("\nSingle line comments: ")
with open(input_program,'r') as f: 
    for lines in f:
        l = lines.split()
        line = " ".join(l)

        #Sxolia me //
        for i in range(1,len(line)):
            if line[i]=='/' and line[i-1]=='/':
                print (line[i-1:])

#Elegxw to programma gia sxolia pollaplwn grammwn
print ("\n\nMultiline comments: ")
num = text.count("/*")
while j<=num:
    
    posA = text[posB:].find("/*")#3ekinaei tis 8eseis apo to 0
    posA=posA+posB #Prosthetw gia na einai swste oi epomenes epanalipseis
    posB = text[posA:].find("*/")#3ekinaei apo thn 8esh tou A
    posB=posB+posA 
    
    
    print (text[posA:posB+2])#+2 giati to */ einai 2 xaraktres
    
    j+=1
    
    
    
    

    
                

            
        
        

        

        
