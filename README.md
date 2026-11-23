Signal-Triggered Checkpoint and Resume for Batch Computation

Project Overview

This project implements a checkpoint and recovery mechanism for batch computation using Python. It is designed to prevent loss of processing progress when a program is interrupted.

The application periodically saves the current processing state into a checkpoint file. If execution stops unexpectedly, the system can validate the saved checkpoint and resume processing from the last saved position instead of restarting from the beginning.

It also supports signal-triggered checkpointing using Linux "SIGUSR1", manual checkpoint requests, and a web-based dashboard for monitoring processing progress.


Problem Statement

Large batch computations may take considerable time to complete. If a process crashes, is interrupted, or stops unexpectedly, the processed work may be lost and the computation may need to restart.

This project addresses the problem by implementing a reliable checkpointing and recovery mechanism that saves progress, validates checkpoint integrity, and enables processing to resume efficiently.

## Key Features

1. Batch processing of large datasets.
2. Automatic checkpoint creation.
3. Signal-triggered checkpoint saving using SIGUSR1.
4. Resume processing from the last saved checkpoint.
5. Checkpoint validation using SHA-256 checksum.
6. Safe checkpoint storage using atomic file replacement.
7. Web-based monitoring dashboard.
8. Unit testing for checkpoint recovery.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Linux Signals
- JSON
- SHA-256

## Testing

The project includes five unit tests to verify checkpoint functionality.

Run tests using:

python -m pytest -v

Result: 5 tests passed.

## Project Status

- Batch processing: Completed
- Automatic checkpoint: Implemented
- Manual checkpoint: Implemented
- Signal-based checkpoint: Implemented
- Resume functionality: Implemented
- Flask dashboard: Implemented
- Checkpoint validation using SHA-256: Implemented
- Unit testing: 5 tests passed
