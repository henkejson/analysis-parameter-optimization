# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    str_0 = "^"
    timer_0 = module_0.Timer(str_0, str_0, str_0)
    timer_1 = timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_0.stop()


def test_case_3():
    str_0 = "^"
    timer_0 = module_0.Timer(str_0, str_0, str_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_4():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    float_arg_0 = module_0.FloatArg()
    var_0 = timer_0.__repr__()
    var_1 = timer_0.__repr__()
    float_arg_1 = module_0.FloatArg()
    none_type_1 = timer_0.start()
    var_1.__exit__()


def test_case_5():
    str_0 = "^"
    timer_0 = module_0.Timer(str_0, str_0, str_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_6():
    str_0 = "^"
    timer_0 = module_0.Timer(str_0, str_0, str_0)
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__call__(timer_0)
    float_0 = timer_0.stop()
    timer_2 = timer_0.__enter__()
    timer_3 = module_0.Timer(initial_text=timer_2)
    timer_4 = timer_3.__enter__()
    var_0.__call__(timer_0)


def test_case_7():
    timer_0 = module_0.Timer()
    bool_0 = False
    timer_1 = timer_0.__enter__()
    none_type_0 = None
    var_0 = timer_0.__call__(none_type_0)
    var_1 = module_1.dataclass(init=bool_0, eq=bool_0, frozen=bool_0)
    float_0 = timer_0.stop()
    timer_error_0 = module_0.TimerError()
    var_1.__exit__()


def test_case_8():
    str_0 = "^"
    timer_0 = module_0.Timer(str_0, str_0, str_0)
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    var_0 = timer_1.__call__(float_arg_0)
    timer_2 = module_0.Timer(initial_text=var_0)
    timer_3 = timer_2.__enter__()
    timer_1.stop()


def test_case_9():
    str_0 = "^"
    none_type_0 = None
    timer_0 = module_0.Timer(str_0, logger=none_type_0)
    var_0 = timer_0.__repr__()
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    var_1 = var_0.__contains__(var_0)
    var_1.start()


def test_case_10():
    str_0 = "^"
    timer_0 = module_0.Timer(str_0, str_0, str_0)
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(str_0, initial_text=timer_0)
    float_0 = timer_0.stop()
    timer_3 = timer_2.__enter__()
    none_type_0 = timer_2.__exit__()
    timer_4 = module_0.Timer(initial_text=timer_2, logger=timer_3)
    timer_5 = timer_3.__enter__()
    var_0 = timer_5.__call__(none_type_0)
    var_1 = timer_0.__call__(float_arg_0)
    var_2 = var_1.__eq__(timer_3)
    var_3 = var_2.__repr__()
    var_2.stop()


def test_case_11():
    str_0 = "^"
    timer_0 = module_0.Timer(str_0, str_0, str_0)
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(timer_1, timer_0, logger=float_arg_0)
    float_0 = timer_0.stop()
    timer_3 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()
    timer_4 = module_0.Timer(initial_text=timer_3)
    timer_5 = timer_4.__enter__()
    var_0 = timer_2.__call__(timer_0)
    timer_6 = module_0.Timer(none_type_0, initial_text=none_type_0)
    var_0.__call__(timer_2)
