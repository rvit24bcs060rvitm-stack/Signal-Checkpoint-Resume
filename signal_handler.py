import signal

# Global flag
checkpoint_requested = False


def handle_checkpoint_signal(signum, frame):
    """
    Signal handler.
    Only sets a flag.
    File operations are handled later
    by the main processing loop.
    """
    global checkpoint_requested
    checkpoint_requested = True


def setup_signal_handler():

    signal.signal(signal.SIGUSR1, handle_checkpoint_signal)

    print("Signal handler registered successfully!")
    print("Send SIGUSR1 to request an early checkpoint.")


def consume_checkpoint_request():
    """
    Check and reset the checkpoint request flag.
    """
    global checkpoint_requested

    if checkpoint_requested:
        checkpoint_requested = False
        return True

    return False