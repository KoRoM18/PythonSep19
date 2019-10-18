def main():
    line = input("Enter a line of code: ")
    op = 0 # open
    cl = 0 # close
    program = True
    # Metraei swsta to anoigma kai kleisimo twn parenthesewn
    for character in line:  
        if character == '(':
            op += 1
        elif character == ')':
            cl += 1
            if cl > op:
                program = False
    # Emfanizei an exei ginei swsta to anoigma kai kleisimo
    if op == cl:
        if program == True:
            print ("Correct")
    else:
        print ("Wrong")




main()
