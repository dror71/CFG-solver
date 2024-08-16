from tree_build import *
from pre_process import rules, prepare_dict
from process import first_pass

rules_raw = dict(S="ε|1S1|0S0|T")
# rules_raw = dict(S="c|S|Sa")  |aA", A="b|C", C="ε")
# rules_raw = dict(S="c|S|Sa|ε|D")

key = 'S'  # S initial key


def run():
    prepare_dict(rules_raw)
    root = first_pass(key)
    root.print_tree()
    root.in_languange()

