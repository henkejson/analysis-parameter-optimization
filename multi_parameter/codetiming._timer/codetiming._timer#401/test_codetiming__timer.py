# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()


def test_case_2():
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=none_type_0)
    timer_0.__exit__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_1.__enter__()


def test_case_4():
    float_arg_0 = module_0.FloatArg()
    str_0 = "\x0csJqQN>lwk->5$_K2"
    none_type_0 = None
    timer_0 = module_0.Timer(str_0, str_0, logger=none_type_0)
    timer_1 = module_0.Timer(none_type_0)
    none_type_1 = timer_0.start()
    var_0 = timer_0.__eq__(timer_0)
    var_1 = timer_0.__repr__()
    none_type_2 = timer_0.__exit__()
    var_0.get(str_0, none_type_0)


def test_case_5():
    float_arg_0 = module_0.FloatArg()
    str_0 = "#name"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    timer_2 = timer_1.__eq__(float_arg_0)


def test_case_6():
    float_arg_0 = module_0.FloatArg()
    str_0 = "name"
    timer_error_0 = module_0.TimerError(*str_0)
    float_arg_1 = module_0.FloatArg()
    timer_0 = module_0.Timer()
    bool_0 = True
    timer_1 = module_0.Timer(text=float_arg_0, initial_text=bool_0)
    timer_2 = timer_1.__enter__()
    timer_2.__enter__()


def test_case_7():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer(timer_0, initial_text=timer_0)
    none_type_0 = timer_1.__call__(timer_0)
    var_0 = timer_1.__eq__(timer_0)
    timer_2 = timer_1.__enter__()
    none_type_1 = timer_0.start()
    var_0.clear()
