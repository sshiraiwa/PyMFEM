# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _estimators
else:
    import _estimators

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _estimators.SWIG_PyInstanceMethod_New
_swig_new_static_method = _estimators.SWIG_PyStaticMethod_New

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

import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.vector
import mfem._ser.fespace
import mfem._ser.coefficient
import mfem._ser.globals
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.symmat
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.fe_base
import mfem._ser.fe_fixed_order
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.fe_h1
import mfem._ser.fe_nd
import mfem._ser.fe_rt
import mfem._ser.fe_l2
import mfem._ser.fe_nurbs
import mfem._ser.fe_pos
import mfem._ser.fe_ser
import mfem._ser.mesh
import mfem._ser.sort_pairs
import mfem._ser.ncmesh
import mfem._ser.gridfunc
import mfem._ser.bilininteg
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.linearform
import mfem._ser.nonlininteg
import mfem._ser.vertex
import mfem._ser.vtk
import mfem._ser.doftrans
import mfem._ser.handle
import mfem._ser.restriction
import mfem._ser.bilinearform
class AbstractErrorEstimator(object):
    r"""Proxy of C++ mfem::AbstractErrorEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _estimators.delete_AbstractErrorEstimator

    def __init__(self):
        r"""__init__(AbstractErrorEstimator self) -> AbstractErrorEstimator"""
        _estimators.AbstractErrorEstimator_swiginit(self, _estimators.new_AbstractErrorEstimator())

# Register AbstractErrorEstimator in _estimators:
_estimators.AbstractErrorEstimator_swigregister(AbstractErrorEstimator)

class ErrorEstimator(AbstractErrorEstimator):
    r"""Proxy of C++ mfem::ErrorEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetTotalError(self):
        r"""GetTotalError(ErrorEstimator self) -> double"""
        return _estimators.ErrorEstimator_GetTotalError(self)
    GetTotalError = _swig_new_instance_method(_estimators.ErrorEstimator_GetTotalError)

    def GetLocalErrors(self):
        r"""GetLocalErrors(ErrorEstimator self) -> Vector"""
        return _estimators.ErrorEstimator_GetLocalErrors(self)
    GetLocalErrors = _swig_new_instance_method(_estimators.ErrorEstimator_GetLocalErrors)

    def Reset(self):
        r"""Reset(ErrorEstimator self)"""
        return _estimators.ErrorEstimator_Reset(self)
    Reset = _swig_new_instance_method(_estimators.ErrorEstimator_Reset)
    __swig_destroy__ = _estimators.delete_ErrorEstimator

# Register ErrorEstimator in _estimators:
_estimators.ErrorEstimator_swigregister(ErrorEstimator)

class AnisotropicErrorEstimator(ErrorEstimator):
    r"""Proxy of C++ mfem::AnisotropicErrorEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetAnisotropicFlags(self):
        r"""GetAnisotropicFlags(AnisotropicErrorEstimator self) -> intArray"""
        return _estimators.AnisotropicErrorEstimator_GetAnisotropicFlags(self)
    GetAnisotropicFlags = _swig_new_instance_method(_estimators.AnisotropicErrorEstimator_GetAnisotropicFlags)
    __swig_destroy__ = _estimators.delete_AnisotropicErrorEstimator

# Register AnisotropicErrorEstimator in _estimators:
_estimators.AnisotropicErrorEstimator_swigregister(AnisotropicErrorEstimator)

class ZienkiewiczZhuEstimator(AnisotropicErrorEstimator):
    r"""Proxy of C++ mfem::ZienkiewiczZhuEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def SetWithCoeff(self, w_coeff=True):
        r"""SetWithCoeff(ZienkiewiczZhuEstimator self, bool w_coeff=True)"""
        return _estimators.ZienkiewiczZhuEstimator_SetWithCoeff(self, w_coeff)
    SetWithCoeff = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_SetWithCoeff)

    def SetAnisotropic(self, aniso=True):
        r"""SetAnisotropic(ZienkiewiczZhuEstimator self, bool aniso=True)"""
        return _estimators.ZienkiewiczZhuEstimator_SetAnisotropic(self, aniso)
    SetAnisotropic = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_SetAnisotropic)

    def SetFluxAveraging(self, fa):
        r"""SetFluxAveraging(ZienkiewiczZhuEstimator self, int fa)"""
        return _estimators.ZienkiewiczZhuEstimator_SetFluxAveraging(self, fa)
    SetFluxAveraging = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_SetFluxAveraging)

    def GetTotalError(self):
        r"""GetTotalError(ZienkiewiczZhuEstimator self) -> double"""
        return _estimators.ZienkiewiczZhuEstimator_GetTotalError(self)
    GetTotalError = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_GetTotalError)

    def GetLocalErrors(self):
        r"""GetLocalErrors(ZienkiewiczZhuEstimator self) -> Vector"""
        return _estimators.ZienkiewiczZhuEstimator_GetLocalErrors(self)
    GetLocalErrors = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_GetLocalErrors)

    def GetAnisotropicFlags(self):
        r"""GetAnisotropicFlags(ZienkiewiczZhuEstimator self) -> intArray"""
        return _estimators.ZienkiewiczZhuEstimator_GetAnisotropicFlags(self)
    GetAnisotropicFlags = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_GetAnisotropicFlags)

    def Reset(self):
        r"""Reset(ZienkiewiczZhuEstimator self)"""
        return _estimators.ZienkiewiczZhuEstimator_Reset(self)
    Reset = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_Reset)
    __swig_destroy__ = _estimators.delete_ZienkiewiczZhuEstimator

    def __init__(self, integ, sol, flux_fes, own_flux_fes=False):
        r"""__init__(ZienkiewiczZhuEstimator self, BilinearFormIntegrator integ, GridFunction sol, FiniteElementSpace flux_fes, bool own_flux_fes=False) -> ZienkiewiczZhuEstimator"""

        if own_flux_fes: flux_fes.thisown=0


        _estimators.ZienkiewiczZhuEstimator_swiginit(self, _estimators.new_ZienkiewiczZhuEstimator(integ, sol, flux_fes, own_flux_fes))

