import sys
import os
print("Hexagon 0.5")
print("Created by +HRs.")
print("August 2019")
print("")
sub_arg_mode = False
swtch = ""
count = 0
outhex = ""
outtxt = ""
for arg in sys.argv[1:]:
    if arg == "--help":
        print("Usage: python hex.py [--file <filename>] ///Prints the file")
        print("Usage: python hex.py [--help] ////prints this help")
    elif arg == "--file":
        sub_arg_mode = True
        swtch = arg
    elif sub_arg_mode == True:
        if swtch == "--file":
            try:
                file1 = open(arg,'rb')
            except FileNotFoundError:
                print("File not found!")
                os.abort()
            print("Output:") 
            buff = file1.read(16)
            while buff:
                for byt in buff:
                    if byt in [127,255,13,10] :
                        repbyt = 32
                    elif byt < 32:
                        repbyt = 46
                    else:
                        repbyt = byt
                    outhex = outhex+('%02x'%byt)+' '
                    outtxt = outtxt+'%c'%repbyt+' '
                print('{outhex: <48}'.format(outhex=outhex.upper()),end='')
                print('\t',end=' ')
                print('{outtxt: <16}'.format(outtxt=outtxt),end='')
                print('')
                outhex = ""
                outtxt = ""
                buff = file1.read(16)
            file1.close()
    else:
        print("Syntax Error")