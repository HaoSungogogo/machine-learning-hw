"""Computes the cost function for an arbitrary number of features."""

__author__="Jesse Lord"
__date__="January 8, 2015"

import numpy as np

def computeCost(X,y,theta):
    m=len(y)
    J = sum((np.dot(theta,X)-y)*(np.dot(theta,X)-y))/(2.0*m)
    # initial result returns 32.07 as expected from the homework
    return J
