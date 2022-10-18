###############################################################################
# Initial imports:

import matplotlib.pyplot as plt
import h5py
import numpy as np

import pesummary
from pesummary.io import read

file_name = "./data/IGWN-GWTC3p0-v1-GW200112_155838_PEDataRelease_mixed_cosmo.h5"

with h5py.File(file_name, "r") as f:
    # Print all root level object names (aka keys)
    # these can be group or dataset names
    print("Keys: %s" % f.keys())

    print(f['C01:IMRPhenomXPHM'].keys())


file = h5py.File(file_name, "r")


file['C01:IMRPhenomXPHM']['meta_data']['meta_data'].keys()
file['C01:IMRPhenomXPHM']['meta_data']['sampler'].keys()

file_name

data = read(file_name)
samples_dict = data.samples_dict
posterior_samples = samples_dict["C01:Mixed"]
