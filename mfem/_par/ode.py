# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ode
else:
    import _ode

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _ode.SWIG_PyInstanceMethod_New
_swig_new_static_method = _ode.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._par.vector
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.operators
class ODESolver(object):
    r"""Proxy of C++ mfem::ODESolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Init(self, f):
        r"""Init(ODESolver self, TimeDependentOperator f)"""
        return _ode.ODESolver_Init(self, f)
    Init = _swig_new_instance_method(_ode.ODESolver_Init)

    def Step(self, x, t, dt):
        r"""Step(ODESolver self, Vector x, double & t, double & dt)"""
        return _ode.ODESolver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.ODESolver_Step)

    def Run(self, x, t, dt, tf):
        r"""Run(ODESolver self, Vector x, double & t, double & dt, double tf)"""
        return _ode.ODESolver_Run(self, x, t, dt, tf)
    Run = _swig_new_instance_method(_ode.ODESolver_Run)
    __swig_destroy__ = _ode.delete_ODESolver

# Register ODESolver in _ode:
_ode.ODESolver_swigregister(ODESolver)

class ForwardEulerSolver(ODESolver):
    r"""Proxy of C++ mfem::ForwardEulerSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def Init(self, _f):
        r"""Init(ForwardEulerSolver self, TimeDependentOperator _f)"""
        return _ode.ForwardEulerSolver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.ForwardEulerSolver_Init)

    def Step(self, x, t, dt):
        r"""Step(ForwardEulerSolver self, Vector x, double & t, double & dt)"""
        return _ode.ForwardEulerSolver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.ForwardEulerSolver_Step)

    def __init__(self):
        r"""__init__(ForwardEulerSolver self) -> ForwardEulerSolver"""
        _ode.ForwardEulerSolver_swiginit(self, _ode.new_ForwardEulerSolver())
    __swig_destroy__ = _ode.delete_ForwardEulerSolver

# Register ForwardEulerSolver in _ode:
_ode.ForwardEulerSolver_swigregister(ForwardEulerSolver)

class RK2Solver(ODESolver):
    r"""Proxy of C++ mfem::RK2Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(RK2Solver self, double const _a=2./3.) -> RK2Solver"""
        _ode.RK2Solver_swiginit(self, _ode.new_RK2Solver(*args, **kwargs))

    def Init(self, _f):
        r"""Init(RK2Solver self, TimeDependentOperator _f)"""
        return _ode.RK2Solver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.RK2Solver_Init)

    def Step(self, x, t, dt):
        r"""Step(RK2Solver self, Vector x, double & t, double & dt)"""
        return _ode.RK2Solver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.RK2Solver_Step)
    __swig_destroy__ = _ode.delete_RK2Solver

# Register RK2Solver in _ode:
_ode.RK2Solver_swigregister(RK2Solver)

class RK3SSPSolver(ODESolver):
    r"""Proxy of C++ mfem::RK3SSPSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def Init(self, _f):
        r"""Init(RK3SSPSolver self, TimeDependentOperator _f)"""
        return _ode.RK3SSPSolver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.RK3SSPSolver_Init)

    def Step(self, x, t, dt):
        r"""Step(RK3SSPSolver self, Vector x, double & t, double & dt)"""
        return _ode.RK3SSPSolver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.RK3SSPSolver_Step)

    def __init__(self):
        r"""__init__(RK3SSPSolver self) -> RK3SSPSolver"""
        _ode.RK3SSPSolver_swiginit(self, _ode.new_RK3SSPSolver())
    __swig_destroy__ = _ode.delete_RK3SSPSolver

# Register RK3SSPSolver in _ode:
_ode.RK3SSPSolver_swigregister(RK3SSPSolver)

class RK4Solver(ODESolver):
    r"""Proxy of C++ mfem::RK4Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def Init(self, _f):
        r"""Init(RK4Solver self, TimeDependentOperator _f)"""
        return _ode.RK4Solver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.RK4Solver_Init)

    def Step(self, x, t, dt):
        r"""Step(RK4Solver self, Vector x, double & t, double & dt)"""
        return _ode.RK4Solver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.RK4Solver_Step)

    def __init__(self):
        r"""__init__(RK4Solver self) -> RK4Solver"""
        _ode.RK4Solver_swiginit(self, _ode.new_RK4Solver())
    __swig_destroy__ = _ode.delete_RK4Solver

