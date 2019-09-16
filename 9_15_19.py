# def patternedMessage(msg, pattern):
#     string = ""
#     finalstring = ""
#     #disregarding first and last new line
#     if pattern[0] == '\n':
#         pattern = pattern[1:]
#     if pattern[-1] == '\n':
#         pattern = pattern[:-1]

#     #replacing the white space for pattern and msg
#     newpattern = pattern.replace(" ", "")
#     newmsg = msg.replace(" ","")

#     #add the according characters based on the number of string count

#     for i in range(len(newpattern)):
#         div = i%len(newmsg)
#         string += newmsg[div]

#     print(string)

#     k = 0
#     for c2 in pattern:
#         if c2.isspace() == False:
#             c2 = string[k]
#             finalstring += c2
#             k += 1
#         else:
#             if c2 == "\n":
#                 finalstring += "\n"
#             elif c2 == "\t":
#                 finalstring += "\t"
#             finalstring += " "
#     print(finalstring)
#     return finalstring
import math

def patternedMessage(msg,pattern):
    if pattern[0] == '\n':
        pattern = pattern[1:]
    if pattern[-1] == '\n':
        pattern = pattern[:-1]

    newmsg = msg.replace(" ","")
    final = ""
    string = ""
    #count will increment everytime its a star
    count = 0

    for i in range(len(pattern)):
        div = i%len(newmsg)
        string += newmsg[div]

    for i in range(len(pattern)):
        if pattern[i] == "*":
            final += string[count]
            count += 1
        elif pattern[i] == " ":
            final += " "
        elif pattern[i] == "\n":
            final += "\n"
        elif pattern[i] == "\t":
            final += "\t"
        else:
            print("what the fuck is this")
            print(pattern[i])

    print (final)
    return final

assert(patternedMessage("abc def",   "***** ***** ****")   ==
       "abcde fabcd efab")
assert(patternedMessage("abc def", "\n***** ***** ****\n") == 
       "abcde fabcd efab")

assert(patternedMessage("Go Pirates!!!", """
***************
******   ******
***************
""")   ==
       """GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira""")

print("""
***
* *
***
""".replace(" ",""))

print(len("""
***
* *
"""))

# def encodeRightLeftRouteCipher(text, rows):
#     numcol = math.ceil(len(text)/rows)
#     counter = 0
#     while numcol*rows != len(text):
#         c = ord("z") - counter
#         if c < ord("a"):
#             c = chr(order+26)
#         counter += 1
#         text += chr(c)
#     newstring=""
#     k=0
#     line = ""
#     for row in range(rows+1):
#         for col in range(numcol+1):
#             i = row + col*numcol
#             while k*numcol < rows*numcol:
#                 line = text[k:len(text):rows]
#                 if row%2 == 1:
#                     line = line[::-1]
#                 newstring += line
#                 k+=1
#     print(newstring)

def encodeRightLeftRouteCipher(text,rows):
    final = ""
    final += str(rows)

    cols = math.ceil(len(text)/rows) #5 cols
    # so we know we're trynna make a grid with 3 ros, 5 cols

    #now we need to add the last letter 
    counter = 0
    if len(text) != rows * cols:
        for i in range(rows * cols - len(text)):
            c = ord("z") - counter
            if c < ord("a"):
                c = chr(order+26)
            counter += 1
            text += chr(c)

    # now since we have the exact number for full row and col
    # we will be adding to the grid

    for i in range(rows):
        for j in range(cols):
            if i % 2 == 0:
                index = i + rows*j
                final += text[index]
            else:
                # every other row go the other way
                index = i + rows * (cols - 1 - j)
                print(index)
                final += text[index]

    print (final)
    return final


assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",3) == "3WTCTWNDKTEAAAAz") 












