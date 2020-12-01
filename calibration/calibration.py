import json
import numpy as np

DEFAULT_FILENAME = 'calibration.json'

class Calibration:
    def __init__(self):
        """
        docstring
        """
        self.filename = DEFAULT_FILENAME
        self.cam_mtx = np.array([])
        self.dist_coeff = np.array([])
        self.src_pts = []
        self.dst_pts = []


    def store(self):
        """
        """

        data = {
            'camera_matrix': self.cam_mtx.tolist(),
            'dist_coeff': self.dist_coeff.tolist(),
            'src_pts': self.src_pts,
            'dst_pts': self.dst_pts
        }
        
        with open(self.filename, "w") as f:
            json.dump(data, f)

        print('Calibration parameters stored in: {0}'.format(self.filename))

    def load(self):
        """
        docstring
        """
        with open(self.filename, "r") as f:
            data = json.load(f)
            
            self.cam_mtx = np.array(data['camera_matrix'])
            self.dist_coeff = np.array(data['dist_coeff'])
            self.src_pts = data['src_pts']
            self.dst_pts = data['dst_pts']
