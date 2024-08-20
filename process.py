from tree_build import *
from pre_process import err_log

iterate_limit = 1

look_up = []

def non_term_pos(data):
    result = []
    for count, v in enumerate(data):
        length = len(result)
        if v.isupper():
            if iterate_limit * 3 < length == count:
                return result
            else:
                result.append(count)
    return result

def derivation(node, data, key, count):         # derive non-terminals and non-terminals
    value = rules.get(key)                      # get values of key

    for i in value:

        if i.upper():
            i = TreeNode(data.replace(key, str(i), 1))
        else:
            i = TreeNode(str(i))

        if i.data in look_up:
            err_log.add(f"{i.data}")
            node.add_child(i)    # keep child registered for ambiguity
        else:
            look_up.append(i.data)
            node.add_child(i)
            for each in node.children:
                res = non_term_pos(each.data)
                for t in res:
                    if count > iterate_limit:
                        return
                    else:
                        derivation(each, each.data, each.data[t], count + 1)


def start_state(key):
    root = TreeNode(key)
    value = rules.get(key)  # get values of key
    for i in value:
        i = TreeNode(i)
        root.add_child(i)

    for each in root.children:

        res = non_term_pos(each.data)
        for temp in res:
            derivation(each, each.data, each.data[temp], 0)

    return root