# Register RK4Solver in _ode:
_ode.RK4Solver_swigregister(RK4Solver)

class ExplicitRKSolver(ODESolver):
    r"""Proxy of C++ mfem::ExplicitRKSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, _s, _a, _b, _c):
        r"""__init__(ExplicitRKSolver self, int _s, double const * _a, double const * _b, double const * _c) -> ExplicitRKSolver"""
        _ode.ExplicitRKSolver_swiginit(self, _ode.new_ExplicitRKSolver(_s, _a, _b, _c))

    def Init(self, _f):
        r"""Init(ExplicitRKSolver self, TimeDependentOperator _f)"""
        return _ode.ExplicitRKSolver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.ExplicitRKSolver_Init)

    def Step(self, x, t, dt):
        r"""Step(ExplicitRKSolver self, Vector x, double & t, double & dt)"""
        return _ode.ExplicitRKSolver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.ExplicitRKSolver_Step)
    __swig_destroy__ = _ode.delete_ExplicitRKSolver

# Register ExplicitRKSolver in _ode:
_ode.ExplicitRKSolver_swigregister(ExplicitRKSolver)

class RK6Solver(ExplicitRKSolver):
    r"""Proxy of C++ mfem::RK6Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(RK6Solver self) -> RK6Solver"""
        _ode.RK6Solver_swiginit(self, _ode.new_RK6Solver())
    __swig_destroy__ = _ode.delete_RK6Solver

# Register RK6Solver in _ode:
_ode.RK6Solver_swigregister(RK6Solver)

class RK8Solver(ExplicitRKSolver):
    r"""Proxy of C++ mfem::RK8Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(RK8Solver self) -> RK8Solver"""
        _ode.RK8Solver_swiginit(self, _ode.new_RK8Solver())
    __swig_destroy__ = _ode.delete_RK8Solver

# Register RK8Solver in _ode:
_ode.RK8Solver_swigregister(RK8Solver)

class AdamsBashforthSolver(ODESolver):
    r"""Proxy of C++ mfem::AdamsBashforthSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, _s, _a):
        r"""__init__(AdamsBashforthSolver self, int _s, double const * _a) -> AdamsBashforthSolver"""
        _ode.AdamsBashforthSolver_swiginit(self, _ode.new_AdamsBashforthSolver(_s, _a))

    def Init(self, _f):
        r"""Init(AdamsBashforthSolver self, TimeDependentOperator _f)"""
        return _ode.AdamsBashforthSolver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.AdamsBashforthSolver_Init)

    def Step(self, x, t, dt):
        r"""Step(AdamsBashforthSolver self, Vector x, double & t, double & dt)"""
        return _ode.AdamsBashforthSolver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.AdamsBashforthSolver_Step)
    __swig_destroy__ = _ode.delete_AdamsBashforthSolver

# Register AdamsBashforthSolver in _ode:
_ode.AdamsBashforthSolver_swigregister(AdamsBashforthSolver)

class AB1Solver(AdamsBashforthSolver):
    r"""Proxy of C++ mfem::AB1Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(AB1Solver self) -> AB1Solver"""
        _ode.AB1Solver_swiginit(self, _ode.new_AB1Solver())
    __swig_destroy__ = _ode.delete_AB1Solver

# Register AB1Solver in _ode:
_ode.AB1Solver_swigregister(AB1Solver)

class AB2Solver(AdamsBashforthSolver):
    r"""Proxy of C++ mfem::AB2Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(AB2Solver self) -> AB2Solver"""
        _ode.AB2Solver_swiginit(self, _ode.new_AB2Solver())
    __swig_destroy__ = _ode.delete_AB2Solver

# Register AB2Solver in _ode:
_ode.AB2Solver_swigregister(AB2Solver)

class AB3Solver(AdamsBashforthSolver):
    r"""Proxy of C++ mfem::AB3Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(AB3Solver self) -> AB3Solver"""
        _ode.AB3Solver_swiginit(self, _ode.new_AB3Solver())
    __swig_destroy__ = _ode.delete_AB3Solver

