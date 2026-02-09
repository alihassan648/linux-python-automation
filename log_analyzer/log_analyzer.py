import sys
import argparse
import json
from datetime import datetime

# -----------------------------
# Function: analyze_logs
# -----------------------------
def analyze_logs(files):
    total_errors = 0
    total_warnings = 0

    for file_path in files:
        try:
            with open(file_path, "r", errors="ignore") as f:
                for line in f:
                    line = line.lower()
                    if "error" in line:
                        total_errors += 1
                    elif "warning" in line:
                        total_warnings += 1
        except FileNotFoundError:
            print(f"[SKIPPED] {file_path} not found")

    return total_errors, total_warnings

# -----------------------------
# Function: save_report
# -----------------------------
def save_report(errors, warnings):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("report.txt", "w") as report:
        report.write("Log Analysis Report\n")
        report.write("-------------------\n")
        report.write(f"Time     : {timestamp}\n")
        report.write(f"Errors   : {errors}\n")
        report.write(f"Warnings : {warnings}\n")

    print("Report saved to report.txt")

# -----------------------------
# Function: parse_args
# -----------------------------
def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze log files for errors and warnings"
    )

    # Accept one or more log files
    parser.add_argument(
        "logfile",
        nargs="+",
        help="One or more log files"
    )

    parser.add_argument(
        "--errors",
        action="store_true",
        help="Show only error count"
    )

    parser.add_argument(
        "--summary",
        action="store_true",
        help="Show summary report"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output result in JSON format"
    )


    return parser.parse_args()

# -----------------------------
# Main entry point
# -----------------------------
def main():
    args = parse_args()

    errors, warnings = analyze_logs(args.logfile)

    # ONE output decision block
    if args.json:
        output = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "errors": errors,
            "warnings": warnings
        }
        print(json.dumps(output, indent=2))

    elif args.summary:
        save_report(errors, warnings)

    elif args.errors:
        print(f"Errors: {errors}")

    else:
        print(f"Errors   : {errors}")
        print(f"Warnings : {warnings}")

    # Exit code logic (always last)
    if errors > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()

