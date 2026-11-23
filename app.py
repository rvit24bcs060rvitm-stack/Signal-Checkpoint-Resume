from flask import Flask, render_template, jsonify
import threading
import time

from checkpoint_manager import save_checkpoint, load_checkpoint
from signal_handler import setup_signal_handler, consume_checkpoint_request

app = Flask(__name__)

TOTAL = 10000
INTERVAL = 50

completed = 0
running = False
manual_checkpoint_requested = False
logs = []

lock = threading.Lock()


def add_log(message):
    with lock:
        logs.append(message)
        if len(logs) > 50:
            logs.pop(0)


def batch_worker():
    global completed, running, manual_checkpoint_requested

    with lock:
        running = True

    add_log("Batch processing started.")

    try:
        while True:
            time.sleep(0.02)

            with lock:
                if not running or completed >= TOTAL:
                    break

                completed += 1
                current = completed

                manual_request = manual_checkpoint_requested
                manual_checkpoint_requested = False

            signal_request = consume_checkpoint_request()

            if (
                manual_request
                or signal_request
                or current % INTERVAL == 0
            ):
                save_checkpoint(current, TOTAL)
                add_log(f"Checkpoint saved at record {current}.")

        if current >= TOTAL:
            add_log("Batch processing completed.")

    finally:
        with lock:
            running = False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/status")
def status():
    with lock:
        current = completed
        active = running
        activity = list(logs)

    return jsonify({
        "total": TOTAL,
        "completed": current,
        "remaining": TOTAL - current,
        "percentage": round(current / TOTAL * 100, 2),
        "running": active,
        "logs": activity
    })


@app.route("/api/start", methods=["POST"])
def start():
    global completed

    with lock:
        if running:
            return jsonify({"message": "Already processing"})

        if completed >= TOTAL:
            completed = load_checkpoint()

        if completed >= TOTAL:
            return jsonify({"message": "All records completed"})

        worker = threading.Thread(target=batch_worker, daemon=True)
        worker.start()

    return jsonify({"message": "Processing started"})


@app.route("/api/checkpoint", methods=["POST"])
def request_checkpoint():
    global manual_checkpoint_requested

    with lock:
        if not running:
            return jsonify({"message": "Processing is not running"})

        manual_checkpoint_requested = True

    return jsonify({"message": "Checkpoint requested"})


@app.route("/api/resume", methods=["POST"])
def resume():
    global completed

    with lock:
        if running:
            return jsonify({"message": "Already processing"})

        completed = load_checkpoint()

    return start()


if __name__ == "__main__":
    completed = load_checkpoint()
    setup_signal_handler()
    app.run(debug=False, use_reloader=False)