# Register AB3Solver in _ode:
_ode.AB3Solver_swigregister(AB3Solver)

class AB4Solver(AdamsBashforthSolver):
    r"""Proxy of C++ mfem::AB4Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(AB4Solver self) -> AB4Solver"""
        _ode.AB4Solver_swiginit(self, _ode.new_AB4Solver())
    __swig_destroy__ = _ode.delete_AB4Solver

# Register AB4Solver in _ode:
_ode.AB4Solver_swigregister(AB4Solver)

class AB5Solver(AdamsBashforthSolver):
    r"""Proxy of C++ mfem::AB5Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(AB5Solver self) -> AB5Solver"""
        _ode.AB5Solver_swiginit(self, _ode.new_AB5Solver())
    __swig_destroy__ = _ode.delete_AB5Solver

# Register AB5Solver in _ode:
_ode.AB5Solver_swigregister(AB5Solver)

class AdamsMoultonSolver(ODESolver):
    r"""Proxy of C++ mfem::AdamsMoultonSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, _s, _a):
        r"""__init__(AdamsMoultonSolver self, int _s, double const * _a) -> AdamsMoultonSolver"""
        _ode.AdamsMoultonSolver_swiginit(self, _ode.new_AdamsMoultonSolver(_s, _a))

    def Init(self, _f):
        r"""Init(AdamsMoultonSolver self, TimeDependentOperator _f)"""
        return _ode.AdamsMoultonSolver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.AdamsMoultonSolver_Init)

    def Step(self, x, t, dt):
        r"""Step(AdamsMoultonSolver self, Vector x, double & t, double & dt)"""
        return _ode.AdamsMoultonSolver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.AdamsMoultonSolver_Step)
    __swig_destroy__ = _ode.delete_AdamsMoultonSolver

# Register AdamsMoultonSolver in _ode:
_ode.AdamsMoultonSolver_swigregister(AdamsMoultonSolver)

class AM0Solver(AdamsMoultonSolver):
    r"""Proxy of C++ mfem::AM0Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(AM0Solver self) -> AM0Solver"""
        _ode.AM0Solver_swiginit(self, _ode.new_AM0Solver())
    __swig_destroy__ = _ode.delete_AM0Solver

# Register AM0Solver in _ode:
_ode.AM0Solver_swigregister(AM0Solver)

class AM1Solver(AdamsMoultonSolver):
    r"""Proxy of C++ mfem::AM1Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(AM1Solver self) -> AM1Solver"""
        _ode.AM1Solver_swiginit(self, _ode.new_AM1Solver())
    __swig_destroy__ = _ode.delete_AM1Solver

# Register AM1Solver in _ode:
_ode.AM1Solver_swigregister(AM1Solver)

class AM2Solver(AdamsMoultonSolver):
    r"""Proxy of C++ mfem::AM2Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(AM2Solver self) -> AM2Solver"""
        _ode.AM2Solver_swiginit(self, _ode.new_AM2Solver())
    __swig_destroy__ = _ode.delete_AM2Solver

# Register AM2Solver in _ode:
_ode.AM2Solver_swigregister(AM2Solver)

class AM3Solver(AdamsMoultonSolver):
    r"""Proxy of C++ mfem::AM3Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(AM3Solver self) -> AM3Solver"""
        _ode.AM3Solver_swiginit(self, _ode.new_AM3Solver())
    __swig_destroy__ = _ode.delete_AM3Solver

# Register AM3Solver in _ode:
_ode.AM3Solver_swigregister(AM3Solver)

class AM4Solver(AdamsMoultonSolver):
    r"""Proxy of C++ mfem::AM4Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(AM4Solver self) -> AM4Solver"""
        _ode.AM4Solver_swiginit(self, _ode.new_AM4Solver())
    __swig_destroy__ = _ode.delete_AM4Solver

# Register AM4Solver in _ode:
_ode.AM4Solver_swigregister(AM4Solver)

class BackwardEulerSolver(ODESolver):
    r"""Proxy of C++ mfem::BackwardEulerSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def Init(self, _f):
        r"""Init(BackwardEulerSolver self, TimeDependentOperator _f)"""
        return _ode.BackwardEulerSolver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.BackwardEulerSolver_Init)

    def Step(self, x, t, dt):
        r"""Step(BackwardEulerSolver self, Vector x, double & t, double & dt)"""
        return _ode.BackwardEulerSolver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.BackwardEulerSolver_Step)

    def __init__(self):
        r"""__init__(BackwardEulerSolver self) -> BackwardEulerSolver"""
        _ode.BackwardEulerSolver_swiginit(self, _ode.new_BackwardEulerSolver())
    __swig_destroy__ = _ode.delete_BackwardEulerSolver

