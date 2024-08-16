from tree_build import *

iterate_limit = 4
 
def non_term_pos(data):
    result = []
    for count, v in enumerate(data):
        length = len(result)
        if v.isupper():
            if iterate_limit < length == count:
                return result
            else:
                result.append(count)
    return result

 
def derive_combined(node, data, key, count):  # derive combined- terminals and non-terminals
    value = rules.get(key)  # get values of key
    for i in value:
        i = TreeNode(data.replace(key, str(i),1))
        node.add_child(i)     
        res = non_term_pos(i.data)
        for t in res:    
                if count > iterate_limit:
                    return
                else:
                    derive_combined(i, i.data, i.data[t], count + 1)

def start_state(key):
    root = TreeNode(key)
    value = rules.get(key)  # get values of key
    for i in value:
        i = TreeNode(i)
        root.add_child(i)
        res = non_term_pos(i.data)
        for temp in res:
                derive_combined(i, i.data, i.data[temp], 0)
         

    return root