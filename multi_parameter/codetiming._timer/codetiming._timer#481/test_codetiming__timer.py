# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    bool_0 = True
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=bool_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()
    timer_1 = module_0.Timer(initial_text=bool_0)
    none_type_2 = timer_1.start()
    timer_1.start()


def test_case_2():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_0.start()


def test_case_3():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    timer_0.__exit__()


def test_case_4():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()


def test_case_5():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = timer_0.__enter__()


def test_case_6():
    bool_0 = True
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=bool_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    timer_1 = module_0.Timer(initial_text=bool_0)
    none_type_2 = timer_1.start()


def test_case_7():
    bool_0 = False
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = module_0.Timer()
    none_type_0 = timer_1.start()


def test_case_8():
    str_0 = "o2;Y0b 2 \\(:2"
    timer_0 = module_0.Timer(initial_text=str_0)
    list_0 = []
    timer_1 = timer_0.__enter__()
    str_0.__setitem__(list_0, list_0)


def test_case_9():
    bool_0 = True
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=bool_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()
    timer_1 = module_0.Timer(initial_text=bool_0)
    none_type_2 = timer_1.start()


def test_case_10():
    bool_0 = True
    timer_0 = module_0.Timer(bool_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()


def test_case_11():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0, logger=float_arg_0)
    timer_0.start()


def test_case_12():
    bool_0 = True
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_1 = timer_0.start()
    set_0 = set()
    var_0 = module_1.dataclass(init=none_type_0, frozen=none_type_1, match_args=timer_0)
    timer_1 = module_0.Timer(text=timer_0)
    timer_2 = timer_1.__enter__()
    none_type_2 = timer_2.__exit__()
    timer_3 = module_0.Timer(text=set_0, initial_text=bool_0, logger=var_0)
