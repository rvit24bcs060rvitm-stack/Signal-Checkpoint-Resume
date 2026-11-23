import time
import os
import signal_handler

from checkpoint_manager import save_checkpoint, load_checkpoint


def process_batch(total_records=10000, checkpoint_interval=50):

    print("\n================================")
    print("   BATCH PROCESSING ENGINE")
    print("================================")
    print("Process ID:",os.getpid())

    # Register SIGUSR1 handler
    signal_handler.setup_signal_handler()

    completed = load_checkpoint()

    if completed >= total_records:
        print("All records have already been processed!")
        return

    print(f"Total records: {total_records}")
    print(f"Starting from: {completed}")

    while completed < total_records:

        completed += 1

        print(
            f"\rProcessing: {completed}/{total_records}",
            end="",
            flush=True
        )

        # Check for signal-triggered checkpoint
        if signal_handler.consume_checkpoint_request():

            print("\nSaving signal-triggered checkpoint...")

            save_checkpoint(completed, total_records)

            print("Signal checkpoint completed!")

        # Automatic checkpoint
        elif completed % checkpoint_interval == 0:

            print()
            save_checkpoint(completed, total_records)

        time.sleep(0.02)

    # Save final checkpoint
    save_checkpoint(completed, total_records)

    print("\n================================")
    print("BATCH PROCESSING COMPLETED!")
    print("Total processed:", completed)
    print("================================")


if __name__ == "__main__":
    process_batch(total_records=10000)