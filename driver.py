from tree_build import *
from pre_process import rules, prepare_dict
from process import start_state
import os

rules = {}
err_log = set()  # error log set

# rules_raw = dict(S="ε|1S1|0S0|T")
# rules_raw = dict(S="c|S|Sa")  |aA", A="b|C", C="ε")
# rules_raw = dict(S="c|S|Sa|ε|D")
#rules_raw = dict(S="a|SA", A="AA|c")
#rules_raw = dict(S="aSa|A", A="bA| b|ε")
# rules_raw=dict(S="A", A="(A)  | AA| ()  ")
#rules_raw=dict(S="A ", A="aA  | B", B="aB |a")
rules_raw = dict(S="AB", A="aA|c", B="Bb|d")
key = 'S'  # S start state


def run():
    if prepare_dict(rules_raw) == 1:
        return 1
    else:
        root = start_state(key)
        root.in_languange()
        if os.path.exists("Tree.txt"):
            os.remove("Tree.txt")
        root.print_tree()