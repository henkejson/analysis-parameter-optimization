# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = None
    timer_2 = module_0.Timer(timer_0, logger=none_type_0)
    var_0 = timer_2.__call__(timer_2)
    float_0 = timer_0.stop()
    timer_3 = timer_2.__enter__()
    timer_4 = timer_0.__enter__()
    timer_0.start()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_3():
    none_type_0 = None
    bool_0 = True
    timer_0 = module_0.Timer(none_type_0, bool_0, bool_0)
    timer_0.stop()


def test_case_4():
    none_type_0 = None
    bool_0 = True
    timer_0 = module_0.Timer(none_type_0, bool_0, bool_0)
    none_type_1 = timer_0.start()


def test_case_5():
    float_arg_0 = module_0.FloatArg()
    str_0 = "&V {"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_0.__enter__()


def test_case_6():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0)
    timer_1 = module_0.Timer()
    timer_2 = timer_1.__enter__()
    timer_3 = timer_0.__enter__()
    float_0 = timer_0.stop()


def test_case_7():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    none_type_1 = timer_0.start()
    timer_2 = module_0.Timer(text=none_type_0, initial_text=none_type_0)
    float_arg_0 = module_0.FloatArg()
    none_type_2 = timer_2.start()
    float_arg_1 = module_0.FloatArg()
    timer_2.__enter__()
