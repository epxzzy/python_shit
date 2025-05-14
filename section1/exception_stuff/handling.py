try:
    print("heinous acts here")
except:
    print("saved yo ass")
    # close file handles


try:
    print("heinous acts here")
except TypeError:
    print("saved from a specific error")




try:
    print("heinous acts here")
except TypeError as e:
    print(f"saved from a specific error: {e}")



try:
    print("heinous acts here")
except:
    print("saved")
else:
    print("lol no error im dooing good")



try:
    print("heinous acts here")
except:
    print("saved")
finally:
    print("idk if there was an error or if a value is returned what i do know is i dont give a shit (runs even if no exceptions)")


# raising errors
num = input("enter number")
already_taken = [1, 5, 6, 8, 7]
if num in already_taken:
    raise ValueError("value already occupied")