#Arxikopoihsh listas ari8mvn
numberList = []


max = 0

#Ftiaxnw lista apo to 2 mexri to 1000
for k in range (2,1000): #To 1 den einai prwtos ari8mos
    numberList.append(k)

#Elegxos gia diairetes 
for i in numberList:
    for j in numberList:
        if (j%i==0) and not(j==i):
            numberList.remove(j)


for s in numberList:
    for d in numberList:
        deff = d - s
        if (deff > max):
            max = deff

#Emfanish listas
print (numberList)

print ("\n", "Max difference between odd numbers from 1 to 1000: ",max)

