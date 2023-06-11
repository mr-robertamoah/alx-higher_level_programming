#!/usr/bin/python3

"""
Multiply to matrices using numpy

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two list of lists containing integers and floats

    Args:
        m_a (list of lists): list of lists containing ints and floats
        m_b (list of lists): list of lists containing ints and floats
    Returns:
        list of lists containing ints and floats
    """
    return (np.matmul(m_a, m_b))
