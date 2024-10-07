hashTable = [[], ] * 10

def check_prime(n):
    if n == 0 or n == 1:
        return 0
    
    for i in range(2, n // 2):
        if n % i == 0:
            return 0    
    return 1

def get_prime(n):
    if n % 2 == 0:
        n += 1
        
    while not check_prime(n):
        n += 2
    return n

def hash_function(key):
    cap = get_prime(10)
    return (key % cap)

def insert_data(key, data):
    index = hash_function(key)
    print(f"index: {index}")
    hashTable[index] = [key, data]

def remove_data(key):
    index = hash_function(key)
    hashTable[index] = 0

def main():
    insert_data(123, "Python")
    insert_data(456, "C++")
    insert_data(789, "JavaScript")
    insert_data(134, "Perl")

    print(hashTable)

    remove_data(789)

    print(hashTable)

if __name__ == '__main__':
    main()
