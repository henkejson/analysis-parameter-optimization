# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    str_0 = "T"
    timer_0 = module_0.Timer()
    var_0 = timer_0.__call__(str_0)
    var_0.__call__(var_0)


def test_case_2():
    str_0 = "T"
    timer_0 = module_0.Timer(str_0)
    timer_1 = module_0.Timer()
    var_0 = timer_0.__repr__()
    none_type_0 = timer_0.start()
    timer_1.__exit__()


def test_case_3():
    str_0 = "L1u\n#{c"
    list_0 = [str_0]
    timer_error_0 = module_0.TimerError(*list_0)
    timer_0 = module_0.Timer(str_0)
    str_1 = "^*HF03"
    dict_0 = {}
    timer_error_1 = module_0.TimerError(**dict_0)
    list_1 = [str_1, str_0]
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__(*list_1)
    module_0.FloatArg(*str_1, **dict_0)


def test_case_4():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    timer_1 = module_0.Timer(text=none_type_0, initial_text=timer_0)
    timer_2 = timer_1.__enter__()
    timer_0.__enter__()


def test_case_5():
    str_0 = "TJ{\x0cPFhOKZ"
    timer_0 = module_0.Timer(text=str_0, initial_text=str_0)
    timer_0.__enter__()


def test_case_6():
    int_0 = 0
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=none_type_0, logger=none_type_0)
    var_0 = timer_0.__call__(timer_0)
    timer_1 = module_0.Timer(text=var_0)
    var_1 = var_0.__call__(int_0)
    none_type_1 = timer_1.start()
    var_2 = var_0.__call__(var_1)


def test_case_7():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.__call__(timer_0)
    var_0 = timer_0.__call__(timer_0)
    timer_1 = module_0.Timer(text=none_type_0, initial_text=timer_0)
    timer_2 = timer_1.__enter__()
    timer_3 = timer_0.__enter__()
    float_0 = timer_0.stop()
    var_1 = timer_0.__eq__(float_0)
    float_arg_0 = module_0.FloatArg()
    none_type_1 = timer_2.__exit__()
    float_arg_1 = module_0.FloatArg()
    timer_4 = module_0.Timer(text=none_type_1, initial_text=var_0, logger=none_type_1)
    timer_3.__exit__()


def test_case_8():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0, logger=float_arg_0)
    var_0 = timer_0.__eq__(float_arg_0)
    timer_0.start()
