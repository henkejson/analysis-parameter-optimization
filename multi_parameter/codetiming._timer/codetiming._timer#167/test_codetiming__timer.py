# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()
    timer_1 = timer_0.__enter__()
    none_type_2 = timer_1.__exit__()
    none_type_3 = timer_1.start()
    timer_1.start()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_0.__exit__()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_5():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_0.start()
    var_0 = timer_0.__repr__()
    float_0 = timer_0.stop()


def test_case_6():
    none_type_0 = None
    str_0 = "?oO'*6Wb%8rt:"
    timer_0 = module_0.Timer(text=none_type_0, initial_text=str_0)
    timer_1 = module_0.Timer(text=str_0)
    timer_2 = timer_1.__enter__()
    none_type_1 = timer_0.start()
    none_type_2 = timer_1.__exit__()
    str_0.start()


def test_case_7():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, float_arg_0, float_arg_0)
    timer_1 = timer_0.__enter__()
    timer_1.__enter__()


def test_case_8():
    none_type_0 = None
    str_0 = "?oO'*6Wb%8rt:"
    timer_0 = module_0.Timer(text=none_type_0, initial_text=str_0)
    timer_1 = module_0.Timer(timer_0, timer_0, none_type_0)
    timer_2 = timer_1.__enter__()
    none_type_1 = timer_0.start()
    timer_1.__exit__()


def test_case_9():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()
    timer_0.max(timer_0)


def test_case_10():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__()
    timer_0.max(timer_0)
