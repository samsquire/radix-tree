def common_substring(value1, value2):
    i = 0
    while i < len(value1) and i < len(value2):
        if value1[i] == value2[i]:
            i += 1
        else:
            break
    return (value1[0:i], i)

class NewRadix:
    def __init__(self, prefix, children, value=None):
        self.prefix = prefix
        self.children = children
        self.value = value

    def child_prefixes(self):
        for child in self.children:
            yield child
            yield from child.child_prefixes()

    def prefixes(self, prefix):
        found = None
        for child in self.children:
            if child.prefix == prefix:
                yield child
            if prefix.startswith(child.prefix):
                found = child
                break

        if found:
            yield from found.child_prefixes()



    def highest_prefix(self, prefix):
        highest = None
        common = None
        for child in self.children:
            if prefix.startswith(child.prefix):
                new_common = common_substring(prefix, child.prefix)
                if highest == None:
                    highest = child
                    common = new_common
                test, new_common = child.highest_prefix(prefix)
                if highest == None:
                    highest = test
                if test:
                    if len(test.prefix) > len(highest.prefix):
                        highest = test
                        common = new_common
        return highest, common

    def insert(self, prefix, value=None):
        # find the longest match where we belong
        highest_prefix, common = self.highest_prefix(prefix)
        if highest_prefix != None:
            common_substring, length = common
            new_item = NewRadix(prefix, value=value, children=[])
            highest_prefix.children.append(new_item)
        else:


            new_remainder = NewRadix(prefix, value=value, children=[])
            new_item = NewRadix(prefix[:1], value=None, children=[new_remainder])
            self.children.append(new_item)
