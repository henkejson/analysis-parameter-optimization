# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    str_0 = ":+\t\nHh"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = module_0.Timer()
    none_type_0 = timer_1.start()
    timer_1.start()


def test_case_2():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()


def test_case_3():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer()
    timer_0.__exit__()


def test_case_4():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    float_arg_0 = module_0.FloatArg()
    list_0 = [none_type_0]
    none_type_1 = timer_0.__exit__(*list_0)


def test_case_5():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_6():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()
    none_type_1 = timer_0.start()
    timer_1 = module_0.Timer(logger=none_type_1)
    none_type_2 = timer_1.start()
    bool_0 = True
    timer_2 = module_0.Timer(text=bool_0, logger=none_type_1)
    timer_3 = timer_2.__enter__()
    var_0 = timer_0.__repr__()
    var_0.__enter__()


def test_case_7():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()
    none_type_1 = timer_0.start()
    timer_1 = module_0.Timer(logger=none_type_1)
    none_type_2 = timer_1.start()
    none_type_3 = timer_1.__exit__()
    bool_0 = True
    timer_2 = module_0.Timer(text=bool_0, logger=none_type_1)
    timer_3 = timer_2.__enter__()
    var_0 = timer_0.__repr__()
    var_1 = timer_1.__repr__()
    var_0.max(timer_0)


def test_case_8():
    str_0 = ":+\t\nHh"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = None
    var_0 = timer_0.__call__(none_type_0)
    timer_1.start()


def test_case_9():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    timer_1 = module_0.Timer(initial_text=timer_0)
    timer_2 = timer_1.__enter__()
    none_type_1 = timer_2.__exit__()


def test_case_10():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()
    none_type_1 = timer_0.start()
    str_0 = '^\t*! sT]0Ux&,d")%]'
    timer_1 = module_0.Timer(float_0, initial_text=timer_0, logger=str_0)
    float_arg_0 = module_0.FloatArg()
    var_0 = timer_1.__repr__()
    timer_1.__enter__()


def test_case_11():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()
    var_0 = timer_0.__call__(float_0)
    str_0 = '^\t*! sT]0Ux&,d")%]'
    timer_1 = module_0.Timer(float_0, timer_0)
    var_1 = var_0.__repr__()
    timer_2 = timer_1.__enter__()
    none_type_1 = timer_1.__exit__(*var_1)
    str_1 = "9F}vvp/_:_GJ#"
    var_0.__setitem__(str_1, str_0)
