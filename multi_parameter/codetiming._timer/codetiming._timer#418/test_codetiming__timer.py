# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    timer_1.__enter__()


def test_case_2():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = timer_0.__enter__()


def test_case_3():
    str_0 = "+Uj}"
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=str_0, logger=none_type_0)
    list_0 = [none_type_0, none_type_0, none_type_0]
    timer_0.__exit__(*list_0)


def test_case_4():
    str_0 = "\tk0!d"
    timer_0 = module_0.Timer(str_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()
    float_arg_0 = module_0.FloatArg()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()
    timer_error_0 = module_0.TimerError()
    timer_0.start()


def test_case_6():
    str_0 = "\tk0!d"
    timer_0 = module_0.Timer(str_0)
    timer_1 = module_0.Timer()
    timer_2 = timer_1.__enter__()


def test_case_7():
    timer_error_0 = module_0.TimerError()
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()
    timer_2 = timer_1.__enter__()


def test_case_8():
    str_0 = "+Uj}"
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=str_0, logger=none_type_0)
    list_0 = [none_type_0, none_type_0, none_type_0]
    var_0 = timer_0.__eq__(timer_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = timer_0.__exit__(*list_0)


def test_case_9():
    timer_error_0 = module_0.TimerError()
    str_0 = "\tk0!d"
    timer_0 = module_0.Timer(text=str_0, initial_text=str_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()
    timer_1.stop()


def test_case_10():
    timer_error_0 = module_0.TimerError()
    str_0 = "\tk0!d"
    timer_0 = module_0.Timer(str_0)
    timer_1 = timer_0.__enter__()
    bool_0 = True
    timer_2 = module_0.Timer(text=timer_1)
    timer_3 = timer_2.__enter__()
    list_0 = [str_0, bool_0, timer_0]
    none_type_0 = timer_3.__exit__(*list_0)
    timer_4 = timer_3.__enter__()
    timer_3.__enter__()


def test_case_11():
    timer_error_0 = module_0.TimerError()
    str_0 = "kQw"
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    bool_0 = True
    timer_2 = module_0.Timer(timer_error_0, str_0, bool_0)
    timer_3 = timer_2.__enter__()
    none_type_0 = timer_1.__exit__()
    timer_4 = timer_1.__enter__()
    timer_2.__enter__()
