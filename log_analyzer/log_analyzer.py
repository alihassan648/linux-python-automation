import sys
from datetime import datetime

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


def save_report(errors, warnings):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("report.txt", "w") as report:
        report.write("Log Analysis Report\n")
        report.write("-------------------\n")
        report.write(f"Time     : {timestamp}\n")
        report.write(f"Errors   : {errors}\n")
        report.write(f"Warnings : {warnings}\n")

    print("Report saved to report.txt")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <log1> <log2> ...")
        sys.exit(1)

    errors, warnings = analyze_logs(sys.argv[1:])
    save_report(errors, warnings)





