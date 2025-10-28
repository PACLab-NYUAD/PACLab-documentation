
import mne

import matplotlib.pyplot as plt

# Define the file path
PATH_FILE = r"/Users/ma6895/Downloads/PACLab/Arabic Visual Crowding/sub-001/derivatives/sub-001_task-visualcrowdpreview_proc-CALMnoisereduction_meg-raw.fif"

TMAX_ALL=1

# Load the raw data
raw = mne.io.read_raw_fif(PATH_FILE, preload=True)

# Filtering
raw.notch_filter(freqs=[50, 100, 150])
raw.filter(l_freq=2, h_freq=40, fir_design='firwin')


# Plot sensors:

#fig = mne.viz.plot_sensors(raw.info, kind="3d", show_names=True)

#plt.show()



events_file = r"/Users/ma6895/Library/CloudStorage/Box-Box/visual_crowding_preview/derivatives/triggers_to_events/sub-001/sub-001_task-visualcrowdpreview_proc-CALMnoisereduction_desc-autopulses_events.eve"

events = mne.read_events(events_file)

epochs = mne.Epochs(raw,
                    events,
                    baseline=(-0.2,0),
                    tmin=-0.2,
                    tmax=TMAX_ALL,
                    preload=True)
epochs.apply_baseline()
evoked = epochs.average(by_event_type=True)





# Pick sensor from occipital for visual ERP plot:


# Save name of the picked sensor
sensor_occipital = 'MEG 193'

# Plot evoked only for that sensor

evoked[2].plot(picks=sensor_occipital)

a=1