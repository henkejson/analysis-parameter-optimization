# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    int_0 = 3118
    timer_0 = module_0.Timer(initial_text=int_0)
    timer_1 = timer_0.__enter__()
    timer_1.start()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_3():
    int_0 = 3120
    timer_0 = module_0.Timer(initial_text=int_0)
    timer_0.__exit__()


def test_case_4():
    int_0 = 3120
    timer_0 = module_0.Timer(initial_text=int_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = timer_0.__exit__()


def test_case_6():
    int_0 = 3120
    timer_0 = module_0.Timer(initial_text=int_0)
    timer_1 = timer_0.__enter__()


def test_case_7():
    int_0 = 3120
    str_0 = "Lgh9#&*7"
    timer_0 = module_0.Timer(str_0, initial_text=int_0)
    none_type_0 = None
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(str_0)
    var_0 = timer_1.__eq__(none_type_0)
    var_0.__len__()


def test_case_8():
    str_0 = "L"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()
    var_0 = module_1.field(metadata=str_0)
    var_0.__call__(timer_1)


def test_case_9():
    int_0 = 3141
    timer_0 = module_0.Timer(initial_text=int_0)
    none_type_0 = None
    timer_1 = module_0.Timer(none_type_0)
    timer_2 = timer_0.__enter__()
    bool_0 = False
    timer_3 = module_0.Timer(text=timer_1, initial_text=bool_0)
    var_0 = timer_3.__call__(timer_2)
    var_1 = var_0.__call__(none_type_0)
    none_type_1 = timer_2.__exit__()
    timer_0.__exit__()


def test_case_10():
    int_0 = 3154
    none_type_0 = None
    timer_0 = module_0.Timer(int_0, initial_text=none_type_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = timer_0.__exit__()
    float_arg_0 = module_0.FloatArg()
