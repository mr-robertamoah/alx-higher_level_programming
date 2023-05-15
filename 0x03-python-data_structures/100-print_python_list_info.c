#include <Python.h>

/**
* print_python_list_info - print information
* about python object
* @p: PyOject
*/
void print_python_list_info(PyObject *p)
{
	int size = 0, i = 0;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = ", size);
	printf("[*] Allocated = ", ((PyListObject *)p)->allocated);

	while (i < size)
	{
		printf("Element %d: ", i)
		obj = PyList_GetItem(p, i);
		printf("%s\n", ((Py_TYPE(obj))->tp_name);
		i++;
	}
}
