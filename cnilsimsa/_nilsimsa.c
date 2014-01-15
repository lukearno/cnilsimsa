/* nilsimsa.c - A C implementation of Nilsimsa for Python. */

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

#include <Python.h>


unsigned char popcount[256];


static void fillpopcount(void) {
  int i, j;
  memset(popcount, 0, sizeof(popcount));
  for (i = 0; i < 256; i++) {
    for (j = 0; j < 8; j++) {
      popcount[i] += 1 & (i >> j);
    }
  }
}


int native_compare_hexdigest(char *a, char *b) {
  int i, ia, ib, bits = 0;
  char ha[3] = "  \0", hb[3] = "  \0";
  for (i = 0; i < 63; i += 2) {
    memcpy(ha, &a[i], 2);
    memcpy(hb, &b[i], 2);
    ia = strtol(&ha[0], NULL, 16);
    ib = strtol(&hb[0], NULL, 16);
    bits += popcount[255 & (ia ^ ib)];
  }
  return 128 - bits;
}


static PyObject * compare_hexdigests(PyObject * self, PyObject * args) {
  char *a, *b;
  int *a_len, *b_len;
  int i;
  if (!PyArg_ParseTuple(args, "s#s#", &a, &a_len, &b, &b_len)) {
    PyErr_SetString(PyExc_ValueError, "64 character hex digests required");
    return NULL;
  }
  if (!(a_len == 64 && b_len == 64)) {
    PyErr_SetString(PyExc_ValueError, "64 character hex digests required");
    return NULL;
  }
  i = native_compare_hexdigest(a, b);
  return Py_BuildValue("i", i);
}


static char _nilsimsa_docs[] =
  "compare_hexdigest(digest1, digest2): similarity score -128 to 128\n";


static PyMethodDef _nilsimsa_funcs[] = {
  {"compare_hexdigests",
   (PyCFunction) compare_hexdigests,
   METH_VARARGS,
   _nilsimsa_docs},
  {NULL}
};


void init_nilsimsa(void) {
  fillpopcount();
  Py_InitModule3("_nilsimsa", _nilsimsa_funcs,
		 "Python C nilsimsa extension module.");
}
