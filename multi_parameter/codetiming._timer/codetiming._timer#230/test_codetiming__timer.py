# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    bool_0 = True
    timer_0 = module_0.Timer(bool_0)
    timer_1 = module_0.Timer(initial_text=bool_0)
    float_arg_0 = module_0.FloatArg()
    timer_2 = timer_1.__enter__()
    timer_1.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_3():
    str_0 = "ak\x0bBc;^VC|"
    timer_0 = module_0.Timer(initial_text=str_0)
    float_0 = -2237.09
    tuple_0 = (str_0, float_0, timer_0)
    var_0 = module_1.dataclass(eq=tuple_0, unsafe_hash=tuple_0)
    timer_1 = module_0.Timer(text=str_0, initial_text=str_0)
    timer_0.stop()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_5():
    str_0 = "<[<@3pFBSu|h36L%w"
    timer_0 = module_0.Timer(str_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()


def test_case_6():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = timer_0.__enter__()


def test_case_7():
    str_0 = "ak\x0bBc;^VC|"
    timer_0 = module_0.Timer(initial_text=str_0)
    none_type_0 = timer_0.start()
    timer_0.__enter__()


def test_case_8():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    var_0 = timer_0.__repr__()
    var_1 = module_1.dataclass(unsafe_hash=none_type_1, match_args=var_0)
    var_0.popitem()


def test_case_9():
    bool_0 = False
    bool_1 = True
    timer_0 = module_0.Timer(bool_1, logger=bool_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()
    var_0 = module_1.dataclass(order=bool_0, unsafe_hash=bool_1)
    var_0.clear()


def test_case_10():
    bool_0 = False
    bool_1 = True
    str_0 = "s>"
    timer_0 = module_0.Timer(str_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()
    var_0 = module_1.dataclass(order=bool_0, unsafe_hash=bool_1)
    timer_1 = module_0.Timer(str_0, initial_text=timer_0)
    timer_2 = timer_1.__enter__()
    bool_1.values()
