def to_ascii(char):
    return chr(int(char, 2))


def translate(txt):
    res = ""
    letters = txt.split(" ")
    for letter in letters:
        res += to_ascii(letter)
    return res


c = ""
for line in open("märchen").read().splitlines():  # input file contains the Story just copied from web page
    for i in line.split():
        if "cyber-" in i.lower():
            if c != "":
                if len(c.split()[-1]) > 7:
                    c += " 1"
                else:
                    c += "1"
            else:
                c = "1"
        elif "cyber" in i.lower():
            if c != "":
                if len(c.split()[-1]) > 7:
                    c += " 0"
                else:
                    c += "0"
            else:
                c = "0"

print(translate(c))

# Copied to_ascii() and translate() from https://www.youtube.com/watch?v=5EoUi5_H_7s
