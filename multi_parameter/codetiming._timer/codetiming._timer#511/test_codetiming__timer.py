# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import builtins as module_1


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_0.__exit__()


def test_case_3():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0, none_type_0, none_type_0)
    none_type_1 = timer_0.start()
    float_arg_0 = module_0.FloatArg()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0, none_type_0, none_type_0)
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()
    bool_0 = False
    module_1.Exception(*bool_0)


def test_case_6():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_7():
    str_0 = "eL"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    float_0.update()


def test_case_8():
    float_arg_0 = module_0.FloatArg()
    none_type_0 = None
    timer_0 = module_0.Timer(float_arg_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    var_0 = timer_1.__repr__()
    var_1 = var_0.__iter__()
    var_0.__delitem__(float_arg_0)


def test_case_9():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, float_arg_0, float_arg_0)
    timer_1 = timer_0.__enter__()
    var_0 = timer_1.__call__(float_arg_0)
    timer_1.stop()


def test_case_10():
    float_arg_0 = module_0.FloatArg()
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0, float_arg_0)
    timer_1 = timer_0.__enter__()
    timer_0.stop()


def test_case_11():
    str_0 = "eL"
    timer_0 = module_0.Timer(initial_text=str_0)
    bool_0 = False
    timer_1 = module_0.Timer(str_0, timer_0, bool_0)
    timer_2 = timer_1.__enter__()
    float_0 = timer_2.stop()
    timer_2.stop()
