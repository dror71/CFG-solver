from pre_process import prepare_dict, rules, err_log
from tree_build import *
from process import start_state
from driver import run
from util import *

if run() == 1:
    error_log()
else:
    words_in_language()
    #error_log()
