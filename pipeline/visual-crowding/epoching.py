# %% Import packages

import mne

import matplotlib.pyplot as plt

# Define the file path
PATH_FILE = r"/Users/ma6895/Downloads/PACLab/Arabic Visual Crowding/sub-001/derivatives/sub-001_task-visualcrowdpreview_proc-CALMnoisereduction_meg-raw.fif"

TMAX_ALL=1

# Load the raw data
raw = mne.io.read_raw_fif(PATH_FILE, preload=True)

# Filtering
raw.notch_filter(freqs=[50, 100, 150])
raw.filter(l_freq=1, h_freq=100, fir_design='firwin')




# %% Plot sensors:

fig = mne.viz.plot_sensors(raw.info, kind="3d", show_names=True)
plt.show()



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

# Save name of the picked sensor (motor) for button press activity
# sensor_occipital = 'MEG '

# Plot evoked only for that sensor

evoked[3].plot(picks=sensor_occipital)

evoked[3].plot()




# ----------------------------
# Motor (button-press) onset locked activity - right hand
# ----------------------------

# Pick sensor over left motor cortex (contralateral to right hand)
sensor_motor = 'MEG 115'  # replace with your left motor sensor name if different

# Event type for right-hand button press (replace 2 if different)
evoked_motor = evoked[2]

# Plot motor ERP for that sensor
evoked_motor.plot(picks=sensor_motor, titles='Motor ERP - Left Motor Cortex')




# Check event IDs in your epochs
print("Event IDs in epochs:", epochs.event_id)

# See which event IDs are included in the current evoked (e.g., evoked[1])
condition_index = 1  # change if plotting a different evoked
event_code = evoked[condition_index].comment  # MNE stores the event name in comment
print(f"This evoked response corresponds to condition: {event_code}")

# Optional: check how many trials contributed
print(f"Number of trials for this condition: {len(epochs[event_code])}")

# Loop through all evoked conditions
for i, ev in enumerate(evoked):
    print(f"Plotting evoked for condition: {ev.comment}")
    print(f"Number of trials: {len(epochs[ev.comment])}")

    # Plot the selected sensor (occipital)
    sensor_occipital = 'MEG 193'
    ev.plot(picks=sensor_occipital, titles=f"Condition {ev.comment}")

a=1