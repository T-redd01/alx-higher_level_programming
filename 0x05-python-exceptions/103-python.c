#include <Python.h>

void print_python_bytes(PyObject *p)
{
	PyBytesObject *byte_str = NULL;
	Py_ssize_t i, size;

	printf("[.] bytes object info\n");
	if (!(PyBytes_Check(p)))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_str = (PyBytesObject *)p;
	size = ((PyVarObject *)byte_str)->ob_size;
	printf("  size: %zd\n", size);
	printf("  trying string: ");
	for (i = 0; i < size; i++)
		printf("%c", byte_str->ob_sval[i]);
	printf("\n");

	if (size > 10)
		size = 10;
	else
		size = size + 1;
	
	printf("  first %zd bytes: ", size);
	for (i = 0; i < size; i++)
		printf("%02x ", (unsigned char)(byte_str->ob_sval[i]));
	printf("\n");
}

void print_python_float(PyObject *p)
{
	PyFloatObject *float_num;

	printf("[.] float object info\n");
	if (!(PyFloat_Check(p)))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	float_num = (PyFloatObject *)p;
	printf("  value: %f\n", float_num->ob_fval);
}

void print_python_list(PyObject *p)
{
	PyListObject *list = NULL;
	PyObject *item = NULL;
	Py_ssize_t i, size;
	const char *name;

	printf("[*] Python list info\n");
	if (!(PyList_Check(p)))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = ((PyVarObject *)list)->ob_size;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		name = (item->ob_type)->tp_name;
		printf("Element %zd: %s\n", i, name);
		if (!(strcmp(name, "float")))
			print_python_float(item);

		if (!(strcmp(name, "bytes")))
			print_python_bytes(item);
	}
}
