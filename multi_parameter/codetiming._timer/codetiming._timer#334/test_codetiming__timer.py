# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    timer_error_0 = module_0.TimerError()
    var_0 = timer_0.__call__(timer_error_0)
    timer_1 = module_0.Timer(none_type_0)
    timer_2 = timer_0.__enter__()
    timer_2.__enter__()


def test_case_2():
    str_0 = "lS6~\t+ :,t]]dF|}cP"
    timer_0 = module_0.Timer(str_0, logger=str_0)
    timer_1 = timer_0.__enter__()


def test_case_3():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    timer_0.stop()


def test_case_4():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    timer_1.__exit__()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=none_type_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    timer_1.stop()


def test_case_6():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.__eq__(timer_0)


def test_case_7():
    str_0 = "Timer {name} started"
    timer_0 = module_0.Timer(initial_text=str_0)
    none_type_0 = timer_0.start()
    var_0 = module_1.dataclass()
    var_0.__len__()


def test_case_8():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    timer_1 = module_0.Timer(float_arg_0)
    timer_2 = timer_1.__enter__()
    float_0 = timer_1.stop()
    timer_1.stop()


def test_case_9():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0, logger=float_arg_0)
    timer_0.__enter__()


def test_case_10():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer()
    var_0 = timer_0.__repr__()
    var_1 = var_0.__eq__(float_arg_0)
    timer_1 = module_0.Timer(initial_text=float_arg_0)
    tuple_0 = (timer_1,)
    timer_2 = module_0.Timer(text=timer_1, logger=tuple_0)
    timer_3 = timer_2.__enter__()
    timer_3.stop()
