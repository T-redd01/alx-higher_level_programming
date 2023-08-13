#include <stdio.h>
#include <Python.h>
/*#include <object.h>
#include <listobject.h>*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size = 0, alloced = 0;
	PyObject *item;
	const char *tp;

	if (!(PyList_Check(p)))
		return;

	size = PyList_Size(p);
	alloced = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloced);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		tp = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", tp);
	}
}

