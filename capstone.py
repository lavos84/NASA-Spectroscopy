# import relevant libraries
import numpy as np
import matplotlib.pyplot as plt

# read in the data
filenames = ["./Data/Win0.clean1.contsub_Jy.rest.scom.c.txt",
             "./Data/Win1.clean1.contsub_Jy.rest.scom.c.txt",
             "./Data/Win2.clean1.contsub_Jy.rest.scom.c.txt",
             "./Data/Win3.clean1.contsub_Jy.rest.scom.c.txt"]
# 'data' will be a 4 element list, with each element representing the data from 1 text file
data = [np.loadtxt(f) for f in filenames]

# Recreate the plot from Cordiner et. al. 2015, Figure 1
fig, axs = plt.subplots(2, 2, figsize = (10, 6))
for index, ax in enumerate(axs.flat):
    # Plot each data set
    ax.plot(data[index][:,0],
            data[index][:,1],
            linewidth = 0.25)
    ax.set(ylabel = "Flux (Jy)")
    ax.set(xlabel = "Frequency (GHz)")
    # Clean up the xticks
    ax.set_xticks(np.arange(round(data[index][0,0], 1), round(data[index][-1,0], 1), step = 0.5))
    # Remove the space from the borders of the plot along the X axis
    ax.autoscale(enable = True, axis = 'x', tight = True)
# Add some space between the plots
plt.subplots_adjust(hspace = .3, wspace = .3)
plt.show()
