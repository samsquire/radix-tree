class RadixTree2:
    def __init__(self, key=None, value=None, is_leaf=False):
        self.children = []
        self.key = key
        self.value = value
        self.is_leaf = is_leaf

    def common_substring(self, value1, value2):
        i = 0
        while i < len(value1) and i < len(value2):
            if value1[i] == value2[i]:
                i += 1
            else:
                break
        return (value1[0:i], i)

    def descend(self, path=""):
        for child in self.children:
            if child.is_leaf:
                yield path + child.key, child
            yield from child.descend(path + child.key)

    def prefixes(self, prefix, path=""):
        for child in self.children:
            common, mismatching_index = self.common_substring(child.key, prefix)
            mismatching_string = prefix[mismatching_index:]

            if common and mismatching_string:
                yield from child.prefixes(mismatching_string, path=path + child.key)
            elif not mismatching_string:
                # we can descend mercilessly
                if child.is_leaf:
                    yield path + child.key, child
                yield from child.descend(path + child.key)

    def insert(self, key, value):
        if not self.children:
            self.children.append(RadixTree2(key, value, True))
            return True
        for child in self.children:
            common, index_where_mismatch_begins = self.common_substring(child.key, key)
            mismatching_string = key[index_where_mismatch_begins:]





            if child.key != common:

                split_parent = RadixTree2(common, None, False)
                new_child_common, child_different_index = self.common_substring(child.key, common)
                child_mismatching_string = child.key[child_different_index:]
                split_parent.children.append(RadixTree2(child_mismatching_string, child.value, True))
                split_parent.children.append(RadixTree2(mismatching_string, value, True))
                self.children.append(split_parent)
                self.children.remove(child)

            elif mismatching_string:

                success = child.insert(mismatching_string, value)
                if success:
                    break
            elif not mismatching_string:

                child.value = value
                child.is_leaf = True
                return True


        return False


