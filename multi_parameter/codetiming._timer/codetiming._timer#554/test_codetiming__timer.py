# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import collections as module_1


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_0.stop()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_5():
    str_0 = "/4^A{)MNKOCzDD"
    timer_0 = module_0.Timer(str_0, str_0)
    none_type_0 = timer_0.start()
    timer_0.__exit__()


def test_case_6():
    bytes_0 = b'\xcf\xaf\xec^\xe2\xf7\xc8\xfb"\xb8\x94@7p\xfa\x9de\xfbd\xbd'
    str_0 = "NA#yUnEdkVF"
    timer_0 = module_0.Timer(bytes_0, str_0)
    none_type_0 = timer_0.start()
    var_0 = timer_0.__eq__(none_type_0)
    var_1 = timer_0.__eq__(bytes_0)
    float_0 = timer_0.stop()
    var_2 = var_1.__repr__()
    var_1.total(var_2)


def test_case_7():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=timer_error_0)
    none_type_0 = timer_0.start()


def test_case_8():
    bool_0 = True
    user_dict_0 = module_1.UserDict()
    var_0 = user_dict_0.__setitem__(bool_0, bool_0)
    timer_0 = module_0.Timer(var_0, var_0)
    int_0 = 60
    none_type_0 = None
    timer_1 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_1.start()
    var_1 = timer_1.__repr__()
    var_2 = timer_1.__eq__(var_1)
    none_type_2 = timer_1.__exit__()
    var_3 = var_1.__eq__(int_0)


def test_case_9():
    timer_0 = module_0.Timer()
    str_0 = "R"
    timer_1 = module_0.Timer(str_0, str_0, str_0)
    var_0 = timer_1.__call__(str_0)
    none_type_0 = None
    timer_2 = module_0.Timer(logger=none_type_0)
    timer_3 = timer_1.__enter__()
    timer_2.stop()


def test_case_10():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0)
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    none_type_0 = timer_0.__exit__()
    timer_2 = timer_0.__enter__()
    var_0.copy()
