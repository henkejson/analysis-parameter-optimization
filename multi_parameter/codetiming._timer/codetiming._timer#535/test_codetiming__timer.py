# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_3():
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=none_type_0)
    timer_0.stop()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()


def test_case_5():
    float_arg_0 = module_0.FloatArg()
    list_0 = []
    dict_0 = {}
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(dict_0, logger=dict_0)
    none_type_0 = timer_0.start()
    float_arg_1 = module_0.FloatArg()
    float_arg_2 = module_0.FloatArg(*list_0, **dict_0)
    var_0 = timer_0.__repr__()
    timer_1 = module_0.Timer()
    timer_2 = module_0.Timer(float_arg_2, logger=none_type_0)
    var_0.stop()


def test_case_6():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    timer_1 = module_0.Timer(text=timer_0)
    none_type_1 = timer_0.__exit__()
    none_type_2 = timer_1.start()
    none_type_3 = timer_1.__exit__()
    none_type_4 = None
    var_0 = module_1.field(default=none_type_4, init=none_type_4, hash=none_type_4)
    var_0.__copy__()


def test_case_7():
    float_arg_0 = module_0.FloatArg()
    list_0 = []
    dict_0 = {}
    timer_0 = module_0.Timer(dict_0, logger=dict_0)
    none_type_0 = timer_0.start()
    float_arg_1 = module_0.FloatArg()
    none_type_1 = timer_0.__exit__()
    float_arg_2 = module_0.FloatArg(*list_0, **dict_0)
    var_0 = timer_0.__repr__()
    timer_1 = module_0.Timer()
    timer_2 = module_0.Timer(float_arg_2, logger=none_type_0)
    var_0.stop()


def test_case_8():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    var_0 = timer_1.__eq__(timer_1)
    var_1 = timer_1.__call__(timer_0)
    timer_2 = module_0.Timer(var_0, initial_text=var_1)
    timer_3 = module_0.Timer(text=timer_0, initial_text=timer_1, logger=var_0)
    timer_4 = timer_2.__enter__()
    none_type_0 = timer_4.__exit__()
    var_2 = var_0.__ror__(timer_0)
    list_0 = []
    var_3 = module_1.dataclass(unsafe_hash=var_2, kw_only=list_0)


def test_case_9():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    var_0 = timer_1.__eq__(timer_1)
    timer_2 = module_0.Timer(initial_text=var_0)
    timer_3 = timer_2.__enter__()
    float_arg_0 = module_0.FloatArg()
    timer_2.__exit__(*var_0)


def test_case_10():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    var_0 = timer_1.__repr__()
    timer_2 = module_0.Timer(initial_text=var_0)
    timer_2.__enter__()
