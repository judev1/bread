import os
import re
import string

# Variables

gettypeof = re.compile(r"\w+$").search

keywords = [("class", "burmger"),
           ("def", "sandwhich"),
           ("if", "tasty"),
           ("elif", "tastier"),
           ("else", "tastiest"),
           ("for", "toppings"),
           ("while", "eat"),
           ("pass", "cry"),
           ("return", "dingding"),
           ("break", "soggybread"),
           ("continue", "sneakbread"),
           ("async", "vegan"),
           ("await", "watchovenfor"),
           ("try", "pokebread"),
           ("except", "stalebread"),
           ("finally", "stilledible"),
           ("in", "ingredientof"),
           ("is", "inside"),
           ("or", "mm"),
           ("and", "nom"),
           ("not", "anythingbut"),
           ("import", "bake"),
           ("from", "preheat"),
           ("with", "butter"),
           ("as", "crispy"),
           ("global", "chonkybread"),
           ("nonlocal", "nab"),
           ("assert", "facts"),
           ("lambda", "teleportbread"),
           ("True", "bread"),
           ("False", "nobread"),
           ("None", "lackofbread"),
           ("str", "toast"),
           ("int", "milk"),
           ("float", "seeds"),
           ("bool", "potatoe"),
           ("list", "buns"),
           ("dict", "oven"),
           ("tuple", "cooked"),
           ("set", "flour"),
           ("input", "gimme"),
           ("print", "boast"),
           ("max", "bigbread"),
           ("min", "smolbread"),
           ("sum", "lotsabread"),
           ("all", "allbread"),
           ("len", "allbread"),
           ("zip", "zip"),
           ("range", "slicesof"),
           ("round", "crusts"),
           ("slice", "chop"),
           ("chr", "chr"),
           ("ord", "ord"),
           ("map", "map"),
           ("help", "bRead"),
           ("id", "id"),
           ("getattr", "getbread"),
           ("setattr", "setbread"),
           ("property", "mybread"),
           ("open", "butter"),
           ("Exception", "nono")]

words, breadwords = {}, {}
for pair in keywords:
    words[pair[0]] = pair[1]
    breadwords[pair[1]] = pair[0]

inlongstring = None
chars = string.ascii_letters + string.digits

symbols = [":", ";", ",", "=", "(", ")", "[", "]", "{", "}", "@", "'", '"',
           "+", "-", "*", "/", "%", "<", ">", ".", "!", "_", "#", " ", "\n"]

# User input

while True:
    file = input("Enter the file to compile/decomplie on: ")

    try:
        open(file, "x").close()
        os.remove(file)
        print("File does not exist")
        continue
    except: pass

    filetype = gettypeof(file)[0]
    if filetype not in ["brr", "py", "pyw"]:
        print("File must be a .brr, .py or .pyw file")
        continue
    if filetype == "brr":
        newfiletype = "py"
    else:
        newfiletype = "brr"
    break

# Complier/decomplier

newfile = file[:-len(filetype)] + newfiletype
newfile = open(newfile, "w+")
file = open(file, "r")

for line in file.readlines():

    word = ""
    lastchar = ""
    instring = None
    comment = False

    for i, char in enumerate(line):

        if comment:
            newfile.write(char)
            continue

        elif inlongstring:
            if char != inlongstring:
                newfile.write(char)
                continue

        elif instring:
            if char != instring:
                newfile.write(char)
                continue           

        elif char in chars:
            word += char
            continue

        if filetype == "brr":
            if word in breadwords:
                word = breadwords[word]
        else:
            if word in words:
                word = words[word]
        newfile.write(word)
        word = ""
        
        if char in symbols:
            if char == "#":
                comment = True
            elif char in ["'", '"']:
                if line[i-1] == char and not instring:
                    if inlongstring: inlongstring = None
                    else: inlongstring = char
                elif instring: instring = None
                else: instring = char
            newfile.write(char)

newfile.close()
        
