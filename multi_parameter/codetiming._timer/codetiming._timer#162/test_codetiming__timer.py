# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    str_0 = "R,6]"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()
    var_0 = timer_0.__repr__()
    timer_2 = timer_0.__enter__()
    timer_2.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_3():
    bool_0 = True
    timer_0 = module_0.Timer(bool_0, bool_0, bool_0, bool_0)
    timer_0.stop()


def test_case_4():
    str_0 = "R,6]"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_5():
    bytes_0 = b"\xee\xe2\x11\x05{[\xa9RBQ\xc4"
    timer_0 = module_0.Timer(initial_text=bytes_0)
    none_type_0 = timer_0.start()
    var_0 = timer_0.__repr__()
    var_1 = timer_0.__repr__()
    var_1.__call__(var_0)


def test_case_6():
    float_arg_0 = module_0.FloatArg()
    float_arg_1 = module_0.FloatArg()
    list_0 = [float_arg_0, float_arg_0, float_arg_0, float_arg_0]
    timer_0 = module_0.Timer(float_arg_0, initial_text=list_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = None
    timer_2 = module_0.Timer(text=timer_0, logger=none_type_0)
    timer_error_0 = module_0.TimerError()
    none_type_1 = None
    timer_3 = module_0.Timer(none_type_1, initial_text=none_type_1, logger=none_type_1)
    var_0 = timer_0.__repr__()


def test_case_7():
    bool_0 = False
    none_type_0 = None
    timer_0 = module_0.Timer(text=bool_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    float_arg_0 = module_0.FloatArg()
    var_0 = timer_0.__eq__(timer_0)
    none_type_1 = timer_0.__exit__()
    timer_0.stop()
