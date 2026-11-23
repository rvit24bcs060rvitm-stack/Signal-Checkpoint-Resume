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
