from tree_build import *
from pre_process import *
from driver import run
from process import iterate_limit

def sentence_in_lanuange():
    f = open("cfg_log.txt", "w")
    f.write(f"sentences generated {iterate_limit} interations limit:\n")
    for i in sorted(sentence):
        f.write(f"{i} \n")
    f.close()
    print(sorted(sentence))

def error_log():
    if len(err_log) > 0:
        print(" ".join(str(x) for x in err_log))
