# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import collections as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_3():
    timer_0 = module_0.Timer()
    str_0 = "Timer is running. Use .stop() to stop it"
    timer_1 = module_0.Timer(text=str_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()
    timer_0.__exit__()


def test_case_4():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()


def test_case_5():
    str_0 = " f~\tCv>BoA/B@\tG9z"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()
    float_arg_0 = module_0.FloatArg()
    var_0 = timer_0.__repr__()


def test_case_6():
    bool_0 = False
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=bool_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()
    timer_0.stop()


def test_case_7():
    str_0 = "2/0I&o{D&V$5"
    timer_0 = module_0.Timer(str_0, str_0)
    timer_1 = module_0.Timer(timer_0, initial_text=timer_0)
    timer_2 = timer_1.__enter__()
    user_dict_0 = module_1.UserDict()
    var_0 = user_dict_0.__eq__(str_0)
    timer_0.setdefault(timer_0)
