# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    float_0 = -987.805
    timer_0 = module_0.Timer(initial_text=float_0)
    timer_1 = timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()
    timer_1.stop()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_5():
    float_0 = -3460.80189
    timer_0 = module_0.Timer(initial_text=float_0)
    timer_1 = timer_0.__enter__()
    timer_1.start()


def test_case_6():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    var_0 = timer_0.__eq__(none_type_0)
    none_type_1 = timer_0.start()
    float_arg_0 = module_0.FloatArg()
    var_1 = timer_0.__repr__()


def test_case_7():
    float_0 = -987.805
    timer_0 = module_0.Timer(initial_text=float_0)
    str_0 = "A/B=m_'QO%,oQQUH\" ><"
    timer_1 = module_0.Timer(str_0, timer_0)
    timer_2 = timer_1.__enter__()
    none_type_0 = timer_2.__exit__()


def test_case_8():
    none_type_0 = None
    none_type_1 = None
    timer_0 = module_0.Timer(initial_text=none_type_1, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    none_type_2 = timer_0.__exit__()
    timer_0.__iter__()


def test_case_9():
    float_0 = -984.0219108217357
    str_0 = "Tf&sY2_n8eZ"
    timer_0 = module_0.Timer(text=float_0, initial_text=str_0)
    timer_1 = timer_0.__enter__()
    int_0 = -1496
    list_0 = [int_0]
    timer_1.__exit__(*list_0)


def test_case_10():
    float_0 = -3460.80189
    timer_0 = module_0.Timer(float_0, initial_text=float_0)
    timer_1 = timer_0.__enter__()
    str_0 = "seconds"
    timer_2 = module_0.Timer(timer_0, str_0, str_0, str_0)
    var_0 = timer_1.__repr__()
    timer_2.__exit__()
