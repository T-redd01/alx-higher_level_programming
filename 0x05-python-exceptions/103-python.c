#include <Python.h>

void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	if (!(PyList_Check(p)))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
}

void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!(PyBytes_Check(p)))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
}

void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (!(PyFloat_Check(p)))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
}
