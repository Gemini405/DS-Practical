def display_hash(hash_table):
    for i in range(10):
        print(i, end=" ")

        for j in hash_table[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


ExampleHashTable = [[] for _ in range(10)]

def hashing(key):
    return (key % len(ExampleHashTable))

def insert_hash(hash_table, key, value):
    hash_key = hashing(key)
    hash_table[hash_key].append(value)

# Example:
insert_hash(ExampleHashTable, 11, "Jeremy")
insert_hash(ExampleHashTable, 11, "Lissa")
insert_hash(ExampleHashTable, 19, "Martin")
insert_hash(ExampleHashTable, 5, "Manny")
insert_hash(ExampleHashTable, 17, "Niko")
insert_hash(ExampleHashTable, 9, "Arthur")

display_hash(ExampleHashTable)
