# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import collections as module_1


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    str_0 = "ba0"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    timer_1.__enter__()


def test_case_2():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    timer_1 = timer_0.__enter__()


def test_case_3():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    timer_0.stop()


def test_case_4():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    var_0 = timer_0.__enter__()
    float_0 = timer_0.stop()


def test_case_5():
    str_0 = "ba0"
    timer_0 = module_0.Timer(logger=str_0)
    var_0 = timer_0.__eq__(str_0)
    timer_0.__exit__()


def test_case_6():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, initial_text=none_type_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()
    none_type_0.__contains__(none_type_0)


def test_case_7():
    str_0 = "ba0"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(str_0, timer_0)
    timer_3 = timer_2.__enter__()
    float_0 = timer_3.stop()


def test_case_8():
    str_0 = "ba0"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()


def test_case_9():
    str_0 = "ba0"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    list_0 = [timer_1]
    none_type_0 = timer_1.__exit__(*list_0)
    timer_2 = timer_0.__enter__()
    float_0 = timer_1.stop()
    timer_3 = module_0.Timer(text=timer_1, initial_text=list_0)
    timer_4 = timer_3.__enter__()


def test_case_10():
    bytes_0 = b"$[\xea\x1b\xd0o\xed#"
    timer_0 = module_0.Timer(bytes_0, initial_text=bytes_0)
    var_0 = timer_0.__call__(bytes_0)
    var_1 = timer_0.__repr__()
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    module_1.UserDict(**var_1)
