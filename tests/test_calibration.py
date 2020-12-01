import pytest
import numpy as np
from numpy import testing
import calibration.calibration as calibration

def test_calibration():

    store = calibration.Calibration()

    # cam_mtx will normally be a numpy array with shape (3,3)
    store.cam_mtx = np.random.rand(3,3)
    store.dist_coeff = np.random.rand(3,3)
    store.store()
    
    load = calibration.Calibration()
    load.load()
    
    np.testing.assert_array_equal(store.cam_mtx, load.cam_mtx)
    np.testing.assert_array_equal(store.dist_coeff, load.dist_coeff)