from pre_process import rules

epsilon = 'ε'
sentence = set()
err = set()  # error set


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.child = child
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level

    def print_tree(self):
        print('  ' * self.get_level() + '|--', end='')
        if epsilon in self.data:
            print(self.data.replace(epsilon, ''))
        else:
            print(self.data)
        if self.children:
            for each in self.children:
                each.print_tree()

    def in_languange(self):
        if self.children:  # travrese to tree leaves to the sentence
            for each in self.children:
                each.in_languange()
        else:
            if self.data.islower():
                if epsilon in self.data:
                    sentence.add(self.data.replace(epsilon, ''))
                else:
                    sentence.add(self.data)

        return sorted(sentence)
