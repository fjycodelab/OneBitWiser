"""Run every executable proof and fail if any proof fails."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS = sorted((ROOT / "experiments").glob("**/*.py"))


def main():
    if not EXPERIMENTS:
        raise SystemExit("No experiments found.")

    failures = []
    for experiment in EXPERIMENTS:
        relative_path = experiment.relative_to(ROOT)
        result = subprocess.run(
            [sys.executable, str(experiment)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode == 0:
            print(f"PASS {relative_path}")
            continue

        failures.append(relative_path)
        print(f"FAIL {relative_path}")
        if result.stdout:
            print(result.stdout.rstrip())
        if result.stderr:
            print(result.stderr.rstrip())

    if failures:
        raise SystemExit(f"{len(failures)} experiment(s) failed.")

    print(f"Verified {len(EXPERIMENTS)} experiment(s).")


if __name__ == "__main__":
    main()
