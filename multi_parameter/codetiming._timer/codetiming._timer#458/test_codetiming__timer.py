# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    bytes_0 = b"\x04\x04\xe2\xa2\t\x02\xd3\xeb{grj\x16\n#k\x90\xe6"
    timer_0 = module_0.Timer(initial_text=bytes_0)
    none_type_0 = timer_0.start()
    timer_0.start()


def test_case_2():
    timer_error_0 = module_0.TimerError()
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_0.start()


def test_case_3():
    str_0 = "wV7Ue[P:6Rxtz"
    str_1 = "HwFZH*0/buBgid%8eX=&"
    timer_0 = module_0.Timer(text=str_0, initial_text=str_1)
    none_type_0 = timer_0.start()
    none_type_1 = None
    timer_1 = module_0.Timer(none_type_1)
    timer_1.stop()


def test_case_4():
    str_0 = "wV7Ue[P:6Rxtz"
    timer_0 = module_0.Timer(text=str_0, initial_text=str_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    timer_1 = timer_0.__enter__()
    timer_error_0 = module_0.TimerError()
    float_0 = timer_0.stop()


def test_case_6():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0)
    timer_1 = timer_0.__enter__()
    timer_0.__exit__()


def test_case_7():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__()
    var_0 = module_1.dataclass()
    var_1 = var_0.__repr__()
    var_1.__exit__()


def test_case_8():
    str_0 = "=14Wwf"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_error_0 = module_0.TimerError()
    timer_1 = timer_0.__enter__()
    var_0 = timer_1.__repr__()
    none_type_0 = timer_0.__exit__(*var_0)
    var_0.__getitem__(var_0)


def test_case_9():
    float_arg_0 = module_0.FloatArg()
    str_0 = '"F@`E@?X?U;J`0\n'
    timer_0 = module_0.Timer(float_arg_0, float_arg_0, float_arg_0)
    var_0 = timer_0.__repr__()
    list_0 = [str_0, str_0, str_0]
    list_1 = [timer_0, list_0, float_arg_0]
    timer_1 = timer_0.__enter__()
    timer_0.__exit__(*list_1)