# Register ZienkiewiczZhuEstimator in _estimators:
_estimators.ZienkiewiczZhuEstimator_swigregister(ZienkiewiczZhuEstimator)

class LpErrorEstimator(ErrorEstimator):
    r"""Proxy of C++ mfem::LpErrorEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(LpErrorEstimator self, int p, GridFunction sol) -> LpErrorEstimator
        __init__(LpErrorEstimator self, int p, Coefficient coef, GridFunction sol) -> LpErrorEstimator
        __init__(LpErrorEstimator self, int p, VectorCoefficient coef, GridFunction sol) -> LpErrorEstimator
        """
        _estimators.LpErrorEstimator_swiginit(self, _estimators.new_LpErrorEstimator(*args))

    def SetLocalErrorNormP(self, p):
        r"""SetLocalErrorNormP(LpErrorEstimator self, int p)"""
        return _estimators.LpErrorEstimator_SetLocalErrorNormP(self, p)
    SetLocalErrorNormP = _swig_new_instance_method(_estimators.LpErrorEstimator_SetLocalErrorNormP)

    def SetCoef(self, *args):
        r"""
        SetCoef(LpErrorEstimator self, Coefficient A)
        SetCoef(LpErrorEstimator self, VectorCoefficient A)
        """
        return _estimators.LpErrorEstimator_SetCoef(self, *args)
    SetCoef = _swig_new_instance_method(_estimators.LpErrorEstimator_SetCoef)

    def Reset(self):
        r"""Reset(LpErrorEstimator self)"""
        return _estimators.LpErrorEstimator_Reset(self)
    Reset = _swig_new_instance_method(_estimators.LpErrorEstimator_Reset)

    def GetLocalErrors(self):
        r"""GetLocalErrors(LpErrorEstimator self) -> Vector"""
        return _estimators.LpErrorEstimator_GetLocalErrors(self)
    GetLocalErrors = _swig_new_instance_method(_estimators.LpErrorEstimator_GetLocalErrors)
    __swig_destroy__ = _estimators.delete_LpErrorEstimator

# Register LpErrorEstimator in _estimators:
_estimators.LpErrorEstimator_swigregister(LpErrorEstimator)

class KellyErrorEstimator(ErrorEstimator):
    r"""Proxy of C++ mfem::KellyErrorEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(KellyErrorEstimator self, BilinearFormIntegrator di_, GridFunction sol_, FiniteElementSpace flux_fes_, intArray attributes_=mfem::Array< int >()) -> KellyErrorEstimator
        __init__(KellyErrorEstimator self, BilinearFormIntegrator di_, GridFunction sol_, FiniteElementSpace flux_fes_, intArray attributes_=mfem::Array< int >()) -> KellyErrorEstimator
        """
        _estimators.KellyErrorEstimator_swiginit(self, _estimators.new_KellyErrorEstimator(*args))
    __swig_destroy__ = _estimators.delete_KellyErrorEstimator

    def GetLocalErrors(self):
        r"""GetLocalErrors(KellyErrorEstimator self) -> Vector"""
        return _estimators.KellyErrorEstimator_GetLocalErrors(self)
    GetLocalErrors = _swig_new_instance_method(_estimators.KellyErrorEstimator_GetLocalErrors)

    def Reset(self):
        r"""Reset(KellyErrorEstimator self)"""
        return _estimators.KellyErrorEstimator_Reset(self)
    Reset = _swig_new_instance_method(_estimators.KellyErrorEstimator_Reset)

    def GetTotalError(self):
        r"""GetTotalError(KellyErrorEstimator self) -> double"""
        return _estimators.KellyErrorEstimator_GetTotalError(self)
    GetTotalError = _swig_new_instance_method(_estimators.KellyErrorEstimator_GetTotalError)

    def SetElementCoefficientFunction(self, compute_element_coefficient_):
        r"""SetElementCoefficientFunction(KellyErrorEstimator self, mfem::KellyErrorEstimator::ElementCoefficientFunction compute_element_coefficient_)"""
        return _estimators.KellyErrorEstimator_SetElementCoefficientFunction(self, compute_element_coefficient_)
    SetElementCoefficientFunction = _swig_new_instance_method(_estimators.KellyErrorEstimator_SetElementCoefficientFunction)

    def SetFaceCoefficientFunction(self, compute_face_coefficient_):
        r"""SetFaceCoefficientFunction(KellyErrorEstimator self, mfem::KellyErrorEstimator::FaceCoefficientFunction compute_face_coefficient_)"""
        return _estimators.KellyErrorEstimator_SetFaceCoefficientFunction(self, compute_face_coefficient_)
    SetFaceCoefficientFunction = _swig_new_instance_method(_estimators.KellyErrorEstimator_SetFaceCoefficientFunction)

    def ResetCoefficientFunctions(self):
        r"""ResetCoefficientFunctions(KellyErrorEstimator self)"""
        return _estimators.KellyErrorEstimator_ResetCoefficientFunctions(self)
    ResetCoefficientFunctions = _swig_new_instance_method(_estimators.KellyErrorEstimator_ResetCoefficientFunctions)

# Register KellyErrorEstimator in _estimators:
_estimators.KellyErrorEstimator_swigregister(KellyErrorEstimator)



