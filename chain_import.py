###############################################################################
# Initial imports:

import h5py
import numpy as np
from getdist.mcsamples import MCSamples

import pesummary
from pesummary.gw.plots.latex_labels import GWlatex_labels

###############################################################################
# Utility to parse GW chains to getdist:


def samples_from_GW_data(file_name, settings=None):
    """

    """
    # get the data:
    with h5py.File(file_name, "r") as file:
        temp_samples = file['C01:IMRPhenomXPHM']['posterior_samples'][()]
    # parse parameter names:
    param_names = list(temp_samples.dtype.fields.keys())
    # parse samples:
    samples = np.array(temp_samples.view((float, len(temp_samples.dtype.names))))
    loglikes = -temp_samples['log_likelihood']
    # get labels:
    labels = []
    for _name in param_names:
        if _name in GWlatex_labels.keys():
            labels.append(GWlatex_labels[_name])
        else:
            labels.append(_name)
    # initialize the samples:
    mc_samples = MCSamples(samples=samples,
                           loglikes=loglikes,
                           sampler='mcmc', names=param_names,
                           labels=labels,
                           ignore_rows=0,
                           settings=settings)
    #
    return mc_samples


"""
file_name = "./data/IGWN-GWTC3p0-v1-GW200112_155838_PEDataRelease_mixed_nocosmo.h5"
samples_from_GW_data(file_name)

file = h5py.File(file_name, "r")


for f in file['C01:IMRPhenomXPHM'].keys(): print(f)

for f in file['C01:IMRPhenomXPHM']['posterior_samples'].keys(): print(f)


for f in file['C01:IMRPhenomXPHM']['priors'].keys(): print(f)

for f in file['C01:IMRPhenomXPHM']['priors']['analytic'].keys(): print(f)
for f in file['C01:IMRPhenomXPHM']['priors']['calibration'].keys(): print(f)
for f in file['C01:IMRPhenomXPHM']['priors']['samples'].keys(): print(f)


prior_samples_names = list(file['C01:IMRPhenomXPHM']['priors']['samples'].keys())


for name in param_names:
    if name in file['C01:IMRPhenomXPHM']['priors']['analytic'].keys():
        print(file['C01:IMRPhenomXPHM']['priors']['analytic'][name][()][0])
    else:
        print('Parameter not found: ', name)
    if name in prior_samples_names:
        print('** name in samples')



prior_samples_names



plt.hist(file['C01:IMRPhenomXPHM']['posterior_samples'][param_names[0]][()])
plt.hist(file['C01:IMRPhenomXPHM']['priors']['samples'][param_names[0]][()])


len(param_names)

list(file['C01:IMRPhenomXPHM']['priors']['analytic'].values())[0][()]

for i in file['C01:IMRPhenomXPHM']['priors']['analytic']: print(i)


for i in file['C01:IMRPhenomXPHM']['meta_data']['sampler']: print(i)

for i in file['C01:IMRPhenomXPHM']['meta_data']['other']: print(i)

for i in file['C01:IMRPhenomXPHM']['meta_data']['meta_data']['f_final']: print(i)

for i in file['C01:IMRPhenomXPHM']['calibration_envelope']: print(i, file['C01:IMRPhenomXPHM']['calibration_envelope'][i][()])




file['C01:IMRPhenomXPHM']['priors']['analytic'].keys()
file['C01:IMRPhenomXPHM']['priors']['analytic'].items()


for f in file['C01:IMRPhenomXPHM']['description'].keys(): print(f)


file['C01:IMRPhenomXPHM']['meta_data']['meta_data'].keys()
file['C01:IMRPhenomXPHM']['meta_data']['sampler'].keys()

file_name

data = read(file_name)
samples_dict = data.samples_dict
posterior_samples = samples_dict["C01:Mixed"]
"""
