
print("okay so from what i have read there are four types of (arrays basically) in python")

def showcase_list():
    list = ["listitem1", "listitem2", "listitem3"]
    print("a list is defined like ", list)

    print("iteration over an list")
    for item in list:
        print(item)

    print("\nlists are mutable, indexed(starting 0), allows duplicates")


def showcase_tuples():
    tuple = ("tupleitem1", "tupleitem2", "tupleitem3")
    print("a tuple is defined like ", tuple)

    print("iteration over an tuple")
    for item in tuple:
        print(item)

    print("\ntuples are immutable(excludes children & indexes), indexed(starting 0), allows duplicates ")


def showcase_set():
    set = {"setitem1", "setitem2", "setitem3"}
    print("a tuple is defined like ", set)

    print("iteration over an array set")
    for item in set:
        print(item)

    print("\nset are immutable(methods work), unindexed(loops or `in`), denys duplicates ")

def showcase_dict():
    dict = {
        "name1": "item1",
        "name2": "item2",
        "name3":"item3"
    }
    print("a dict is defined like ", dict)

    print("iteration over an array set")
    for item in dict:
        print(item)

    print("\nset are mutable, only indexed in > v3.7, no duplicates at same index")



print("\n\n")
showcase_list()
print("\n\n")
showcase_tuples()
print("\n\n")
showcase_set()
print("\n\n")
showcase_dict()

