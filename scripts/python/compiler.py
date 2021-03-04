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
           ("yield", "sneakbread"),
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
           ("print", "numnums"),
           ("max", "bigbread"),
           ("min", "smolbread"),
           ("sum", "lotsabread"),
           ("all", "allbread"),
           ("len", "longbread"),
           ("range", "slicesof"),
           ("round", "crusts"),
           ("slice", "chop"),
           ("help", "bRead"),
           ("getattr", "getbread"),
           ("setattr", "setbread"),
           ("property", "mybread"),
           ("open", "breadside"),
           ("Exception", "nono")]

words, breadwords = {}, {}
for pair in keywords:
    words[pair[0]] = pair[1]
    breadwords[pair[1]] = pair[0]

chars = string.ascii_letters + string.digits
symbols = [":", ";", ",", "=", "(", ")", "[", "]", "{", "}", "@", "'", '"',
           "+", "-", "*", "/", "%", "<", ">", ".", "!", "_", "#", " ", "\n"]    

def compile(filename):

    filetype = gettypeof(filename)[0]
    if filetype not in ["brr", "py", "pyw"]:
        print("File must be a .brr, .py or .pyw file")
        return
    if filetype == "brr":
        newfiletype = "py"
    else:
        newfiletype = "brr"

    inlongstring = None

    newfilename = filename[:-len(filetype)] + newfiletype
    newfile = open(newfilename, "w+")
    file = open(filename, "r")

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
    print(f"Done! Compiled {filename} --> {newfilename}")
        
if __name__ == "__main__":
    with open("file.txt", "r") as file:
        filename = file.read().split("\n")[0]
    if filename[0] in ["'", '"']:
        filename = filename[1:-1]
    compile(filename)