# Register BackwardEulerSolver in _ode:
_ode.BackwardEulerSolver_swigregister(BackwardEulerSolver)

class ImplicitMidpointSolver(ODESolver):
    r"""Proxy of C++ mfem::ImplicitMidpointSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def Init(self, _f):
        r"""Init(ImplicitMidpointSolver self, TimeDependentOperator _f)"""
        return _ode.ImplicitMidpointSolver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.ImplicitMidpointSolver_Init)

    def Step(self, x, t, dt):
        r"""Step(ImplicitMidpointSolver self, Vector x, double & t, double & dt)"""
        return _ode.ImplicitMidpointSolver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.ImplicitMidpointSolver_Step)

    def __init__(self):
        r"""__init__(ImplicitMidpointSolver self) -> ImplicitMidpointSolver"""
        _ode.ImplicitMidpointSolver_swiginit(self, _ode.new_ImplicitMidpointSolver())
    __swig_destroy__ = _ode.delete_ImplicitMidpointSolver

# Register ImplicitMidpointSolver in _ode:
_ode.ImplicitMidpointSolver_swigregister(ImplicitMidpointSolver)

class SDIRK23Solver(ODESolver):
    r"""Proxy of C++ mfem::SDIRK23Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, gamma_opt=1):
        r"""__init__(SDIRK23Solver self, int gamma_opt=1) -> SDIRK23Solver"""
        _ode.SDIRK23Solver_swiginit(self, _ode.new_SDIRK23Solver(gamma_opt))

    def Init(self, _f):
        r"""Init(SDIRK23Solver self, TimeDependentOperator _f)"""
        return _ode.SDIRK23Solver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.SDIRK23Solver_Init)

    def Step(self, x, t, dt):
        r"""Step(SDIRK23Solver self, Vector x, double & t, double & dt)"""
        return _ode.SDIRK23Solver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.SDIRK23Solver_Step)
    __swig_destroy__ = _ode.delete_SDIRK23Solver

# Register SDIRK23Solver in _ode:
_ode.SDIRK23Solver_swigregister(SDIRK23Solver)

class SDIRK34Solver(ODESolver):
    r"""Proxy of C++ mfem::SDIRK34Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def Init(self, _f):
        r"""Init(SDIRK34Solver self, TimeDependentOperator _f)"""
        return _ode.SDIRK34Solver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.SDIRK34Solver_Init)

    def Step(self, x, t, dt):
        r"""Step(SDIRK34Solver self, Vector x, double & t, double & dt)"""
        return _ode.SDIRK34Solver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.SDIRK34Solver_Step)

    def __init__(self):
        r"""__init__(SDIRK34Solver self) -> SDIRK34Solver"""
        _ode.SDIRK34Solver_swiginit(self, _ode.new_SDIRK34Solver())
    __swig_destroy__ = _ode.delete_SDIRK34Solver

# Register SDIRK34Solver in _ode:
_ode.SDIRK34Solver_swigregister(SDIRK34Solver)

class SDIRK33Solver(ODESolver):
    r"""Proxy of C++ mfem::SDIRK33Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def Init(self, _f):
        r"""Init(SDIRK33Solver self, TimeDependentOperator _f)"""
        return _ode.SDIRK33Solver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.SDIRK33Solver_Init)

    def Step(self, x, t, dt):
        r"""Step(SDIRK33Solver self, Vector x, double & t, double & dt)"""
        return _ode.SDIRK33Solver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.SDIRK33Solver_Step)

    def __init__(self):
        r"""__init__(SDIRK33Solver self) -> SDIRK33Solver"""
        _ode.SDIRK33Solver_swiginit(self, _ode.new_SDIRK33Solver())
    __swig_destroy__ = _ode.delete_SDIRK33Solver

