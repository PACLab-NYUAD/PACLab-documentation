
import mne



# Define the file path
PATH_FILE = r"/Users/ma6895/Downloads/PACLab/Arabic Visual Crowding/sub-001/derivatives/sub-001_task-visualcrowdpreview_proc-CALMnoisereduction_meg-raw.fif"


# Load the raw data
raw = mne.io.read_raw_fif(PATH_FILE, preload=False)

events_file = r"/Users/ma6895/Library/CloudStorage/Box-Box/visual_crowding_preview/derivatives/triggers_to_events/sub-001/sub-001_task-visualcrowdpreview_proc-CALMnoisereduction_desc-autopulses_events.eve"

events = mne.read_events(events_file)

epochs = mne.Epochs(raw,
                    events,
                    baseline=(-0.2,0),
                    tmin=-0.2,
                    tmax=6,
                    preload=True)

evoked = epochs.average(by_event_type=True)

a=1