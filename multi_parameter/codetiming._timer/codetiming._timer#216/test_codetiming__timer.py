# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, initial_text=none_type_0)
    timer_1 = timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer(initial_text=timer_0)
    timer_2 = timer_0.__repr__()
    none_type_0 = timer_1.__call__(timer_2)
    dict_0 = {}
    float_arg_0 = module_0.FloatArg(**dict_0)
    set_0 = {none_type_0}
    timer_3 = module_0.Timer(logger=set_0)
    timer_0.__exit__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()


def test_case_4():
    str_0 = '6"HtX64pyR'
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=str_0)
    var_0 = timer_0.__eq__(str_0)
    var_1 = timer_0.__repr__()
    timer_1 = module_0.Timer(timer_0)
    timer_2 = timer_0.__enter__()
    float_0 = timer_2.stop()
    var_1.__getitem__(var_0)


def test_case_5():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_0.start()


def test_case_6():
    str_0 = '6"HtX64pyR'
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(str_0, initial_text=float_arg_0)
    var_0 = timer_0.__eq__(str_0)
    var_1 = timer_0.__repr__()
    timer_1 = module_0.Timer(timer_0)
    timer_2 = timer_0.__enter__()
    none_type_0 = timer_1.start()
    var_2 = var_0.__eq__(float_arg_0)
    float_0 = timer_2.stop()
    float_arg_1 = module_0.FloatArg()
    dict_0 = {str_0: str_0}
    module_0.TimerError(**dict_0)


def test_case_7():
    timer_error_0 = module_0.TimerError()
    float_arg_0 = module_0.FloatArg()
    bool_0 = True
    timer_0 = module_0.Timer(text=timer_error_0, initial_text=bool_0, logger=bool_0)
    timer_0.__enter__()


def test_case_8():
    str_0 = '6"HtX64pyR'
    float_arg_0 = module_0.FloatArg()
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=none_type_0, logger=none_type_0)
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    float_arg_1 = module_0.FloatArg()
    dict_0 = {str_0: str_0}
    module_0.TimerError(**dict_0)


def test_case_9():
    str_0 = '6"HtX64pyR'
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=str_0)
    var_0 = module_0.Timer(text=timer_0, initial_text=timer_0, logger=timer_0)
    var_1 = timer_0.__repr__()
    timer_1 = module_0.Timer(timer_0)
    timer_2 = var_0.__enter__()
    float_0 = timer_2.stop()
    float_arg_1 = module_0.FloatArg()
    var_2 = var_1.__len__()
    var_3 = var_1.__contains__(str_0)
    none_type_0 = timer_1.start()
    var_4 = var_0.__eq__(var_1)
    module_0.FloatArg(**var_2)
