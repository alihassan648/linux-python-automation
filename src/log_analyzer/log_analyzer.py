#!/usr/bin/env python3

import sys
import argparse
import json
from datetime import datetime
from pathlib import Path

# ----------------------------
# Log Analysis Functions
# ----------------------------

def analyze_logs(files):
    """
    Analyze multiple log files and count errors and warnings.
    """
    total_errors = 0
    total_warnings = 0

    for file_path in files:
        path = Path(file_path)
        if not path.exists():
            print(f"[SKIPPED] {file_path} not found")
            continue

        try:
            with path.open("r", errors="ignore") as f:
                for line in f:
                    line = line.lower()
                    if "error" in line:
                        total_errors += 1
                    elif "warning" in line:
                        total_warnings += 1

        except Exception as e:
            print(f"[ERROR] Failed to read {file_path}: {e}")

    return total_errors, total_warnings


def save_report(errors, warnings, filename="report.txt"):
    """
    Save a human-readable report to a file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w") as report:
        report.write("Log Analysis Report\n")
        report.write("-------------------\n")
        report.write(f"Time     : {timestamp}\n")
        report.write(f"Errors   : {errors}\n")
        report.write(f"Warnings : {warnings}\n")
    print(f"Report saved to {filename}")


# ----------------------------
# CLI Argument Parser
# ----------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze one or more log files for errors and warnings"
    )

    parser.add_argument(
        "logfile",
        nargs="+",  # Accept multiple log files
        help="Path(s) to log file(s)"
    )

    parser.add_argument(
        "--errors",
        action="store_true",
        help="Show only error count"
    )

    parser.add_argument(
        "--summary",
        action="store_true",
        help="Save summary report to report.txt"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format"
    )

    return parser.parse_args()


# ----------------------------
# Main Function
# ----------------------------

def main():
    args = parse_args()

    errors, warnings = analyze_logs(args.logfile)

    # JSON output has priority
    if args.json:
        output = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "errors": errors,
            "warnings": warnings
        }
        print(json.dumps(output, indent=2))

    # Summary report
    if args.summary:
        save_report(errors, warnings)

    # Error count only
    if args.errors and not args.json:
        print(f"Errors: {errors}")

    # Default human-readable output if no flags
    if not (args.json or args.summary or args.errors):
        print(f"Errors   : {errors}")
        print(f"Warnings : {warnings}")

    # Exit code for automation
    sys.exit(1 if errors > 0 else 0)


# ----------------------------
# Entry Point
# ----------------------------

if __name__ == "__main__":
    main()
