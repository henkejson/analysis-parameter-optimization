# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import collections as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    timer_0.__exit__()


def test_case_3():
    str_0 = "|7/#Hv_"
    timer_0 = module_0.Timer(text=str_0, initial_text=str_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_5():
    timer_error_0 = module_0.TimerError()
    bytes_0 = b"\x14\xa6\x07\x8e"
    bytes_1 = b'Li\xaa\x04\x05\xa1\xc6\xb0\x13\xda\n\x85T"'
    timer_error_1 = module_0.TimerError()
    timer_0 = module_0.Timer(bytes_1, initial_text=bytes_0)
    var_0 = timer_0.__call__(bytes_1)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    none_type_0 = timer_0.start()
    user_dict_0 = module_1.UserDict()
    timer_0.__enter__()


def test_case_6():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=timer_error_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    none_type_0 = timer_0.start()
    user_dict_0 = module_1.UserDict()
    timer_1.__enter__()


def test_case_7():
    timer_error_0 = module_0.TimerError()
    bytes_0 = b"\x14\xa6\x07\x8e"
    int_0 = -2809
    none_type_0 = None
    str_0 = "|7/#Hv_"
    timer_0 = module_0.Timer(none_type_0, initial_text=str_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    str_1 = "aJ]/>Bz]@2>"
    str_2 = "QrE0w{VvI\nw\x0b8lA)s9#:"
    int_1 = -3910
    dict_0 = {str_1: int_0, str_2: bytes_0, str_1: int_1, str_1: float_0}
    user_dict_0 = module_1.UserDict(**dict_0)
    user_dict_0.__ior__(none_type_0)


def test_case_8():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=timer_error_0)
    timer_1 = module_0.Timer(initial_text=timer_error_0)
    timer_2 = timer_0.__enter__()
