# Make an MNE script that logs the .fif file
# Use MNE functions to plot the headshape with the sensors

# In OPM sensor space coordinates, the (0, 0, 0) correspond to the center of the helmet
# (x, y, z)

# The x-axis is right to left
# The y-axis is anterior to posterior
# the z-axis is superior to inferior
# the x-axis increases from left to right
# the y-axis increases from posterior to anterior
# the z-axis increases from inferior to superior
# therefore it is a RAS coordinate system



import mne
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pyvista as pv
import numpy as np

mne.viz.set_3d_backend('pyvistaqt')  # force PyVista Qt backend for 3D plots


# Option to add sensor names as labels
add_labels = False  # Set to True to display labels

# Define the file path
PATH_FILE = r"/Users/ma6895/Downloads/PACLab/Arabic Visual Crowding/sub-001/derivatives/sub-001_task-visualcrowdpreview_proc-CALMnoisereduction_meg-raw.fif"


# Load the raw data
raw = mne.io.read_raw_fif(PATH_FILE, preload=False)

# Plot the sensors and retrieve the Matplotlib figure
# Set show_names=False to prevent default labeling
fig = mne.viz.plot_sensors(raw.info, kind="3d")
#fig = mne.viz.plot_sensors(raw.info, kind='3d', show_names=False, show=False)

# Get the current 3D Axes from the figure
ax = fig.gca()

plt.show()


fig = mne.viz.plot_alignment(raw.info,
                             show_axes=True,
                             dig=True,      # show digitized points
                             eeg=False,     # if you only have MEG
                             meg='helmet',

                             )  # optional: show head surface


# ---------- Customize sensors ----------
# Extract MEG sensor positions
# Extract MEG sensor locations
meg_locs = np.array([ch['loc'][:3] for ch in raw.info['chs']
                     if ch['kind'] == mne.io.constants.FIFF.FIFFV_MEG_CH])

# ---------- Plot sensors as visible points ----------
# Create a PyVista point cloud
points = pv.PolyData(meg_locs)
fig.plotter.add_points(points, color='red', point_size=15, render_points_as_spheres=True)


# ---------- Show and save ----------
fig.plotter.show()
fig.plotter.screenshot('headshape_sensors.png')
print(f"Figure saved to")