# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__call__(timer_0)
    timer_1 = timer_0.__enter__()
    timer_0.start()


def test_case_2():
    timer_error_0 = module_0.TimerError()
    bool_0 = False
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer()
    timer_0.stop()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer()
    float_0 = timer_0.stop()
    timer_3 = module_0.Timer()
    var_0 = timer_0.__repr__()
    float_arg_0 = module_0.FloatArg()


def test_case_5():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()
    var_1 = timer_0.__repr__()
    var_2 = timer_0.__eq__(timer_0)
    var_3 = var_2.__eq__(var_2)
    timer_0.stop()


def test_case_6():
    str_0 = "cyI!,JNV\x0b\x0c{E-XnN@[OW"
    timer_0 = module_0.Timer(str_0)
    none_type_0 = timer_0.start()
    timer_error_0 = module_0.TimerError()
    float_arg_0 = module_0.FloatArg()
    bool_0 = False
    var_0 = timer_0.__repr__()
    timer_1 = module_0.Timer(initial_text=str_0)
    var_1 = timer_0.__eq__(bool_0)
    float_0 = timer_0.stop()
    var_1.__exit__(*var_0)


def test_case_7():
    dict_0 = {}
    timer_0 = module_0.Timer(logger=dict_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = None
    none_type_1 = None
    bytes_0 = b"\x88\x1c\xb1\x95\\\xbf\xfc\xea\xf1\x8c+C"
    complex_0 = -1403.392 + 2487.036j
    var_0 = module_1.dataclass(
        eq=none_type_1, frozen=bytes_0, match_args=complex_0, slots=none_type_1
    )
    var_0.__delitem__(none_type_0)


def test_case_8():
    timer_error_0 = module_0.TimerError()
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()


def test_case_9():
    str_0 = "cyI!,JNV\x0b\x0c{E-XnN@[OW"
    timer_error_0 = module_0.TimerError()
    bool_0 = False
    timer_0 = module_0.Timer(initial_text=str_0)
    var_0 = timer_0.__eq__(bool_0)
    list_0 = []
    timer_error_1 = module_0.TimerError(*list_0)
    timer_0.__enter__()


def test_case_10():
    str_0 = "yI!,JNV\x0b\x0c{E-XnN@[OW"
    list_0 = [str_0, str_0, str_0]
    timer_error_0 = module_0.TimerError(*list_0)
    timer_error_1 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=str_0)
    list_1 = []
    var_0 = timer_0.__eq__(timer_error_1)
    timer_error_2 = module_0.TimerError(*list_1)
    bool_0 = True
    timer_1 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_1.start()
    timer_error_3 = module_0.TimerError()
    float_0 = timer_1.stop()
    none_type_1 = None
    timer_2 = module_0.Timer(initial_text=timer_error_2, logger=none_type_1)
    var_1 = timer_2.__repr__()
    timer_3 = timer_2.__enter__()
    var_2 = timer_2.__eq__(list_0)
    none_type_2 = timer_2.__exit__()
    var_3 = var_1.__repr__()
    var_3.apply(var_3, str_0)


def test_case_11():
    str_0 = "yI!,JNV\x0b\x0c{E-XnN@[OW"
    list_0 = [str_0, str_0, str_0]
    dict_0 = {}
    timer_error_0 = module_0.TimerError(**dict_0)
    timer_error_1 = module_0.TimerError(*list_0)
    timer_error_2 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=str_0)
    list_1 = []
    var_0 = timer_0.__eq__(timer_error_2)
    timer_error_3 = module_0.TimerError(*list_1)
    timer_1 = module_0.Timer(var_0, initial_text=timer_error_1)
    none_type_0 = timer_1.start()
    timer_error_4 = module_0.TimerError()
    var_0.__len__()


def test_case_12():
    str_0 = "cyI!,JNV\x0b\x0c{E-XnN@[OW"
    list_0 = [str_0]
    timer_error_0 = module_0.TimerError(*list_0)
    timer_error_1 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=str_0)
    var_0 = timer_0.__eq__(timer_error_1)
    timer_error_2 = module_0.TimerError()
    timer_1 = module_0.Timer(text=timer_0, logger=var_0)
    none_type_0 = timer_1.start()
    timer_1.stop()
