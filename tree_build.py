from pre_process import rules
from pre_process import err_log

epsilon = 'ε'
words_in_dict = {}
words_set = set()
err = set()  # error set
# look_up = []
paths = []


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

    def parent_getter(self, node):
        return node.parent

    def print_tree(self):
        if epsilon in self.data:
            str = f"{'  ' * self.get_level()}|--{self.data.replace(epsilon, '')}\n"
        else:
            if self.data in err_log and self.data.islower():
                str = f"{'  ' * self.get_level()}|--[{self.data}]\n"

            else:
                str = f"{'  ' * self.get_level()}|--{self.data}\n"
        print_getter(str)
        if self.children:
            for each in self.children:
                each.print_tree()

    def in_language(self):
        if self.children:  # traverse to tree leaves to the sentence
            for each in self.children:
                each.in_language()
        else:

            if self.data.islower():
                path = word_path(self)
                # rout = path.copy()
                if epsilon in self.data:
                    word = self.data.replace(epsilon, '')

                else:
                    word = self.data
                    path.pop()
                rout = path.copy()
                words_set.add(word)
                if word in words_in_dict.keys():
                    if sorted(words_in_dict.get(word)) == sorted(rout):
                        return None
                    else:
                        words_in_dict[word].append(rout)
                else:
                    words_in_dict[word] = [rout]

        #     print(f"\033[1;32m {self.data} \033[1;35m is ambiguous")


def print_dict():
    print()
    for key in words_in_dict.keys():
        for each in words_in_dict.get(key):
            for val in each:
                # print(f"\033[0m{val} -> ", end=" ")     ### color IDE
                print(f"{val} -> ", end=" ")    
            if key in err_log:
                # print(f"\033[1;31m {key} \033[0m\n", end="")
                print(f"{key}", end="")
            else:
                # print(f"\033[1;36m {key} \033[0m\n", end="")
                print(f"{key}", end="")
            print()

def word_path(node):  # helper bottom up route
    paths.clear()
    paths.append(node.data)
    leaf = node
    while leaf is not None:
        leaf = leaf.parent_getter(leaf)
        if leaf is None:
            break
        else:
            paths.append(leaf.data)
    paths.reverse()
    return paths


def path_to_file():
    f = open("paths.txt", "w")
    str = "           Words Paths         \n\n"
    f.write(str)
    for key in words_in_dict.keys():
        for each in words_in_dict.get(key):
            for val in each:
                if epsilon in val:
                    str = f"{val.replace(epsilon, '')}"
                else:
                    str = f"{val} -> "
                f.write(str)
            if str == key:
                str = f"\n"
            else:
                str = f"{key}\n"
            f.write(str)
            
    f.close()


def print_getter(str):
    f = open(f"Tree.txt", "a")
    f.write(str)
    f.close()
