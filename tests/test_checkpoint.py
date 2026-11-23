import os
import json
import unittest

from checkpoint_manager import (
    save_checkpoint,
    load_checkpoint,
    CHECKPOINT_FILE
)


class CheckpointTests(unittest.TestCase):

    def setUp(self):
        os.makedirs("checkpoints", exist_ok=True)

        if os.path.exists(CHECKPOINT_FILE):
            os.remove(CHECKPOINT_FILE)

    def tearDown(self):
        if os.path.exists(CHECKPOINT_FILE):
            os.remove(CHECKPOINT_FILE)

    def test_save_checkpoint(self):
        save_checkpoint(50, 100)

        self.assertEqual(load_checkpoint(), 50)

        print("\nPASS: Checkpoint saved successfully")

    def test_resume_checkpoint(self):
        save_checkpoint(75, 100)

        progress = load_checkpoint()

        self.assertEqual(progress, 75)

        print("\nPASS: Resume from saved progress")

    def test_missing_checkpoint(self):
        progress = load_checkpoint()

        self.assertEqual(progress, 0)

        print("\nPASS: Missing checkpoint handled")

    def test_corrupted_checkpoint(self):

        with open(CHECKPOINT_FILE, "w") as file:
            file.write("{invalid json")

        progress = load_checkpoint()

        self.assertEqual(progress, 0)

        print("\nPASS: Corrupted checkpoint detected")

    def test_invalid_checksum(self):

        save_checkpoint(50, 100)

        with open(CHECKPOINT_FILE, "r") as file:
            data = json.load(file)

        data["checksum"] = "invalid_checksum"

        with open(CHECKPOINT_FILE, "w") as file:
            json.dump(data, file)

        progress = load_checkpoint()

        self.assertEqual(progress, 0)

        print("\nPASS: Invalid checksum detected")


if __name__ == "__main__":
    unittest.main()