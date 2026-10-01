import hashlib
import subprocess
import time
from datetime import datetime
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

CHECK_INTERVAL = 2
WAIT_SECONDS = 30


def git(*args):
    """Run a Git command and return its output."""
    result = subprocess.run(
        ["git"] + list(args),
        cwd=str(PROJECT_DIR),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=60
    )

    if result.returncode != 0:
        error = result.stderr.decode("utf-8", errors="replace")
        output = result.stdout.decode("utf-8", errors="replace")
        raise RuntimeError(error.strip() or output.strip())

    return result.stdout


def get_snapshot():
    """Calculate the current state using file names and contents."""
    status = git("status", "--porcelain", "-z", "--", "*.py")

    files = git(
        "ls-files", "-z",
        "--cached", "--others", "--exclude-standard",
        "--", "*.py"
    )

    digest = hashlib.sha256()
    digest.update(status)

    for name in sorted(set(files.split(b"\0"))):
        if not name:
            continue

        digest.update(name)
        path = PROJECT_DIR / name.decode(
            "utf-8", errors="surrogateescape"
        )

        if path.is_file():
            digest.update(path.read_bytes())

    return digest.hexdigest(), bool(status)


def main():
    print("Auto backup start: {}".format(PROJECT_DIR))
    print("Python files will be uploaded 30 seconds after the last change.")
    print("Press Ctrl+C to exit.")

    last_snapshot = None
    changed_at = time.monotonic()

    pending_push = True
    next_push_at = 0

    while True:
        try:
            snapshot, has_changes = get_snapshot()
            now = time.monotonic()

            if snapshot != last_snapshot:
                last_snapshot = snapshot
                changed_at = now

                if has_changes:
                    print("[Detected] Changed. Wait for 30 seconds.")

            if has_changes and now - changed_at >= WAIT_SECONDS:
                git("add", "-A", "--", "*.py")

                message = "Auto backup: {}".format(
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )

                git("commit", "--only", "-m", message, "--", "*.py")

                print("[Commit] {}".format(message))
                pending_push = True
                next_push_at = 0

                last_snapshot, _ = get_snapshot()

            if pending_push and time.monotonic() >= next_push_at:
                next_push_at = time.monotonic() + WAIT_SECONDS

                git("push", "origin", "main")
                pending_push = False

                print("[Complete] GitHub upload success")

        except (RuntimeError, OSError, subprocess.TimeoutExpired) as error:
            print("[ERROR] {}".format(error))
            changed_at = time.monotonic()

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAuto backup exit.")        
