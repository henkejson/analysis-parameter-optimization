# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import codetiming._timers as module_1
import dataclasses as module_2


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    str_0 = "Timer is running. Use .stp() to stop it"
    timer_0 = module_0.Timer(initial_text=str_0)
    none_type_0 = timer_0.start()
    timer_0.start()


def test_case_2():
    timers_0 = module_1.Timers()
    var_0 = timers_0.__iter__()
    timer_0 = module_0.Timer(initial_text=var_0)
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__(*var_0)
    var_1 = timers_0.__ror__(timer_0)
    timers_0.__getitem__(var_0)


def test_case_3():
    timers_0 = module_1.Timers()
    timer_0 = module_0.Timer(initial_text=timers_0)
    timer_1 = timer_0.__enter__()
    module_0.FloatArg(**timer_0)


def test_case_4():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    str_0 = "A<rSu~@]R(mec"
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    timer_error_0 = module_0.TimerError()
    timer_2 = module_0.Timer()
    var_0 = timer_2.__repr__()
    var_1 = module_2.dataclass(init=str_0)
    var_1.count(timer_2)


def test_case_5():
    timers_0 = module_1.Timers()
    var_0 = timers_0.__iter__()
    timer_0 = module_0.Timer(initial_text=var_0)
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__(*var_0)
    timer_0.__exit__(*var_0)


def test_case_6():
    str_0 = '/"!pj'
    timer_0 = module_0.Timer(str_0)
    timers_0 = module_1.Timers()
    timer_1 = timer_0.__enter__()
    var_0 = timers_0.__iter__()
    var_1 = timer_0.__call__(str_0)
    float_0 = timer_0.stop()
    var_2 = var_0.__eq__(timer_1)
    timers_0.pop(str_0)


def test_case_7():
    float_arg_0 = module_0.FloatArg()
    float_arg_1 = module_2.dataclass(init=float_arg_0, repr=float_arg_0)
    timer_0 = module_0.Timer(text=float_arg_1, logger=float_arg_1)
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    timer_1.__exit__()


def test_case_8():
    timers_0 = module_1.Timers()
    var_0 = module_2.field(kw_only=timers_0)
    timer_0 = module_0.Timer(initial_text=var_0)
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    timer_error_0 = module_0.TimerError()


def test_case_9():
    timers_0 = module_1.Timers()
    var_0 = timers_0.__iter__()
    tuple_0 = ()
    timer_0 = module_0.Timer(var_0, tuple_0, var_0)
    float_arg_0 = module_0.FloatArg(*var_0)
    timer_1 = timer_0.__enter__()
    var_1 = var_0.__repr__()
    module_2.dataclass(var_0, eq=var_1, unsafe_hash=var_1)
