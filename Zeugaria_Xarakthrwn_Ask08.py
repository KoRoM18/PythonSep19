import string


ascii_string = set("""!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~""")
ascii = list(ascii_string)
ascii.sort()
infile = open("filetext",'r')
text = infile.read()

def main():

    #Vriskw twn ari8mo olwn twn zeugariwn ascii xarakthrwn tou keimenou
    d = 0
    for k in text:
        if k in ascii:
            d += 1
    doubles = d-2 #Ari8mos Zeugariwn

    #Vriskw poia einai auta ta zeugaria kai poses fores emfanizontai
    for i in ascii:
        for j in ascii:
            a = i + j

            #Emfanizei to ka8e zeugari xarakthrwn poses fores emfanizetai se synerthsh me ton synoliko ari8mo zeugariwn
            if text.count(a): 
                print (a,(" {0:0d}/{1:0d}".format(text.count(a),doubles)))




infile.close()
main()
        
        


        
        
    




