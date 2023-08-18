#include <Python.h>

/**
 * print_python_bytes - print info about python byte string
 * @p: python object struct
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, stop, size = 0;
	char *str;

	if (!(PyBytes_Check(p)))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	size = ((PyVarObject *)p)->ob_size;
	printf("  size: %zd\n", size);
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", str);
	if (size < 10)
	{
		stop = size;
		printf("first %zd bytes:", size + 1);
	}
	else
	{
		stop = 10;
		printf("first 10 bytes:");
	}

	for (i = 0; i < stop; i++)
	{
		printf(" %02hhx", str[i]);
	}
	if (i < 9)
		printf(" %02hhx", str[i]);
	printf("\n");
}

/**
 * print_python_list - print info about python list
 * @p: python list object
 */
void print_python_list(PyObject *p)
{
	PyListObject *pylist;
	PyTypeObject *tp;
	PyObject *el;
	Py_ssize_t i, size = 0, aloc = 0;
	const char *name;

	if (!(PyList_Check(p)))
		return;
	
	printf("[*] Python list info\n");
	pylist = (PyListObject *)p;
	size = PyList_GET_SIZE(pylist);
	aloc = pylist->allocated;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", aloc);

	for (i = 0; i < size; i++)
	{
		el = pylist->ob_item[i];
		tp = (PyTypeObject *)el->ob_type;
		name = tp->tp_name;
		printf("Element %zd: %s\n", i, name);
		if ((PyBytes_Check(el)))
			print_python_bytes(el);
	}
}

