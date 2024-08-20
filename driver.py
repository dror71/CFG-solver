# from tree_build import *
from pre_process import rules, prepare_dict
from process import start_state
from util import clear_files

rules = {}
err_log = set()  # error log set

# rules_raw = dict(S="ε|1S1|0S0")
# rules_raw = dict(S="c|S|Sa |aA", A="b|C" , C="ε")
# rules_raw = dict(S="c|S|Sa|ε|D")
# rules_raw = dict(S="AB", A="aA|c", B="Bb|d")
# rules_raw=dict(S="A B", A="a A|c",B="B b|   d")
# rules_raw=dict(S="E", E="a  | [L] | []", L="E | E,L ")
rules_raw=dict(S="A", A="aA | B", B="aB | a")
# rules_raw=dict(S="A", A="aAb | bAa | AA | ab | ba")
# rules_raw=dict(S="aSc| T ", T="bTc | ε" )
# rules_raw=dict(S="A", A="(A)  | AA| ()  ")
# rules_raw=dict(S="A", A="aAa | B", B="bBb | c")
# rules_raw=dict(S="AB", A="aA  | c", B="bB | d")
# rules_raw=dict(S="A ", A="aAb  | aA | b ")
# rules_raw=dict(S="A ", A="aAb  | bAa  | AA  | ab | ba")
# rules_raw = dict(S="A ", A="aA  | B", B="aB |a")
# rules_raw = dict(S="aSb | T ", T="aTa | bTb | ε ")
key = 'S'  # S start state



def run():
    if prepare_dict(rules_raw) == 1:
        return 1
    else:
        clear_files()
        root = start_state(key)
        root.in_language()
        root.print_tree()
