import pickle

islandData = {"population": 420, "haveTheyBeenFound": False}

# serialise and write
with open("./gobblegobble.dat", "r+b") as file:
    pickle.dump(islandData, file)


# deserialise
with open("./gobblegobble.dat", "r+b") as file:
    written_shit = pickle.load(file)
    print(written_shit)

