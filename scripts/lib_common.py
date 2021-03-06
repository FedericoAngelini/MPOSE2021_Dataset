from init_vars import paths
import os
import pickle
import pandas as pd
import numpy as np

def read_poses(path=paths['pose']):
    report = pd.DataFrame(columns=['sample', 'dataset', 'lenght', 'aver_conf'])
    data = dict()
    frames = dict()
    for i in os.listdir(path):
        with open(os.path.join(path, i), 'rb') as f:
            d = pickle.load(f)
        report = report.append({'sample': d['sample'],
                                'dataset': d['dataset'],
                                'actor': d['actor'],
                                'action': d['action'],
                                'length': d['length'],
                                'aver_conf': np.nanmean(d['seq'][:, 2, :])}, ignore_index=True)
        data[i] = d['seq']
        frames[i] = d['frames']

    return report, data, frames
