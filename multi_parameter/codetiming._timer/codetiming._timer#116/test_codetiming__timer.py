# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    str_0 = 'h~~="'
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()


def test_case_2():
    timer_error_0 = module_0.TimerError()
    list_0 = []
    float_arg_0 = module_0.FloatArg(*list_0)
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    timer_0.__exit__(*list_0)


def test_case_3():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, timer_error_0)
    var_0 = timer_0.__call__(timer_error_0)
    none_type_0 = timer_0.start()
    timer_0.__exit__(*none_type_0)


def test_case_4():
    timer_error_0 = module_0.TimerError()
    str_0 = 'h~~="'
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_5():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, timer_error_0, timer_error_0)
    none_type_0 = timer_0.start()
    timer_0.__exit__()


def test_case_6():
    timer_error_0 = module_0.TimerError()
    str_0 = 'h~~="'
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__(*var_0)
    var_0.clear()


def test_case_7():
    timer_error_0 = module_0.TimerError()
    str_0 = 'h~~="'
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=none_type_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = timer_1.__exit__(*str_0)
    timer_1.__delitem__(timer_0)


def test_case_8():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=timer_error_0)
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    var_0.__contains__(timer_1)


def test_case_9():
    timer_error_0 = module_0.TimerError()
    str_0 = 'h~~="'
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    none_type_0 = None
    timer_1 = module_0.Timer(str_0, timer_0, none_type_0)
    none_type_1 = timer_0.start()
    var_0 = timer_1.__repr__()
    timer_2 = timer_1.__enter__()
    none_type_2 = timer_2.__exit__(*var_0)
    var_0.__delitem__(var_0)
