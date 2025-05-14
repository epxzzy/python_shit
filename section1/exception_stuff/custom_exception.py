class TooOldError(Exception):
    pass

try:
    num = int(input("Enter age: "))
    if num > 18:
        raise TooOldError
except TooOldError:
    print("you are not welcome to the island")
else:
    print("welcome to the island")
finally:
    print("NEXT!!!!")