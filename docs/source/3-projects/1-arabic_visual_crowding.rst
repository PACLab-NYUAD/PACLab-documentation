Arabic Visual Crowding
======================

**Visual word crowding** is the inability to view a stimulus distinctly when presented in a clutter. Crowding impairs the ability to discriminate word features and contours among flankers, which in turn impairs people's ability to respond appropriately to the target stimulus.

Overview
--------

One of the most powerful capacities of the human brain is the ability to detect regularities and contextual clues in the environment and to use that learning to predict future events. Many recent theories recognize a central role for prediction in brain function. Historically, however, research in perception and word reading has started from a more passive model, using experimental paradigms in which words or other visual stimuli suddenly appear at the center of gaze. In recent years, Melcher and others have developed new paradigms to study the role of prediction in more naturalistic viewing conditions, in which people move their eyes to look at stimuli of interest, as we do normally while reading or looking around. In particular, we developed a combined behavioral, eye-tracking and neuroimaging paradigm to study the “preview effect”, in which the fact that we see a stimulus peripherally in the “corner of the eye” dramatically influences the neural processing of that item when we look at it. These neural measures allow us to characterize how prediction and the preview increases the efficiency of neural processing.
In this context, the role of previewing a word with peripheral vision while reading in Arabic is a particularly interesting research question. Considering the number of speakers of the language, Arabic is surprisingly under-studied compared to other languages. Thus, most theories of word reading and the recent developments in the study of the role of prediction in reading are based mainly on Latin script languages. Arabic words are visually different in theoretically important ways, in particular since short vowels and long (or geminated) consonants are not typically written (unless diacritic marks are included, such as in children’s books), the letters are mainly connected and can change shape based on word position, with some letters differentiated only by the presence or number of dots. Arabic letters in words are more visually “crowded” together, which might reduce the ability to gain a useful preview from peripheral vision. In addition, the reading direction is different which provides a critical test of common theories of brain lateralization for language processing.
In the proposed research, we will investigate the role of prediction in reading Arabic words, including (1) the magnitude of the preview effect and its neural correlates, (2) how this is related to the basic visual properties of the script, (3) the influence of expertise, and (4) how preview effects with the Arabic script compare with other recently reported preview effects.


This project investigates how visual properties of Arabic script, such as ligatures, crowding, and intra-letter spacing, affect reading efficiency, and how reading performance is influenced by formal education and proficiency in Arabic.
Using a 4x4 experimental design, participants viewed target words presented either to the left or right of a central fixation point.
Each word appeared with either a valid preview (the correct word) or an invalid preview (a flipped or altered version of the word).
Participants were instructed to fixate on the central point and make a saccade to the target word when cued, after which they judged whether the word matched the previous one.

The study employs both magnetoencephalography (MEG) and eye-tracking to measure neural responses and eye movements during reading.
Stimuli were carefully balanced across conditions to test the effects of crowding, ligatures, and intra-letter spacing while controlling for word length and frequency.

Research questions include:
1. How do crowding and the number of ligatures influence the preview effect in reading Arabic?
2. How does intra-letter spacing affect reading speed and accuracy?
3. How do Arabic proficiency, fluency, and nativity modulate reading performance and associated brain activity?

This design allows investigation of both behavioural and neural mechanisms underlying reading, which will provide insight into how visual and linguistic factors interact in the processing of Arabic script.


Highlights
----------

-

Pipeline
--------

**Current Progress**
Based on the initial scripts in `pipeline/visual-crowding/`, the following steps have been implemented for individual subject analysis:

1. **Data Loading & Filtering**: 
   - Loading raw MEG data (`.fif` files) after initial CALM noise reduction.
   - Applying notch filters (50, 100, 150 Hz) and a bandpass filter (1-100 Hz) to remove environmental and high-frequency noise.
2. **Co-registration & Visualization**: 
   - Generating 3D plots of MEG sensors and aligning them with the participant's digitized headshape to verify sensor positions.
3. **Epoching**: 
   - Extracting trials based on event triggers (`.eve` files).
   - Defining epochs from -200 ms to 1000 ms relative to stimulus onset, with baseline correction applied (-200 ms to 0 ms).
4. **Evoked Responses (ERPs)**: 
   - Computing average evoked fields across different experimental conditions.
   - Visualizing specific sensor activity, including occipital sensors (for visual responses) and motor sensors (locked to button-press activity).

**Next Steps**
To advance the MEG analysis pipeline, the following stages should be considered:

1. **Artifact Rejection**: Implement Independent Component Analysis (ICA) or Signal Space Projection (SSP) to systematically clean heartbeat (ECG) and eye-movement (EOG) artifacts.
2. **Time-Frequency Analysis**: Examine induced oscillatory activity (e.g., changes in alpha/gamma band power) to understand the dynamics of the crowding and preview effects.
3. **Source Localization**: Co-register MEG data with structural MRI scans to reconstruct the neural activity in source space, identifying the specific cortical regions involved.
4. **Group-Level Statistics**: Generalize the single-subject pipeline to handle multiple subjects and apply robust statistical methods (e.g., cluster-based permutation tests) across conditions.
5. **Multivariate Pattern Analysis (MVPA)**: Implement decoding models to investigate how the neural representations of Arabic words change under different crowding and preview conditions.

Team
----

- Prof. David Melcher - Principal Investigator
- Maitha AlShaali - Kawader Research Fellow
- Tasnim Ezzeddin - Masters Graduate
- Hadi Zaatiti - MEG Research Scientist
