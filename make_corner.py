import matplotlib.pyplot as plt
import pesummary
from pesummary.io import read
import h5py
import numpy as np
import corner
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import shapiro, normaltest, anderson

file_name = "../data/IGWN-GWTC3p0-v1-GW200112_155838_PEDataRelease_mixed_cosmo.h5"

data = read(file_name)
samples_dict = data.samples_dict
posterior_samples = samples_dict["C01:Mixed"]
parameters = posterior_samples.parameters

per_pdf = 5

for ind in range(0, len(parameters), per_pdf):
    fig = posterior_samples.plot(type="corner", parameters=parameters[ind:ind+per_pdf])
    fig.savefig(f"./plots/corner{ind}.pdf")
    fig.close()

