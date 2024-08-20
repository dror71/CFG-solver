from tree_build import *
from process import iterate_limit
import os


def words_in_language():
    f = open("cfg_log.txt", "w")
    f.write(f"sentences generated {iterate_limit} interations limit:\n")
    #print(f"\033[1;31m Ambiguous")           #color IDE
    print(f"Ambiguous")
    for i in sorted(words_set):
        if i in err_log:
            # print(f"\033[1;31m {i}", end=" ")     #color IDE
            print(f"{i}", end=" ")
            f.write(f"[{i}]        ambiguous\n")
        else:
            # print(f"\033[1;36m {i}\033[0m", end=" ")     #color IDE
            print(f"{i}", end=" ")
            f.write(f"{i} \n")
    f.close()
    print_dict()
    path_to_file()

    # print(f"\033[0m {sorted(sentence)} ")


def error_log():
    if len(err_log) > 0:
        print(" ".join(str(x) for x in err_log))


def clear_files():

    if os.path.exists("Tree.txt"):
        os.remove("Tree.txt")
