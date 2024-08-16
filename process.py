
from tree_build import *



iterate_limit = 3

def non_term_pos(data):
    result = [b for b, v in enumerate(data) if v.isupper()]
    return result


def derive_non(node, key, count):                # derive non terminals
    value = rules.get(key)                       # get values of key
    for i in value:
        i = TreeNode(str(i))
        node.add_child(i)
        if i.data.isupper():
            if i.data in rules:
                if count > iterate_limit:
                    return
                else:
                    derive_non(i, i.data, count + 1)


def derive_combined(node, data, key, count):  # derive combined- terminals and non-terminals
    value = rules.get(key)  # get values of key
    for i in value:
        i = TreeNode(data.replace(key, str(i)))
        node.add_child(i)
        if (not i.data.isupper() and not i.data.islower()) or i.data.isalnum():
            res = non_term_pos(i.data)
            for t in res:
                if i.data[t] in rules:
                    if count > iterate_limit:
                        return
                    else:
                        derive_combined(i, i.data, i.data[t], count + 1)
                else:
                    err.add(i.data[t])
        if i.data.isupper():
            if i.data in rules:
                if count > iterate_limit:
                    return
                else:
                    derive_combined(i, i.data, key, count + 1)


def first_pass(key):
    root = TreeNode(key)
    value = rules.get(key)            # get values of key
    for i in value:
        i = TreeNode(i)
        root.add_child(i)
        if (not i.data.isupper() and not i.data.islower()) or i.data.isalnum():
            res = non_term_pos(i.data)
            for t in res:
                if i.data[t] in rules:
                    derive_combined(i, i.data, i.data[t], 0)
                else:
                    err.add(i.data[t])

        if i.data.isupper():
            if i.data in rules:
                derive_non(i, i.data, 0)

    return root