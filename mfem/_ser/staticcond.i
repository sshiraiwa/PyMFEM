%module(package="mfem._ser")  staticcond
%{
#include "mfem.hpp"  
#include "pyoperator.hpp"        
#include "numpy/arrayobject.h"
#include "../common/pycoefficient.hpp"  
%}

%init %{
import_array();
%}

%include "exception.i"
%import "fespace.i"

%include "fem/staticcond.hpp"
