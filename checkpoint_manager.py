import os
import json
import hashlib
import tempfile


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHECKPOINT_DIR = os.path.join(BASE_DIR, "checkpoints")
CHECKPOINT_FILE = os.path.join(CHECKPOINT_DIR, "checkpoint.json")


def calculate_checksum(data):
    """Generate checksum to validate checkpoint data."""
    content = json.dumps(data, sort_keys=True).encode("utf-8")
    return hashlib.sha256(content).hexdigest()


def save_checkpoint(completed, total):
    """Save progress safely using atomic file replacement."""

    os.makedirs(CHECKPOINT_DIR, exist_ok=True)

    data = {
        "completed": completed,
        "total": total
    }

    checkpoint = {
        "version": 1,
        "data": data,
        "checksum": calculate_checksum(data)
    }

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=CHECKPOINT_DIR,
            delete=False
        ) as temp_file:

            temp_path = temp_file.name

            json.dump(checkpoint, temp_file, indent=4)
            temp_file.flush()
            os.fsync(temp_file.fileno())

        os.replace(temp_path, CHECKPOINT_FILE)

        # Ensure the directory entry is also flushed.
        dir_fd = os.open(CHECKPOINT_DIR, os.O_RDONLY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)

        print("Checkpoint saved successfully!")

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)


def load_checkpoint():
    """Load and validate the last checkpoint."""

    if not os.path.exists(CHECKPOINT_FILE):
        print("No checkpoint found. Starting from beginning.")
        return 0

    try:
        with open(CHECKPOINT_FILE, "r", encoding="utf-8") as file:
            checkpoint = json.load(file)

        if checkpoint.get("version") != 1:
            raise ValueError("Unsupported checkpoint version")

        data = checkpoint["data"]

        completed = data["completed"]
        total = data["total"]

        if (
            not isinstance(completed, int)
            or isinstance(completed, bool)
            or not isinstance(total, int)
            or isinstance(total, bool)
            or total < 0
            or completed < 0
            or completed > total
        ):
            raise ValueError("Invalid progress values")

        expected_checksum = calculate_checksum(data)

        if checkpoint["checksum"] != expected_checksum:
            raise ValueError("Checkpoint checksum mismatch")

        print("Checkpoint validated successfully!")
        print(f"Resuming from record: {completed}")

        return completed

    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print("Checkpoint validation failed:", error)
        print("Starting from the beginning.")
        return 0