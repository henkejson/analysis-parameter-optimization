# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import codetiming._timers as module_1


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    list_0 = []
    timer_0 = module_0.Timer()
    timer_error_0 = module_0.TimerError()
    float_arg_0 = module_0.FloatArg(*list_0)
    none_type_0 = timer_0.start()
    timer_error_1 = module_0.TimerError()
    timer_0.start()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()


def test_case_3():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    timer_error_1 = module_0.TimerError()
    timer_1 = module_0.Timer()
    none_type_0 = timer_0.start()
    timer_1.__exit__()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__call__(timer_0)
    float_0 = timer_1.__call__(timer_0)


def test_case_5():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()
    timers_0 = module_1.Timers()
    var_0 = timers_0.__iter__()
    timer_0.__exit__()


def test_case_6():
    timer_error_0 = module_0.TimerError()
    none_type_0 = None
    list_0 = []
    timer_error_1 = module_0.TimerError(*list_0)
    timer_0 = module_0.Timer(none_type_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()
    timers_0 = module_1.Timers(*list_0)
    timers_0.mean(timer_error_0)


def test_case_7():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    str_0 = "\x0b-\rzt+eNjm=0K$\x0cKV)N"
    timer_1 = module_0.Timer(initial_text=str_0)
    list_0 = []
    timer_error_1 = module_0.TimerError(*list_0)
    timer_2 = module_0.Timer(initial_text=str_0)
    none_type_0 = timer_2.start()
    timer_1.stop()


def test_case_8():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    timer_error_1 = module_0.TimerError()
    timer_1 = module_0.Timer(text=timer_error_1, initial_text=timer_error_0)
    none_type_0 = timer_1.start()
    var_0 = timer_0.__repr__()
    var_0.__contains__(none_type_0)
