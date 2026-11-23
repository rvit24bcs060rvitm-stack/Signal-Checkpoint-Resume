Signal-Triggered Checkpoint and Resume for Batch Computation

📌 Project Overview

This project implements a checkpoint and recovery mechanism for batch computation using Python. It helps prevent loss of processing progress when a program is interrupted during execution.

The system periodically saves the current processing state to a checkpoint file. If processing is interrupted, the application can restore the saved state and resume from the last checkpoint rather than restarting from the beginning.

The project also supports signal-triggered checkpointing using Linux "SIGUSR1", manual checkpoint requests, checkpoint integrity verification using SHA-256, and a Flask-based dashboard for monitoring processing activity.

---

🎯 Problem Statement

Large batch computations can take considerable time to complete. If a program crashes or is interrupted during execution, the processing progress may be lost, forcing the computation to restart from the beginning.

This project addresses this problem by implementing a reliable checkpointing and recovery mechanism that periodically saves progress, validates checkpoint integrity, and enables computation to resume from the last saved state.

---

🚀 Key Features

- Batch Processing: Processes up to 10,000 records.
- Automatic Checkpointing: Saves progress after every 50 records.
- Manual Checkpointing: Allows users to request a checkpoint through the dashboard.
- Signal-Triggered Checkpointing: Uses Linux "SIGUSR1" to trigger checkpoint saving.
- Resume Capability: Continues processing from the last saved checkpoint.
- Checkpoint Integrity: Uses SHA-256 checksums to validate saved checkpoint data.
- Atomic File Replacement: Helps prevent incomplete checkpoint files during saving.
- Web Dashboard: Provides a visual interface to monitor processing progress.
- Unit Testing: Includes five tests to verify checkpoint and recovery functionality.

---

🛠️ Technologies Used

Technology| Purpose
Python| Core application and batch processing
Flask| Web dashboard and application server
HTML| Dashboard structure
CSS| Dashboard styling
JavaScript| Interactive dashboard functionality
JSON| Checkpoint data storage
Linux Signals| Signal-triggered checkpoint requests
SHA-256| Checkpoint integrity verification
Pytest| Automated testing
Git & GitHub| Version control and project hosting

---

🏗️ Project Structure

Signal-Checkpoint-Resume/
│
├── app.py
├── batch_engine.py
├── checkpoint_manager.py
├── signal_handler.py
├── batch.log
├── requirements.txt
│
├── checkpoints/
│   └── checkpoint.json
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_checkpoint.py

---

⚙️ How It Works

1. The application starts batch processing.
2. Records are processed sequentially.
3. Processing progress is periodically saved in a checkpoint.
4. A manual request or "SIGUSR1" signal can trigger an early checkpoint.
5. The checkpoint data is stored and protected with integrity validation.
6. When processing is restarted, the system loads and validates the saved checkpoint.
7. Processing resumes from the last saved position.
8. The dashboard displays processing information.

---

💻 Installation and Setup

1. Clone the repository

git clone https://github.com/rvit24bcs060rvitm-stack/Signal-Checkpoint-Resume.git

2. Navigate to the project directory

cd Signal-Checkpoint-Resume

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Linux / Ubuntu / WSL:

source venv/bin/activate

Windows:

venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Run the application

python app.py

Open the local Flask address shown in your terminal in a web browser.

---

🧪 Testing

The project includes five unit tests for verifying checkpoint functionality and recovery behavior.

Run the tests using:

python -m pytest -v

Test Results

Result: 5 tests passed

The test suite verifies the implemented checkpoint-related functionality.

---

📊 Project Status

Component| Status
Batch processing| ✅ Completed
Automatic checkpointing| ✅ Implemented
Manual checkpointing| ✅ Implemented
Signal-triggered checkpointing| ✅ Implemented
Resume functionality| ✅ Implemented
SHA-256 validation| ✅ Implemented
Atomic checkpoint saving| ✅ Implemented
Flask dashboard| ✅ Completed
Unit testing| ✅ 5 tests passed

---

🔮 Future Enhancements

- Support for larger datasets and configurable batch sizes.
- Improved dashboard visualizations.
- Detailed checkpoint history and recovery logs.
- Performance monitoring and processing statistics.
- Additional fault-injection and recovery tests.

---

👩‍💻 Author

Developed as an academic project demonstrating batch processing, checkpoint recovery, signal handling, data integrity, and web-based monitoring.

---

📄 License

This project is intended for educational and academic purposes.