from radixtree import NewRadix

root = NewRadix("", children=[NewRadix("h", children=[NewRadix("hello", children=[])])])

root.insert("hellohello", None)

items = list(root.prefixes("h"))
for item in items:
    print("h match")
    print(item.prefix)
    
root.insert("bumf", None)


items = list(root.prefixes("bumf"))
for item in items:
    print("bumf match")
    print(item.prefix)

