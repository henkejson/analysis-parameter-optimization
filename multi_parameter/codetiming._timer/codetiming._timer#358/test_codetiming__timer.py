# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import collections as module_1
import dataclasses as module_2


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer(text=timer_0)
    timer_1.stop()


def test_case_3():
    str_0 = "Timer started"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_1 = timer_0.__enter__()
    timer_0.start()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()


def test_case_5():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_6():
    str_0 = ""
    timer_0 = module_0.Timer(logger=str_0)
    user_dict_0 = module_1.UserDict()
    list_0 = []
    none_type_0 = timer_0.start()
    var_0 = module_2.dataclass(
        repr=list_0, order=list_0, frozen=list_0, kw_only=list_0, slots=list_0
    )
    timer_1 = module_0.Timer(logger=str_0)
    timer_1.__exit__(*var_0)


def test_case_7():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__repr__()
    str_0 = "T89^5zMs!#|\\<="
    timer_1 = module_0.Timer(str_0)
    none_type_0 = timer_1.start()
    var_1 = timer_0.__eq__(timer_1)
    float_0 = timer_1.stop()
    module_0.FloatArg(**var_1)


def test_case_8():
    timer_0 = module_0.Timer()
    none_type_0 = None
    timer_1 = module_0.Timer(logger=none_type_0)
    timer_2 = timer_1.__enter__()
    none_type_1 = timer_0.__repr__()
    float_0 = timer_2.stop()
    var_0 = timer_0.__repr__()
    var_0.pop(var_0)


def test_case_9():
    none_type_0 = None
    var_0 = module_2.dataclass(
        none_type_0,
        repr=none_type_0,
        unsafe_hash=none_type_0,
        match_args=none_type_0,
        kw_only=none_type_0,
    )
    timer_0 = module_0.Timer(initial_text=var_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = timer_0.__exit__()
    timer_2 = timer_1.__enter__()
    none_type_2 = timer_1.__exit__()
    var_0.stop()


def test_case_10():
    str_0 = "T"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=timer_1)
    timer_3 = timer_2.__enter__()
    none_type_0 = timer_3.__exit__()
    float_0 = timer_1.stop()
    var_0 = timer_0.__repr__()
    var_0.stop()


def test_case_11():
    none_type_0 = None
    var_0 = module_2.dataclass(
        none_type_0,
        repr=none_type_0,
        unsafe_hash=none_type_0,
        match_args=none_type_0,
        kw_only=none_type_0,
    )
    timer_0 = module_0.Timer(var_0, initial_text=var_0)
    timer_1 = timer_0.__enter__()
    var_0.stop()
