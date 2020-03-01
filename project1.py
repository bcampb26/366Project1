operations = {"addi": "0b001000", "andi" : "0b001100", "lw":"0b100011", "sw":"0b101011",
              "add": ["0b000000","0b00000100000"], "sub": ["0b000000", "0b00000100010"], "slt": ["0b000000", "0b00000101010"],
              "mult": ["0b000000", "0b00000011000"],
              "bne": "0b000101", "beq": "0b000100", "j":"0b000010"}

Registers = [0]*35
Binary_strings = []
code = []
counter = 0

def display(): #display the table as registers potentially used as putput
    print("_______________________________________")
    print("|Register | adress | value |           |")
    for x in range(35):
            print("_______________________________________")
            if (x> 31):
                if x == 32:
                    x = "lo"
                if x == 33:
                    x = 'hi'
                if x == 34:
                    x = 'PC'
            print("${}| adress:      |value:        |    ".format(x))



#reads input, stores int code array, ignores loops and comments
with open('hex2mips.txt') as inputTxt:
    for line in inputTxt:
        if not line.strip():
            break
        elif not line.startswith("#") and not ":" in line:
            line.strip()
            code.append(line)
            counter +=1

#step 2 convert hex -> binary-> store into the array Binary_strings
Cvalue = 0
def hex2Binary():
    for x in range(counter):
        Cvalue = format(int(code[x],16), '032b')
        Binary_strings.append(Cvalue)

#step 3 store op ... rt... rs..etc

def bin2mips():
     for x in range(counter):
         opp = Binary_strings[x][0:6]
         rs = Binary_strings[x][7:12]
         rt = Binary_strings[x][13:18]
         rd = Binary_strings[x][19:24]
         print("opp is :", opp, " rs : ", rs, " rt : ",rt, "rd : ",rd)





#counter = 0; # shows the values in each register
# for x in Registers:
#     print(" {} : {}".format(counter, Registers[x]))
#     counter = counter + 1


hex2Binary()
bin2mips()
#display()
