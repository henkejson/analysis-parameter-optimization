# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import collections as module_1
import builtins as module_2
import codetiming._timers as module_3


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    none_type_0 = None
    user_dict_0 = module_1.UserDict()
    var_0 = user_dict_0.__eq__(user_dict_0)
    var_1 = var_0.__eq__(var_0)
    var_2 = var_0.__eq__(none_type_0)
    timer_0 = module_0.Timer(var_2, initial_text=var_2)
    none_type_1 = timer_0.start()
    timer_0.start()


def test_case_2():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()


def test_case_3():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, initial_text=none_type_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__()


def test_case_4():
    str_0 = "g\x0cO|z+YD{kr+;U"
    timer_0 = module_0.Timer(logger=str_0)
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    var_1 = timer_1.__repr__()
    var_2 = var_0.__repr__()
    var_2.__enter__()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    timer_1 = timer_0.__enter__()
    timer_2 = timer_0.__call__(none_type_0)
    var_0 = timer_0.__repr__()
    var_1 = var_0.__repr__()
    timer_1.__enter__()


def test_case_6():
    none_type_0 = None
    none_type_1 = None
    timer_0 = module_0.Timer(none_type_1, initial_text=none_type_0)
    none_type_2 = timer_0.start()
    none_type_3 = timer_0.__exit__()
    timer_0.__exit__()


def test_case_7():
    base_exception_0 = module_2.BaseException()
    timer_0 = module_0.Timer(base_exception_0, initial_text=base_exception_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()
    base_exception_0.stop()


def test_case_8():
    str_0 = "i$z^4$\rdCNod:w?:"
    timer_0 = module_0.Timer(initial_text=str_0)
    none_type_0 = None
    user_dict_0 = module_1.UserDict()
    var_0 = user_dict_0.update()
    timer_1 = timer_0.__enter__()
    var_1 = var_0.__repr__()
    var_2 = var_1.__eq__(none_type_0)
    timers_0 = module_3.Timers()
    timer_2 = module_0.Timer(none_type_0)
    none_type_1 = timer_2.start()
    none_type_2 = timer_2.__exit__()
    var_3 = var_0.__eq__(none_type_0)
    var_4 = user_dict_0.values()
    var_4.pop(none_type_0)


def test_case_9():
    none_type_0 = None
    user_dict_0 = module_1.UserDict()
    var_0 = none_type_0.__eq__(none_type_0)
    var_1 = var_0.__eq__(user_dict_0)
    timer_0 = module_0.Timer(initial_text=var_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__()
    var_0.stop()


def test_case_10():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    timer_1.popitem()
