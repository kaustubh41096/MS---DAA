arr = []


def insert():
    f = open("small_data.txt", "r")
    contents = f.read()
    x = contents.split()
    for i in x:
        arr.append(int(i))


def search(num):
    for i in range(len(arr)):
        if num == arr[i]:
            return True
    return False


def linear_search():
    insert()
    if search(345):
        return 20
    else:
        return 10
