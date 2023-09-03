#include <python.h>

void print_python_string(PyObject *p)
{
	Py_ssize_t len = 0;
	const char *string = NULL;

	printf("[.] string object info\n");
	if (!(PyUnicode_Check(p)))
	{
		printf("[ERROR] Invalid String Object\n");
		return;
	}

	printf("  type: ");
	if (PyUnicode _IS_COMPACT_ASCII(p))
		printf("compact ascii\n");
	else if (PyUnicode_IS_COMPACT(p))
		printf("compact unicode object\n");
	else
		printf("UNKNOWN\n");

	len = PyUnicode_GET_LENGTH(p);
	printf("length: %zd\n", len);

	string = PyUnicode_AsUTF8AndSize(p, NULL);
	printf("value: ");
	if (string)
		printf("%s\n", string);
}
