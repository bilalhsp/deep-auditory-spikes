import yaml
import numpy as np
from pathlib import Path
from auditory_cortex import neural_data_dir

class RecordingConfig:
    def __init__(self):
        data_dir = neural_data_dir / 'ucsf'
        annotations_path = data_dir / 'sessions_metadata.yml'
        with open(annotations_path, 'r') as f:
            annotations = yaml.safe_load(f)
        self.annotations = annotations

        self.stim_wise_num_repeats = self.annotations['stim_wise_num_repeats']
        self.c_RH_sessions = np.array(self.annotations['c_RH_sessions'])
        self.b_RH_sessions = np.array(self.annotations['b_RH_sessions'])
        self.f_RH_sessions = np.array(self.annotations['f_RH_sessions'])
        self.c_LH_sessions = np.array(self.annotations['c_LH_sessions'])
        
        self.area_wise_sessions = {
            k: np.array(v) for k,v in self.annotations['area_wise_sessions'].items()
        }

        self.bad_sessions = self.annotations['bad_sessions']
        self.session_coordinates = self.annotations['session_coordinates']

        self.subject_wise_sessions = {
        'c': np.concatenate([self.c_RH_sessions, self.c_LH_sessions], axis=0),
        'b': self.b_RH_sessions,
        'f': self.f_RH_sessions
    }