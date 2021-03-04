import os
import re
import string

# local variables

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
           ("yield", "bbbread"),
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

breadwords = {}
for pair in keywords:
    breadwords[pair[1]] = pair[0]

chars = string.ascii_letters + string.digits
symbols = [":", ";", ",", "=", "(", ")", "[", "]", "{", "}", "@", "'", '"',
           "+", "-", "*", "/", "%", "<", ">", ".", "!", "_", "#", " ", "\n"]

# Interpreter

def interpret(filename):

    code = ""
    inlongstring = None

    file = open(filename, "r")
    for line in file.readlines():

        word = ""
        lastchar = ""
        instring = None
        comment = False

        for i, char in enumerate(line):

            if comment:
                code += char
                continue

            elif inlongstring:
                if char != inlongstring:
                    code += char
                    continue

            elif instring:
                if char != instring:
                    code += char
                    continue           

            elif char in chars:
                word += char
                continue

            if word in breadwords:
                word = breadwords[word]
            code += word
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
                code += char

    exec(code)

if __name__ == "__main__":
    with open("file.txt", "r") as file:
        filename = file.read().split("\n")[0]
    if filename[0] in ["'", '"']:
        filename = filename[1:-1]
    interpret(filename)
        
