# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1
import contextlib as module_2


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_0.start()


def test_case_2():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()


def test_case_3():
    none_type_0 = None
    timer_0 = module_0.Timer(
        text=none_type_0, initial_text=none_type_0, logger=none_type_0
    )
    timer_1 = module_0.Timer(initial_text=timer_0)
    none_type_1 = timer_1.start()
    none_type_2 = timer_1.__exit__()
    timer_1.stop()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_error_0 = module_0.TimerError()
    str_0 = "\\|;KX77`hB Mel#G\n2"
    module_1.field(init=str_0, repr=str_0, compare=str_0, metadata=timer_error_0)


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(
        text=none_type_0, initial_text=none_type_0, logger=none_type_0
    )
    timer_1 = module_0.Timer(initial_text=timer_0)
    none_type_1 = timer_1.start()
    float_0 = timer_1.stop()


def test_case_6():
    timer_error_0 = module_0.TimerError()
    str_0 = "jKyQD:0rL2\x0bkO:.9B"
    timer_0 = module_0.Timer(initial_text=str_0)
    float_arg_0 = module_0.FloatArg()
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()
    var_0 = timer_0.__repr__()
    timer_0.stop()


def test_case_7():
    timer_error_0 = module_0.TimerError()
    none_type_0 = None
    timer_0 = module_0.Timer(
        text=none_type_0, initial_text=none_type_0, logger=none_type_0
    )
    timer_1 = timer_0.__enter__()
    float_arg_0 = module_0.FloatArg()
    float_0 = timer_0.stop()
    var_0 = module_1.field()
    timer_2 = module_0.Timer(logger=timer_1)
    timer_2.__exit__(*var_0)


def test_case_8():
    none_type_0 = None
    timer_0 = module_0.Timer(
        text=none_type_0, initial_text=none_type_0, logger=none_type_0
    )
    var_0 = timer_0.__call__(timer_0)
    var_1 = var_0.__eq__(var_0)
    timer_1 = module_0.Timer(initial_text=var_1)
    timer_2 = module_0.Timer(timer_0, initial_text=var_0)
    none_type_1 = timer_2.start()
    var_2 = module_1.field(init=var_0, repr=var_1, compare=var_0)
    timer_0.stop()


def test_case_9():
    none_type_0 = None
    timer_0 = module_0.Timer(
        text=none_type_0, initial_text=none_type_0, logger=none_type_0
    )
    context_decorator_0 = module_2.ContextDecorator()
    none_type_1 = None
    timer_1 = module_0.Timer(timer_0, initial_text=none_type_1)
    var_0 = timer_1.__eq__(none_type_0)
    float_arg_0 = module_0.FloatArg()
    none_type_2 = timer_1.start()
    timer_1.__exit__()


def test_case_10():
    none_type_0 = None
    timer_0 = module_0.Timer(
        text=none_type_0, initial_text=none_type_0, logger=none_type_0
    )
    var_0 = timer_0.__call__(timer_0)
    var_1 = timer_0.__eq__(none_type_0)
    timer_1 = module_0.Timer(text=var_0, initial_text=var_0)
    float_arg_0 = module_0.FloatArg()
    none_type_1 = timer_1.start()
    float_0 = timer_1.stop()
    timer_1.__exit__()
