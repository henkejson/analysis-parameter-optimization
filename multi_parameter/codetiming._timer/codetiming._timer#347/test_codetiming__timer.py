# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1
import codetiming._timers as module_2


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0)
    var_0 = timer_0.__enter__()
    timer_0.stop()


def test_case_2():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0)
    var_0 = timer_0.__eq__(none_type_0)
    timer_0.stop()


def test_case_3():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0)
    timer_0.__exit__()


def test_case_4():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    timer_1 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_5():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()
    timer_2 = module_0.Timer(initial_text=timer_0)
    none_type_1 = timer_2.start()
    var_0 = timer_0.__repr__()
    float_0 = 2365.222131
    timer_1.__setitem__(float_0, none_type_1)


def test_case_6():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    float_arg_0 = module_0.FloatArg()
    var_1 = var_0.__eq__(var_0)
    var_1.start()


def test_case_7():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__call__(timer_0)
    none_type_0 = timer_1.__exit__()
    timer_2 = module_0.Timer(var_0, var_0, var_0)
    none_type_1 = timer_2.start()
    none_type_2 = timer_1.start()
    timer_0.__enter__()


def test_case_8():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__repr__()
    var_0 = timer_0.__repr__()
    none_type_0 = var_0.__len__()
    timer_2 = module_0.Timer(initial_text=timer_1)
    timer_2.start()


def test_case_9():
    str_0 = "2mE!dC*gFlZ`.:U\rUQ_a"
    timer_0 = module_0.Timer(str_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    none_type_0 = None
    dict_0 = {str_0: none_type_0, str_0: none_type_0}
    var_0 = module_1.field(default_factory=none_type_0, compare=dict_0)
    timer_2 = timer_1.__enter__()
    var_0.__contains__(none_type_0)


def test_case_10():
    float_arg_0 = module_0.FloatArg()
    none_type_0 = None
    timer_0 = module_0.Timer(text=float_arg_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = None
    timers_0 = module_2.Timers()
    float_0 = timer_1.stop()
    timers_0.__ior__(none_type_1)


def test_case_11():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__call__(timer_0)
    none_type_0 = timer_1.__exit__()
    timer_2 = module_0.Timer(var_0, var_0, var_0)
    none_type_1 = timer_2.start()
    float_0 = timer_2.stop()
    none_type_2 = timer_1.start()
    module_1.field(init=timer_2, hash=none_type_2, metadata=timer_2, kw_only=var_0)
