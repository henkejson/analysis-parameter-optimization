# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import collections as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()


def test_case_2():
    str_0 = '1{\\*5q0$wu2P"S;Zz'
    list_0 = [str_0, str_0]
    timer_0 = module_0.Timer(str_0, logger=list_0)
    timer_0.__exit__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_4():
    float_arg_0 = module_0.FloatArg()
    list_0 = [float_arg_0, float_arg_0, float_arg_0]
    timer_0 = module_0.Timer(float_arg_0, float_arg_0, list_0)
    timer_1 = timer_0.__enter__()
    module_0.FloatArg(*list_0)


def test_case_5():
    int_0 = -3340
    str_0 = "\r\x0bK^"
    timer_0 = module_0.Timer(str_0, initial_text=int_0)
    str_1 = ""
    bytes_0 = b"\x174\x01Yy\xa8J\xe1\xbb]\\\xc1\xc6>"
    timer_1 = timer_0.__enter__()
    list_0 = [timer_0, bytes_0, str_1]
    none_type_0 = timer_1.__exit__(*list_0)
    user_dict_0 = module_1.UserDict()
    none_type_1 = timer_0.start()


def test_case_6():
    int_0 = -3340
    str_0 = "\r\x0bK^"
    timer_0 = module_0.Timer(str_0, initial_text=int_0)
    timer_1 = module_0.Timer()
    timer_2 = timer_0.__enter__()
    timer_2.__enter__()


def test_case_7():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_error_0 = module_0.TimerError()
    timer_1 = timer_0.__enter__()


def test_case_8():
    none_type_0 = None
    bool_0 = False
    timer_0 = module_0.Timer(none_type_0, initial_text=bool_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()
    var_0 = timer_0.__repr__()
    none_type_2 = timer_0.start()
    var_1 = timer_0.__repr__()
    timer_error_0 = module_0.TimerError()
    timer_0.__exit__(*none_type_2)


def test_case_9():
    str_0 = "\r\x0bK^"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    str_1 = ""
    bytes_0 = b"\x174\x01Yy\xa8J\xe1\xbb]\\\xc1\xc6>"
    timer_1 = timer_0.__enter__()
    list_0 = [timer_0, bytes_0, str_1]
    none_type_0 = timer_1.__exit__(*list_0)
    user_dict_0 = module_1.UserDict()
    none_type_1 = None
    var_0 = user_dict_0.__ror__(none_type_1)
    user_dict_0.get(list_0)
