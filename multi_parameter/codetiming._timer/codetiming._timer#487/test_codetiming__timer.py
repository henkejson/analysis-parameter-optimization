# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    str_0 = "\x0b84a>"
    timer_0 = module_0.Timer(str_0)
    timer_1 = timer_0.__enter__()


def test_case_2():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer()
    var_0 = timer_0.__eq__(timer_0)
    var_1 = var_0.__repr__()
    timer_0.__exit__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_4():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_arg_0 = module_0.FloatArg()
    timer_error_1 = module_0.TimerError()
    timer_0.start()


def test_case_5():
    timer_error_0 = module_0.TimerError()
    none_type_0 = None
    timer_0 = module_0.Timer(text=none_type_0)
    str_0 = "1@{G%\nk=OW]?zb"
    timer_1 = module_0.Timer(initial_text=str_0)
    timer_1.start()


def test_case_6():
    bool_0 = True
    timer_0 = module_0.Timer(bool_0, initial_text=bool_0)
    none_type_0 = timer_0.start()
    str_0 = "Timer started"
    str_1 = '"CRg;WN'
    str_2 = "5*'@r<\tuNvW&}\t"
    dict_0 = {
        str_0: none_type_0,
        str_1: none_type_0,
        str_0: none_type_0,
        str_2: none_type_0,
    }
    module_0.FloatArg(**dict_0)


def test_case_7():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = None
    timer_2 = module_0.Timer(text=none_type_0)
    var_0 = timer_1.__call__(none_type_0)
    timer_3 = module_0.Timer(initial_text=timer_0)
    none_type_1 = timer_3.start()
    var_1 = timer_2.__repr__()
    module_0.FloatArg(*timer_2)


def test_case_8():
    str_0 = "\x0b84a>"
    timer_0 = module_0.Timer(str_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()


def test_case_9():
    timer_error_0 = module_0.TimerError()
    none_type_0 = None
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(timer_error_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    var_0 = module_1.dataclass(
        repr=timer_error_0, match_args=timer_error_0, kw_only=timer_error_0
    )
    var_1 = var_0.__repr__()
    var_1.pop(none_type_0)
