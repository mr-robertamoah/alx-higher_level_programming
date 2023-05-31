#include "Python.h"

/**
* print_python_list - print basic info about PyListObject
* @p: PyObject
*/
void print_python_list(PyObject *p)
{
	PyListObject *pList = NULL;
	Py_ssize_t size = 0;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	pList = (PyListObject *) p;
	size = pList->ob_size;
}

/**
* print_python_bytes- print basic info about PyBytesObject
* @p: PyObject
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *pBytes = NULL;
	Py_ssize_t size = 0;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	pBytes = (PyBytesObject *) p;
	size = pBytes->ob_size;

}

/**
* print_python_float - print basic info about PyFloatObject
* @p: PyObject
*/
void print_python_float(PyObject *p)
{
	PyFloatObject *pFloat = NULL;
	Py_ssize_t size = 0;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	pFloat = (PyFloatObject *) p;
	size = pFloat->ob_size;

}
