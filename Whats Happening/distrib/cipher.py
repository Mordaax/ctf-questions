def split(word):
    return [char for char in word]


plaintext = input("Enter plaintext: ").upper()

asc = [ord(c) for c in plaintext]
ltr = []

""" Z P F Q H X M T U K A """

for each in asc:
    if each % 10 == 0:
        ltr.append(str(each)[-1])
        ltr.append("N")
    elif each % 9 == 0:
        ltr.append(str(each)[-1])
        ltr.append("U")
    elif each % 8 == 0:
        ltr.append(str(each)[-1])
        ltr.append("L")
    elif each % 7 == 0:
        ltr.append(str(each)[-1])
        ltr.append("S")
    elif each % 5 == 0:
        ltr.append(str(each)[-1])
        ltr.append("E")
    else:
        ltr.append(str(each)[-1])
        ltr.append("C")
        if each % 6 == 0:
            ltr.append("S")
        elif each % 4 == 0:
            ltr.append("E")
        elif each % 3 == 0:
            ltr.append("N")
        elif each % 2 == 0:
            ltr.append("G")
        else:
            ltr.append("Q")

print(ltr)
