#!/usr/bin/env python
from TOV import *
import matplotlib
import matplotlib.pyplot as plt
import scipy.constants as cst
import scipy.optimize
import numpy as np
import math
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

def unit_test():
    PhiInit = 1
    PsiInit = 0
    option = 2
    radiusMax_in = 40000
    radiusMax_out = 100000
    Npoint = 100000
    log_active = True
    dilaton_active = True
    rho_cen = 500
    rhoInit = rho_cen*cst.eV*10**6/(cst.c**2*cst.fermi**3)
    tov = TOV(rhoInit, PsiInit, PhiInit, radiusMax_in, radiusMax_out, Npoint, option, dilaton_active, log_active)
    tov.ComputeTOV()
    plt.show()


unit_test()
