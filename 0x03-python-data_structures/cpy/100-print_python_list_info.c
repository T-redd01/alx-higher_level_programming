#include <stdio.h>
#include <Python.h>
/*#include <object.h>
#include <listobject.h>*/

void print_python_list_info(PyObject *p)
{
	if (!(PyList_Check(p)))
		return;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", sizeof(p));
}

