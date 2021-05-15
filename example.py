from radixtree import NewRadix

root = NewRadix("", children=[NewRadix("h", children=[NewRadix("hello", children=[])])])

root.insert("hellohello", None)
root.insert("hellohellohello", None)

items = list(root.prefixes("h"))
for item in items:
    print("h match")
    print(item.prefix)

root.insert("bumf", None)


items = list(root.prefixes("bumf"))
for item in items:
    print("bumf match")
    print(item.prefix)

items = list(root.prefixes("b"))
for item in items:
    print("b match")
    print(item.prefix)

def walk(item, spaces=0):
    for child in item:
        print(" " * spaces, child.prefix)
        walk(child.children, spaces + 1)

items = list(root.prefixes("hellohello"))
for item in items:
    print("hellohello match")
    print(item.prefix)

walk(root.children)
