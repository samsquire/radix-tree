from efficientradixtree import RadixTree2

root = RadixTree2()
root.insert("hello", 1)
root.insert("hellohullaba", 2)
root.insert("hellohullabasomething", 3)
root.insert("hellohullabasomesplit", 4)
root.insert("hellohullabasome", 5)


def walk(items, spaces = 0):
    for child in items:
        print(" " * spaces, child.key, child.value)
        walk(child.children, spaces + 1)

walk(root.children)

print("matches for hello")
for item in root.prefixes("hello"):
    print(item[0], item[1].value)

print("matches for hellohullaba")
for item in root.prefixes("hellohullaba"):
    print(item[0], item[1].value)

print("matches for hellohullabasome")
for item in root.prefixes("hellohullabasome"):
    print(item[0], item[1].value)
