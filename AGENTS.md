# Agent Instructions & Context

This file contains important context, history, and instructions for AI agents working in the `PACLab-documentation` repository. Please read this before starting work and update it with any significant new decisions, environments, or findings.

## Environment Setup
*   **Conda Environment:** A Conda virtual environment named `PACLab` was created specifically for this repository.
*   **Key Dependencies:** It includes Python 3.11, `mne`, `matplotlib`, `pyvista`, `numpy`, and `pyqt`.
*   **Usage:** To run scripts like those in `pipeline/visual-crowding/`, ensure the `PACLab` environment is active (`conda activate PACLab`).

## System Context & Limitations
*   **Disk Space Warning:** This Mac's main disk partition frequently runs low on space. Large datasets and temporary caches (like Conda or Pip caches) can fill it quickly. Always clean up caches (`conda clean --all -y` or `pip cache purge`) or verify disk space (`df -h`) before downloading large files or installing heavy packages.

## Ongoing Work / Notes
*   **Pipeline Documentation Updates:** Whenever you make significant progress, modify, or add new steps to the code pipelines (e.g., in `pipeline/visual-crowding/`), you must actively update the corresponding project documentation (`.rst` files in `docs/source/3-projects/`). Make sure to maintain a "Pipeline" section that accurately reports what has been accomplished in the code so far, and clearly outlines the logical next steps.
*(Add future notes, prompt preferences, and architecture decisions here.)*
