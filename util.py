from tree_build import *
from pre_process import *
from driver import run
from process import iterate_limit

def words_in_lanuange():
    f = open("cfg_log.txt", "w")
    f.write(f"sentences generated {iterate_limit} interations limit:\n")
    print("Ambiguous")
    for i in sorted(sentence):

        if i in err_log:
            print(f"[{i}]", end=" ")
            f.write(f"{i}        ambiguous\n")
        else:
            print(f"{i}", end=" ")
            f.write(f"{i} \n")
    f.close()
    
def error_log():
    if len(err_log) > 0:
        print(" ".join(str(x) for x in err_log))
