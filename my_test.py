from omsi.dataformat.omsi_file import *
from omsi.analysis.findpeaks.omsi_findpeaks_global import omsi_findpeaks_global
from omsi.analysis.multivariate_stats.omsi_nmf import omsi_nmf

# f = omsi_file('C:\\Users\\2017v\\Desktop\\Research\\Bhattacharya\\NIMS\\data\\Flax_Pod_12_day_old_CS.h5' , 'r')
f = omsi_file('C:\\Users\\2017v\\Desktop\\Research\\Bhattacharya\\NIMS\\data\\Brain.h5' , 'r')
d = f.get_experiment(0).get_msidata(0)

print(d)

# Specify the analysis workflow
# Create a global peak finding analysis
a1 = omsi_findpeaks_global()      # Create the analysis
# Create an NMF that processes our peak cube
a2 = omsi_nmf()

# Define the inputs of the global peak finder
a1['msidata'] = d                 # Set the input msidata
a1['mzdata'] = d.mz               # Set the input mz data
# Define the inputs of the NMF
a2['msidata'] = a1['peak_cube']   # Set the input data to the peak cube
a2['numIter'] = 2                 # Set input to perform 2 iterations only

a1.execute()

peak_cube = a1['peak_cube']

# # Plot the first three peak images
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

print("Plotting example peak finding analysis results")
shape_x = peak_cube.shape[0]
shape_y = peak_cube.shape[1]
ho1 = peak_cube[:, :, 0]
ho2 = peak_cube[:, :, 0]
ho3 = peak_cube[:, :, 0]

main_figure = plt.figure()
figure_grid_spec = gridspec.GridSpec(1, 4)
image_figure = main_figure.add_subplot(figure_grid_spec[0])
image_figure.autoscale(True, 'both', tight=True)
_ = image_figure.pcolor(np.log(ho1 + 1))

image_figure = main_figure.add_subplot(figure_grid_spec[1])
image_figure.autoscale(True, 'both', tight=True)
_ = image_figure.pcolor(np.log(ho2 + 1))

image_figure = main_figure.add_subplot(figure_grid_spec[2])
image_figure.autoscale(True, 'both', tight=True)
_ = image_figure.pcolor(np.log(ho3 + 1))

# do the three color
ho = np.zeros(shape=(shape_x, shape_y, 3))
temp = np.log(peak_cube[:, :, 0] + 1)
temp = temp - temp.min()
temp = temp / temp.max()
ho[:, :, 0] = temp

temp = np.log(peak_cube[:, :, 1] + 1)
temp = temp - temp.min()
temp = temp / temp.max()
ho[:, :, 1] = temp

temp = np.log(peak_cube[:, :, 2] + 1)
temp = temp - temp.min()
temp = temp / temp.max()
ho[:, :, 2] = temp

image_figure = main_figure.add_subplot(figure_grid_spec[3])
image_figure.autoscale(True, 'both', tight=True)
_ = image_figure.imshow(ho)

plt.show()