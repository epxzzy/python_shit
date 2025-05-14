print("an example of exceptions: \n\n\n")

try:
    print("69/0")
    blyaat = 69/0
except ZeroDivisionError:
    print("we got a ZeroDivisionError\n\n")


try:
    print("\"69\" + 420")
    blyaat = "69" + 420
except TypeError:
    print("we got a TypeError\n\n")


try:
    print("int(\"no number l bozo\")")
    blyaat = int("no number l bozo")
except ValueError:
    print("we got a ValueError\n\n")


try:
    blyaat = [ "item0" ]
    print(blyaat, "\nprint( blyaat[2] )")
    print(blyaat[2])
except IndexError:
    print("we got a IndexError\n\n")


try:
    blyaat = { "realindex" : "realvalue"}
    print(blyaat, "\nprint( blyaat[\"fakeindex\"] )")
    print(blyaat["fakeindex"])
except KeyError:
    print("we got a KeyError\n\n")



blyaat_file = None
try:
    print("open('blyaat.txt', 'r').read()")
    blyaat_file = open("blyaat.txt", "r").read()
except FileNotFoundError:
    print("we got a FileNotFoundError\n\n")


