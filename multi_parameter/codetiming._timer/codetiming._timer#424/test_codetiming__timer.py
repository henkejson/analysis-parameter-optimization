# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_2():
    timer_error_0 = module_0.TimerError()
    timer_error_1 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_1)
    timer_0.stop()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_4():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_5():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0)
    none_type_0 = timer_0.start()
    timer_0.start()


def test_case_6():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_0.start()
    int_0 = -8
    var_0 = timer_0.__eq__(int_0)
    timer_1 = module_0.Timer(text=int_0)
    var_0.stop()


def test_case_7():
    float_arg_0 = module_0.FloatArg()
    none_type_0 = None
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    var_0 = timer_0.__repr__()
    none_type_2 = var_0.__repr__()
    var_0.__setitem__(none_type_2, var_0)


def test_case_8():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    timer_error_0 = module_0.TimerError()
    none_type_1 = timer_1.__exit__()
    var_0 = timer_1.__repr__()
    none_type_0.__enter__()


def test_case_9():
    none_type_0 = None
    str_0 = "M&QK5n0"
    timer_0 = module_0.Timer(initial_text=str_0)
    none_type_1 = timer_0.start()
    timer_1 = module_0.Timer(text=none_type_0, initial_text=none_type_0)
    float_0 = timer_0.stop()
    var_0 = timer_0.__call__(none_type_0)
    var_1 = module_1.field(compare=none_type_0)
    timer_1.add(str_0, str_0)


def test_case_10():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0, logger=none_type_0)
    float_arg_0 = module_0.FloatArg()
    float_arg_1 = module_0.FloatArg()
    timer_1 = module_0.Timer(text=timer_0, initial_text=none_type_0)
    none_type_1 = timer_1.start()
    float_0 = timer_1.stop()
