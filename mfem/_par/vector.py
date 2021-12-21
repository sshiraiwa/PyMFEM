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
    from . import _vector
else:
    import _vector

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _vector.SWIG_PyInstanceMethod_New
_swig_new_static_method = _vector.SWIG_PyStaticMethod_New

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


import mfem._par.array
import mfem._par.mem_manager

def add_vector(*args):
    r"""
    add_vector(Vector v1, Vector v2, Vector v)
    add_vector(Vector v1, double alpha, Vector v2, Vector v)
    add_vector(double const a, Vector x, Vector y, Vector z)
    add_vector(double const a, Vector x, double const b, Vector y, Vector z)
    """
    return _vector.add_vector(*args)
add_vector = _vector.add_vector

def subtract_vector(*args):
    r"""
    subtract_vector(Vector v1, Vector v2, Vector v)
    subtract_vector(double const a, Vector x, Vector y, Vector z)
    """
    return _vector.subtract_vector(*args)
subtract_vector = _vector.subtract_vector

def CheckFinite(v, n):
    r"""CheckFinite(double const * v, int const n) -> int"""
    return _vector.CheckFinite(v, n)
CheckFinite = _vector.CheckFinite

def infinity():
    r"""infinity() -> double"""
    return _vector.infinity()
infinity = _vector.infinity
class Vector(object):
    r"""Proxy of C++ mfem::Vector class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def UseDevice(self, *args):
        r"""
        UseDevice(Vector self, bool use_dev)
        UseDevice(Vector self) -> bool
        """
        return _vector.Vector_UseDevice(self, *args)
    UseDevice = _swig_new_instance_method(_vector.Vector_UseDevice)

    def Load(self, *args):
        r"""
        Load(Vector self, std::istream ** _in, int np, int * dim)
        Load(Vector self, std::istream & _in, int Size)
        Load(Vector self, std::istream & _in)
        """
        return _vector.Vector_Load(self, *args)
    Load = _swig_new_instance_method(_vector.Vector_Load)

    def SetSize(self, *args):
        r"""
        SetSize(Vector self, int s)
        SetSize(Vector self, int s, mfem::MemoryType mt)
        SetSize(Vector self, int s, Vector v)
        """
        return _vector.Vector_SetSize(self, *args)
    SetSize = _swig_new_instance_method(_vector.Vector_SetSize)

    def SetData(self, d):
        r"""SetData(Vector self, double * d)"""
        return _vector.Vector_SetData(self, d)
    SetData = _swig_new_instance_method(_vector.Vector_SetData)

    def SetDataAndSize(self, d, s):
        r"""SetDataAndSize(Vector self, double * d, int s)"""
        return _vector.Vector_SetDataAndSize(self, d, s)
    SetDataAndSize = _swig_new_instance_method(_vector.Vector_SetDataAndSize)

    def NewDataAndSize(self, d, s):
        r"""NewDataAndSize(Vector self, double * d, int s)"""
        return _vector.Vector_NewDataAndSize(self, d, s)
    NewDataAndSize = _swig_new_instance_method(_vector.Vector_NewDataAndSize)

    def NewMemoryAndSize(self, mem, s, own_mem):
        r"""NewMemoryAndSize(Vector self, mfem::Memory< double > const & mem, int s, bool own_mem)"""
        return _vector.Vector_NewMemoryAndSize(self, mem, s, own_mem)
    NewMemoryAndSize = _swig_new_instance_method(_vector.Vector_NewMemoryAndSize)

    def MakeRef(self, *args):
        r"""
        MakeRef(Vector self, Vector base, int offset, int size)
        MakeRef(Vector self, Vector base, int offset)
        """
        return _vector.Vector_MakeRef(self, *args)
    MakeRef = _swig_new_instance_method(_vector.Vector_MakeRef)

    def MakeDataOwner(self):
        r"""MakeDataOwner(Vector self)"""
        return _vector.Vector_MakeDataOwner(self)
    MakeDataOwner = _swig_new_instance_method(_vector.Vector_MakeDataOwner)

    def Destroy(self):
        r"""Destroy(Vector self)"""
        return _vector.Vector_Destroy(self)
    Destroy = _swig_new_instance_method(_vector.Vector_Destroy)

    def DeleteDevice(self, copy_to_host=True):
        r"""DeleteDevice(Vector self, bool copy_to_host=True)"""
        return _vector.Vector_DeleteDevice(self, copy_to_host)
    DeleteDevice = _swig_new_instance_method(_vector.Vector_DeleteDevice)

    def Size(self):
        r"""Size(Vector self) -> int"""
        return _vector.Vector_Size(self)
    Size = _swig_new_instance_method(_vector.Vector_Size)

    def Capacity(self):
        r"""Capacity(Vector self) -> int"""
        return _vector.Vector_Capacity(self)
    Capacity = _swig_new_instance_method(_vector.Vector_Capacity)

    def GetData(self):
        r"""GetData(Vector self) -> double *"""
        return _vector.Vector_GetData(self)
    GetData = _swig_new_instance_method(_vector.Vector_GetData)

    def begin(self, *args):
        r"""
        begin(Vector self) -> double
        begin(Vector self) -> double const *
        """
        return _vector.Vector_begin(self, *args)
    begin = _swig_new_instance_method(_vector.Vector_begin)

    def end(self, *args):
        r"""
        end(Vector self) -> double
        end(Vector self) -> double const *
        """
        return _vector.Vector_end(self, *args)
    end = _swig_new_instance_method(_vector.Vector_end)

    def GetMemory(self, *args):
        r"""
        GetMemory(Vector self) -> mfem::Memory< double >
        GetMemory(Vector self) -> mfem::Memory< double > const &
        """
        return _vector.Vector_GetMemory(self, *args)
    GetMemory = _swig_new_instance_method(_vector.Vector_GetMemory)

    def SyncMemory(self, v):
        r"""SyncMemory(Vector self, Vector v)"""
        return _vector.Vector_SyncMemory(self, v)
    SyncMemory = _swig_new_instance_method(_vector.Vector_SyncMemory)

    def SyncAliasMemory(self, v):
        r"""SyncAliasMemory(Vector self, Vector v)"""
        return _vector.Vector_SyncAliasMemory(self, v)
    SyncAliasMemory = _swig_new_instance_method(_vector.Vector_SyncAliasMemory)

    def OwnsData(self):
        r"""OwnsData(Vector self) -> bool"""
        return _vector.Vector_OwnsData(self)
    OwnsData = _swig_new_instance_method(_vector.Vector_OwnsData)

    def StealData(self, *args):
        r"""
        StealData(Vector self, double ** p)
        StealData(Vector self) -> double *
        """
        return _vector.Vector_StealData(self, *args)
    StealData = _swig_new_instance_method(_vector.Vector_StealData)

    def Elem(self, *args):
        r"""
        Elem(Vector self, int i) -> double
        Elem(Vector self, int i) -> double const &
        """
        return _vector.Vector_Elem(self, *args)
    Elem = _swig_new_instance_method(_vector.Vector_Elem)

    def __call__(self, *args):
        r"""
        __call__(Vector self, int i) -> double
        __call__(Vector self, int i) -> double const &
        """
        return _vector.Vector___call__(self, *args)
    __call__ = _swig_new_instance_method(_vector.Vector___call__)

    def __mul__(self, *args):
        r"""
        __mul__(Vector self, double const * arg2) -> double
        __mul__(Vector self, Vector v) -> double
        """
        return _vector.Vector___mul__(self, *args)
    __mul__ = _swig_new_instance_method(_vector.Vector___mul__)

    def __imul__(self, v):
        ret = _vector.Vector___imul__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0            
        return self



    def __itruediv__(self, v):
        ret = _vector.Vector___itruediv__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0      
        return self



    def __isub__(self, v):
        ret = _vector.Vector___isub__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0            
        return self



    def __iadd__(self, v):
        ret = _vector.Vector___iadd__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0                  
        return self



    def Add(self, a, Va):
        r"""Add(Vector self, double const a, Vector Va) -> Vector"""
        return _vector.Vector_Add(self, a, Va)
    Add = _swig_new_instance_method(_vector.Vector_Add)

    def Set(self, a, x):
        r"""Set(Vector self, double const a, Vector x) -> Vector"""
        return _vector.Vector_Set(self, a, x)
    Set = _swig_new_instance_method(_vector.Vector_Set)

    def SetVector(self, v, offset):
        r"""SetVector(Vector self, Vector v, int offset)"""
        return _vector.Vector_SetVector(self, v, offset)
    SetVector = _swig_new_instance_method(_vector.Vector_SetVector)

    def Neg(self):
        r"""Neg(Vector self)"""
        return _vector.Vector_Neg(self)
    Neg = _swig_new_instance_method(_vector.Vector_Neg)

    def Swap(self, other):
        r"""Swap(Vector self, Vector other)"""
        return _vector.Vector_Swap(self, other)
    Swap = _swig_new_instance_method(_vector.Vector_Swap)

    def median(self, lo, hi):
        r"""median(Vector self, Vector lo, Vector hi)"""
        return _vector.Vector_median(self, lo, hi)
    median = _swig_new_instance_method(_vector.Vector_median)

    def GetSubVector(self, *args):
        r"""
        GetSubVector(Vector self, intArray dofs, Vector elemvect)
        GetSubVector(Vector self, intArray dofs, double * elem_data)
        """
        return _vector.Vector_GetSubVector(self, *args)
    GetSubVector = _swig_new_instance_method(_vector.Vector_GetSubVector)

    def SetSubVector(self, *args):
        r"""
        SetSubVector(Vector self, intArray dofs, double const value)
        SetSubVector(Vector self, intArray dofs, Vector elemvect)
        SetSubVector(Vector self, intArray dofs, double * elem_data)
        """
        return _vector.Vector_SetSubVector(self, *args)
    SetSubVector = _swig_new_instance_method(_vector.Vector_SetSubVector)

    def AddElementVector(self, *args):
        r"""
        AddElementVector(Vector self, intArray dofs, Vector elemvect)
        AddElementVector(Vector self, intArray dofs, double * elem_data)
        AddElementVector(Vector self, intArray dofs, double const a, Vector elemvect)
        """
        return _vector.Vector_AddElementVector(self, *args)
    AddElementVector = _swig_new_instance_method(_vector.Vector_AddElementVector)

    def SetSubVectorComplement(self, dofs, val):
        r"""SetSubVectorComplement(Vector self, intArray dofs, double const val)"""
        return _vector.Vector_SetSubVectorComplement(self, dofs, val)
    SetSubVectorComplement = _swig_new_instance_method(_vector.Vector_SetSubVectorComplement)

    def PrintHash(self, out):
        r"""PrintHash(Vector self, std::ostream & out)"""
        return _vector.Vector_PrintHash(self, out)
    PrintHash = _swig_new_instance_method(_vector.Vector_PrintHash)

    def Randomize(self, seed=0):
        r"""Randomize(Vector self, int seed=0)"""
        return _vector.Vector_Randomize(self, seed)
    Randomize = _swig_new_instance_method(_vector.Vector_Randomize)

    def Norml2(self):
        r"""Norml2(Vector self) -> double"""
        return _vector.Vector_Norml2(self)
    Norml2 = _swig_new_instance_method(_vector.Vector_Norml2)

    def Normlinf(self):
        r"""Normlinf(Vector self) -> double"""
        return _vector.Vector_Normlinf(self)
    Normlinf = _swig_new_instance_method(_vector.Vector_Normlinf)

    def Norml1(self):
        r"""Norml1(Vector self) -> double"""
        return _vector.Vector_Norml1(self)
    Norml1 = _swig_new_instance_method(_vector.Vector_Norml1)

    def Normlp(self, p):
        r"""Normlp(Vector self, double p) -> double"""
        return _vector.Vector_Normlp(self, p)
    Normlp = _swig_new_instance_method(_vector.Vector_Normlp)

    def Max(self):
        r"""Max(Vector self) -> double"""
        return _vector.Vector_Max(self)
    Max = _swig_new_instance_method(_vector.Vector_Max)

    def Min(self):
        r"""Min(Vector self) -> double"""
        return _vector.Vector_Min(self)
    Min = _swig_new_instance_method(_vector.Vector_Min)

    def Sum(self):
        r"""Sum(Vector self) -> double"""
        return _vector.Vector_Sum(self)
    Sum = _swig_new_instance_method(_vector.Vector_Sum)

    def DistanceSquaredTo(self, p):
        r"""DistanceSquaredTo(Vector self, double const * p) -> double"""
        return _vector.Vector_DistanceSquaredTo(self, p)
    DistanceSquaredTo = _swig_new_instance_method(_vector.Vector_DistanceSquaredTo)

    def DistanceTo(self, p):
        r"""DistanceTo(Vector self, double const * p) -> double"""
        return _vector.Vector_DistanceTo(self, p)
    DistanceTo = _swig_new_instance_method(_vector.Vector_DistanceTo)

    def CheckFinite(self):
        r"""CheckFinite(Vector self) -> int"""
        return _vector.Vector_CheckFinite(self)
    CheckFinite = _swig_new_instance_method(_vector.Vector_CheckFinite)
    __swig_destroy__ = _vector.delete_Vector

    def Read(self, on_dev=True):
        r"""Read(Vector self, bool on_dev=True) -> double const *"""
        return _vector.Vector_Read(self, on_dev)
    Read = _swig_new_instance_method(_vector.Vector_Read)

    def HostRead(self):
        r"""HostRead(Vector self) -> double const *"""
        return _vector.Vector_HostRead(self)
    HostRead = _swig_new_instance_method(_vector.Vector_HostRead)

    def Write(self, on_dev=True):
        r"""Write(Vector self, bool on_dev=True) -> double *"""
        return _vector.Vector_Write(self, on_dev)
    Write = _swig_new_instance_method(_vector.Vector_Write)

    def HostWrite(self):
        r"""HostWrite(Vector self) -> double *"""
        return _vector.Vector_HostWrite(self)
    HostWrite = _swig_new_instance_method(_vector.Vector_HostWrite)

    def ReadWrite(self, on_dev=True):
        r"""ReadWrite(Vector self, bool on_dev=True) -> double *"""
        return _vector.Vector_ReadWrite(self, on_dev)
    ReadWrite = _swig_new_instance_method(_vector.Vector_ReadWrite)

    def HostReadWrite(self):
        r"""HostReadWrite(Vector self) -> double *"""
        return _vector.Vector_HostReadWrite(self)
    HostReadWrite = _swig_new_instance_method(_vector.Vector_HostReadWrite)

    def __init__(self, *args):
        r"""
        __init__(Vector self) -> Vector
        __init__(Vector self, Vector arg2) -> Vector
        __init__(Vector self, Vector v) -> Vector
        __init__(Vector self, int s) -> Vector
        __init__(Vector self, double * data_, int size_) -> Vector
        __init__(Vector self, Vector base, int base_offset, int size_) -> Vector
        __init__(Vector self, int size_, mfem::MemoryType mt) -> Vector
        __init__(Vector self, int size_, mfem::MemoryType h_mt, mfem::MemoryType d_mt) -> Vector
        __init__(Vector self, Vector v, int offset, int size) -> Vector
        """

        from numpy import ndarray, ascontiguousarray
        keep_link = False
        own_data = False  
        if len(args) == 1:
            if isinstance(args[0], list): 
                args = (args[0], len(args[0]))
                own_data = True	  
            elif isinstance(args[0], ndarray):
                if args[0].dtype != 'float64':
                    raise ValueError('Must be float64 array ' + str(args[0].dtype) +
        			     ' is given')  
                else:
                    args = (ascontiguousarray(args[0]), args[0].shape[0])
        # in this case, args[0] need to be maintained
        # in this object.
                    keep_link = True


        _vector.Vector_swiginit(self, _vector.new_Vector(*args))

        if keep_link:
           self._link_to_data = args[0]
        if own_data:
           self.MakeDataOwner()




    def Assign(self, *args):
        r"""
        Assign(Vector self, double const v)
        Assign(Vector self, Vector v)
        Assign(Vector self, PyObject * param)
        """

        from numpy import ndarray, ascontiguousarray, array
        keep_link = False
        if len(args) == 1:
            if isinstance(args[0], ndarray):
                if args[0].dtype != 'float64':
                     raise ValueError('Must be float64 array ' + str(args[0].dtype) +
        			      ' is given')
                elif args[0].ndim != 1:
                    raise ValueError('Ndim must be one') 
                elif args[0].shape[0] != _vector.Vector_Size(self):
                    raise ValueError('Length does not match')
                else:
                    args = (ascontiguousarray(args[0]),)
            elif isinstance(args[0], tuple):
                args = (array(args[0], dtype = float),)      
            elif isinstance(args[0], list):	      
                args = (array(args[0], dtype = float),)      
            else:
                pass


        val = _vector.Vector_Assign(self, *args)

        return self


        return val


    def __setitem__(self, i, v):
        r"""__setitem__(Vector self, int i, double const v)"""
        return _vector.Vector___setitem__(self, i, v)
    __setitem__ = _swig_new_instance_method(_vector.Vector___setitem__)

    def __getitem__(self, param):
        r"""__getitem__(Vector self, PyObject * param) -> PyObject *"""
        return _vector.Vector___getitem__(self, param)
    __getitem__ = _swig_new_instance_method(_vector.Vector___getitem__)

    def GetDataArray(self):
        r"""GetDataArray(Vector self) -> PyObject *"""
        return _vector.Vector_GetDataArray(self)
    GetDataArray = _swig_new_instance_method(_vector.Vector_GetDataArray)

    def WriteToStream(self, StringIO, width=8):
        r"""WriteToStream(Vector self, PyObject * StringIO, int width=8) -> PyObject *"""
        return _vector.Vector_WriteToStream(self, StringIO, width)
    WriteToStream = _swig_new_instance_method(_vector.Vector_WriteToStream)

    def Print(self, *args):
        r"""
        Print(Vector self, std::ostream & out=mfem::out, int width=8)
        Print(Vector self, char const * file, int precision=16)
        """
        return _vector.Vector_Print(self, *args)
    Print = _swig_new_instance_method(_vector.Vector_Print)

    def PrintGZ(self, file, precision=16):
        r"""PrintGZ(Vector self, char const * file, int precision=16)"""
        return _vector.Vector_PrintGZ(self, file, precision)
    PrintGZ = _swig_new_instance_method(_vector.Vector_PrintGZ)

    def Print_HYPREGZ(self, file, precision=16):
        r"""Print_HYPREGZ(Vector self, char const * file, int precision=16)"""
        return _vector.Vector_Print_HYPREGZ(self, file, precision)
    Print_HYPREGZ = _swig_new_instance_method(_vector.Vector_Print_HYPREGZ)

    def Print_HYPRE(self, *args):
        r"""
        Print_HYPRE(Vector self, std::ostream & out)
        Print_HYPRE(Vector self, char const * file, int precision=16)
        Print_HYPRE(Vector self)
        """
        return _vector.Vector_Print_HYPRE(self, *args)
    Print_HYPRE = _swig_new_instance_method(_vector.Vector_Print_HYPRE)

# Register Vector in _vector:
_vector.Vector_swigregister(Vector)


def IsFinite(val):
    r"""IsFinite(double const & val) -> bool"""
    return _vector.IsFinite(val)
IsFinite = _vector.IsFinite

def DistanceSquared(x, y, n):
    r"""DistanceSquared(double const * x, double const * y, int const n) -> double"""
    return _vector.DistanceSquared(x, y, n)
DistanceSquared = _vector.DistanceSquared

def Distance(x, y, n):
    r"""Distance(double const * x, double const * y, int const n) -> double"""
    return _vector.Distance(x, y, n)
Distance = _vector.Distance

Vector.__idiv__ = Vector.__itruediv__