# Register SDIRK33Solver in _ode:
_ode.SDIRK33Solver_swigregister(SDIRK33Solver)

class GeneralizedAlphaSolver(ODESolver):
    r"""Proxy of C++ mfem::GeneralizedAlphaSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, rho=1.0):
        r"""__init__(GeneralizedAlphaSolver self, double rho=1.0) -> GeneralizedAlphaSolver"""
        _ode.GeneralizedAlphaSolver_swiginit(self, _ode.new_GeneralizedAlphaSolver(rho))

    def Init(self, _f):
        r"""Init(GeneralizedAlphaSolver self, TimeDependentOperator _f)"""
        return _ode.GeneralizedAlphaSolver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.GeneralizedAlphaSolver_Init)

    def Step(self, x, t, dt):
        r"""Step(GeneralizedAlphaSolver self, Vector x, double & t, double & dt)"""
        return _ode.GeneralizedAlphaSolver_Step(self, x, t, dt)
    Step = _swig_new_instance_method(_ode.GeneralizedAlphaSolver_Step)
    __swig_destroy__ = _ode.delete_GeneralizedAlphaSolver

# Register GeneralizedAlphaSolver in _ode:
_ode.GeneralizedAlphaSolver_swigregister(GeneralizedAlphaSolver)

class SIASolver(object):
    r"""Proxy of C++ mfem::SIASolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Init(self, P, F):
        r"""Init(SIASolver self, Operator P, TimeDependentOperator F)"""
        return _ode.SIASolver_Init(self, P, F)
    Init = _swig_new_instance_method(_ode.SIASolver_Init)

    def Step(self, q, p, t, dt):
        r"""Step(SIASolver self, Vector q, Vector p, double & t, double & dt)"""
        return _ode.SIASolver_Step(self, q, p, t, dt)
    Step = _swig_new_instance_method(_ode.SIASolver_Step)

    def Run(self, q, p, t, dt, tf):
        r"""Run(SIASolver self, Vector q, Vector p, double & t, double & dt, double tf)"""
        return _ode.SIASolver_Run(self, q, p, t, dt, tf)
    Run = _swig_new_instance_method(_ode.SIASolver_Run)
    __swig_destroy__ = _ode.delete_SIASolver

# Register SIASolver in _ode:
_ode.SIASolver_swigregister(SIASolver)

class SIA1Solver(SIASolver):
    r"""Proxy of C++ mfem::SIA1Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(SIA1Solver self) -> SIA1Solver"""
        _ode.SIA1Solver_swiginit(self, _ode.new_SIA1Solver())

    def Step(self, q, p, t, dt):
        r"""Step(SIA1Solver self, Vector q, Vector p, double & t, double & dt)"""
        return _ode.SIA1Solver_Step(self, q, p, t, dt)
    Step = _swig_new_instance_method(_ode.SIA1Solver_Step)
    __swig_destroy__ = _ode.delete_SIA1Solver

# Register SIA1Solver in _ode:
_ode.SIA1Solver_swigregister(SIA1Solver)

class SIA2Solver(SIASolver):
    r"""Proxy of C++ mfem::SIA2Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(SIA2Solver self) -> SIA2Solver"""
        _ode.SIA2Solver_swiginit(self, _ode.new_SIA2Solver())

    def Step(self, q, p, t, dt):
        r"""Step(SIA2Solver self, Vector q, Vector p, double & t, double & dt)"""
        return _ode.SIA2Solver_Step(self, q, p, t, dt)
    Step = _swig_new_instance_method(_ode.SIA2Solver_Step)
    __swig_destroy__ = _ode.delete_SIA2Solver

# Register SIA2Solver in _ode:
_ode.SIA2Solver_swigregister(SIA2Solver)

