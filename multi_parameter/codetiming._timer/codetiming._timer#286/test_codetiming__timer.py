# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import collections as module_1
import dataclasses as module_2


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()
    timer_0.start()


def test_case_2():
    str_0 = " >%UnjvA[-6d@%K_"
    timer_0 = module_0.Timer(str_0, str_0, str_0)
    timer_1 = timer_0.__enter__()
    float_arg_0 = module_0.FloatArg()
    var_0 = timer_0.__eq__(str_0)
    var_0.__call__(var_0)


def test_case_3():
    str_0 = " Y%UnjvA[-6d%K_"
    timer_0 = module_0.Timer(str_0, str_0, str_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    timer_1.stop()


def test_case_4():
    dict_0 = {}
    timer_0 = module_0.Timer(initial_text=dict_0)
    str_0 = " >%UnjvA[-6d@%K_"
    timer_1 = module_0.Timer(str_0, str_0, str_0)
    timer_2 = timer_1.__enter__()
    float_arg_0 = module_0.FloatArg()
    var_0 = timer_1.__call__(float_arg_0)
    none_type_0 = timer_1.__exit__()
    var_1 = timer_2.__repr__()
    timer_1.__exit__()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
    none_type_1 = timer_0.start()
    module_0.FloatArg(*list_0)


def test_case_6():
    str_0 = " >%UnjvA[-6d@%K_"
    timer_0 = module_0.Timer(text=str_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    user_dict_0 = module_1.UserDict()
    none_type_0 = None
    var_0 = user_dict_0.setdefault(none_type_0)
    var_1 = timer_1.__repr__()


def test_case_7():
    dict_0 = {}
    timer_0 = module_0.Timer(initial_text=dict_0)
    str_0 = " >%UnjvA[-6d@%K_"
    timer_1 = module_0.Timer(str_0, str_0, str_0)
    timer_2 = timer_1.__enter__()
    float_0 = timer_2.stop()
    timer_3 = timer_1.__enter__()
    timer_error_0 = module_0.TimerError()
    float_arg_0 = module_0.FloatArg()


def test_case_8():
    dict_0 = {}
    timer_0 = module_0.Timer(logger=dict_0)
    str_0 = " does not support item assignment. Use '.add()' to update values."
    timer_1 = module_0.Timer(initial_text=str_0, logger=dict_0)
    timer_2 = timer_1.__enter__()
    float_arg_0 = module_0.FloatArg()
    none_type_0 = timer_2.__exit__()
    var_0 = none_type_0.__repr__()
    var_0.__exit__()


def test_case_9():
    dict_0 = {}
    timer_0 = module_0.Timer(initial_text=dict_0)
    str_0 = " >%UnjvA[-6d@%K_"
    timer_1 = module_0.Timer(text=timer_0, initial_text=str_0)
    timer_2 = timer_0.__enter__()
    float_arg_0 = module_0.FloatArg()
    timer_3 = timer_1.__enter__()
    none_type_0 = timer_1.__exit__()
    none_type_1 = None
    var_0 = module_2.dataclass(repr=none_type_0, eq=none_type_1, match_args=timer_1)
    var_0.__contains__(timer_1)


def test_case_10():
    bytes_0 = b"\xb4B\x93\xe7\xf1\xf7es%\x86\x17\xcc\xcfWx 5\x9e"
    timer_0 = module_0.Timer(initial_text=bytes_0)
    timer_1 = timer_0.__enter__()
    var_0 = module_2.field(compare=timer_0)
    module_0.FloatArg(**var_0)


def test_case_11():
    dict_0 = {}
    timer_0 = module_0.Timer(initial_text=dict_0)
    timer_1 = module_0.Timer(timer_0, timer_0, timer_0)
    timer_2 = timer_1.__enter__()
    float_arg_0 = module_0.FloatArg()
    var_0 = timer_1.__call__(float_arg_0)
    timer_1.__exit__()
