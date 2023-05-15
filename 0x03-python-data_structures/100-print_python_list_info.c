#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
* print_python_list_info - print information
* about python object
* @p: PyOject
*/
void print_python_list_info(PyObject *p)
{
	long int size = 0;
	int i = 0;
	PyObject *obj;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %l\n", size);
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

	while (i < size)
	{
		printf("Element %d: ", i)
		obj = PyList_GetItem(p, i);
		printf("%s\n", ((Py_TYPE(obj->ob_item[i]))->tp_name);
		i++;
	}
}