class SIAVSolver(SIASolver):
    r"""Proxy of C++ mfem::SIAVSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, order):
        r"""__init__(SIAVSolver self, int order) -> SIAVSolver"""
        _ode.SIAVSolver_swiginit(self, _ode.new_SIAVSolver(order))

    def Step(self, q, p, t, dt):
        r"""Step(SIAVSolver self, Vector q, Vector p, double & t, double & dt)"""
        return _ode.SIAVSolver_Step(self, q, p, t, dt)
    Step = _swig_new_instance_method(_ode.SIAVSolver_Step)
    __swig_destroy__ = _ode.delete_SIAVSolver

# Register SIAVSolver in _ode:
_ode.SIAVSolver_swigregister(SIAVSolver)

class SecondOrderODESolver(object):
    r"""Proxy of C++ mfem::SecondOrderODESolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Init(self, f):
        r"""Init(SecondOrderODESolver self, SecondOrderTimeDependentOperator f)"""
        return _ode.SecondOrderODESolver_Init(self, f)
    Init = _swig_new_instance_method(_ode.SecondOrderODESolver_Init)

    def Step(self, x, dxdt, t, dt):
        r"""Step(SecondOrderODESolver self, Vector x, Vector dxdt, double & t, double & dt)"""
        return _ode.SecondOrderODESolver_Step(self, x, dxdt, t, dt)
    Step = _swig_new_instance_method(_ode.SecondOrderODESolver_Step)

    def Run(self, x, dxdt, t, dt, tf):
        r"""Run(SecondOrderODESolver self, Vector x, Vector dxdt, double & t, double & dt, double tf)"""
        return _ode.SecondOrderODESolver_Run(self, x, dxdt, t, dt, tf)
    Run = _swig_new_instance_method(_ode.SecondOrderODESolver_Run)
    __swig_destroy__ = _ode.delete_SecondOrderODESolver

# Register SecondOrderODESolver in _ode:
_ode.SecondOrderODESolver_swigregister(SecondOrderODESolver)

class NewmarkSolver(SecondOrderODESolver):
    r"""Proxy of C++ mfem::NewmarkSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, beta_=0.25, gamma_=0.5):
        r"""__init__(NewmarkSolver self, double beta_=0.25, double gamma_=0.5) -> NewmarkSolver"""
        _ode.NewmarkSolver_swiginit(self, _ode.new_NewmarkSolver(beta_, gamma_))

    def PrintProperties(self, *args, **kwargs):
        r"""PrintProperties(NewmarkSolver self, std::ostream & out=mfem::out)"""
        return _ode.NewmarkSolver_PrintProperties(self, *args, **kwargs)
    PrintProperties = _swig_new_instance_method(_ode.NewmarkSolver_PrintProperties)

    def Init(self, _f):
        r"""Init(NewmarkSolver self, SecondOrderTimeDependentOperator _f)"""
        return _ode.NewmarkSolver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.NewmarkSolver_Init)

    def Step(self, x, dxdt, t, dt):
        r"""Step(NewmarkSolver self, Vector x, Vector dxdt, double & t, double & dt)"""
        return _ode.NewmarkSolver_Step(self, x, dxdt, t, dt)
    Step = _swig_new_instance_method(_ode.NewmarkSolver_Step)
    __swig_destroy__ = _ode.delete_NewmarkSolver

# Register NewmarkSolver in _ode:
_ode.NewmarkSolver_swigregister(NewmarkSolver)

class LinearAccelerationSolver(NewmarkSolver):
    r"""Proxy of C++ mfem::LinearAccelerationSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(LinearAccelerationSolver self) -> LinearAccelerationSolver"""
        _ode.LinearAccelerationSolver_swiginit(self, _ode.new_LinearAccelerationSolver())
    __swig_destroy__ = _ode.delete_LinearAccelerationSolver

# Register LinearAccelerationSolver in _ode:
_ode.LinearAccelerationSolver_swigregister(LinearAccelerationSolver)

class CentralDifferenceSolver(NewmarkSolver):
    r"""Proxy of C++ mfem::CentralDifferenceSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(CentralDifferenceSolver self) -> CentralDifferenceSolver"""
        _ode.CentralDifferenceSolver_swiginit(self, _ode.new_CentralDifferenceSolver())
    __swig_destroy__ = _ode.delete_CentralDifferenceSolver

# Register CentralDifferenceSolver in _ode:
_ode.CentralDifferenceSolver_swigregister(CentralDifferenceSolver)

class FoxGoodwinSolver(NewmarkSolver):
    r"""Proxy of C++ mfem::FoxGoodwinSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(FoxGoodwinSolver self) -> FoxGoodwinSolver"""
        _ode.FoxGoodwinSolver_swiginit(self, _ode.new_FoxGoodwinSolver())
    __swig_destroy__ = _ode.delete_FoxGoodwinSolver

# Register FoxGoodwinSolver in _ode:
_ode.FoxGoodwinSolver_swigregister(FoxGoodwinSolver)

class GeneralizedAlpha2Solver(SecondOrderODESolver):
    r"""Proxy of C++ mfem::GeneralizedAlpha2Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, rho_inf=1.0):
        r"""__init__(GeneralizedAlpha2Solver self, double rho_inf=1.0) -> GeneralizedAlpha2Solver"""
        _ode.GeneralizedAlpha2Solver_swiginit(self, _ode.new_GeneralizedAlpha2Solver(rho_inf))

    def PrintProperties(self, *args, **kwargs):
        r"""PrintProperties(GeneralizedAlpha2Solver self, std::ostream & out=mfem::out)"""
        return _ode.GeneralizedAlpha2Solver_PrintProperties(self, *args, **kwargs)
    PrintProperties = _swig_new_instance_method(_ode.GeneralizedAlpha2Solver_PrintProperties)

    def Init(self, _f):
        r"""Init(GeneralizedAlpha2Solver self, SecondOrderTimeDependentOperator _f)"""
        return _ode.GeneralizedAlpha2Solver_Init(self, _f)
    Init = _swig_new_instance_method(_ode.GeneralizedAlpha2Solver_Init)

    def Step(self, x, dxdt, t, dt):
        r"""Step(GeneralizedAlpha2Solver self, Vector x, Vector dxdt, double & t, double & dt)"""
        return _ode.GeneralizedAlpha2Solver_Step(self, x, dxdt, t, dt)
    Step = _swig_new_instance_method(_ode.GeneralizedAlpha2Solver_Step)
    __swig_destroy__ = _ode.delete_GeneralizedAlpha2Solver

# Register GeneralizedAlpha2Solver in _ode:
_ode.GeneralizedAlpha2Solver_swigregister(GeneralizedAlpha2Solver)

class AverageAccelerationSolver(GeneralizedAlpha2Solver):
    r"""Proxy of C++ mfem::AverageAccelerationSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(AverageAccelerationSolver self) -> AverageAccelerationSolver"""
        _ode.AverageAccelerationSolver_swiginit(self, _ode.new_AverageAccelerationSolver())
    __swig_destroy__ = _ode.delete_AverageAccelerationSolver

# Register AverageAccelerationSolver in _ode:
_ode.AverageAccelerationSolver_swigregister(AverageAccelerationSolver)

class HHTAlphaSolver(GeneralizedAlpha2Solver):
    r"""Proxy of C++ mfem::HHTAlphaSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, alpha=1.0):
        r"""__init__(HHTAlphaSolver self, double alpha=1.0) -> HHTAlphaSolver"""
        _ode.HHTAlphaSolver_swiginit(self, _ode.new_HHTAlphaSolver(alpha))
    __swig_destroy__ = _ode.delete_HHTAlphaSolver

# Register HHTAlphaSolver in _ode:
_ode.HHTAlphaSolver_swigregister(HHTAlphaSolver)

class WBZAlphaSolver(GeneralizedAlpha2Solver):
    r"""Proxy of C++ mfem::WBZAlphaSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, rho_inf=1.0):
        r"""__init__(WBZAlphaSolver self, double rho_inf=1.0) -> WBZAlphaSolver"""
        _ode.WBZAlphaSolver_swiginit(self, _ode.new_WBZAlphaSolver(rho_inf))
    __swig_destroy__ = _ode.delete_WBZAlphaSolver

# Register WBZAlphaSolver in _ode:
_ode.WBZAlphaSolver_swigregister(WBZAlphaSolver)



