import sys

def analyze_log(file_path):
    errors = 0
    warnings = 0

    try:
        # Open the log file
        with open(file_path, "r", errors="ignore") as f:
            for line in f:
                line = line.lower()
                if "error" in line:
                    errors += 1
                elif "warning" in line:
                    warnings += 1

        # Print summary
        print("Log Analysis Report")
        print("-------------------")
        print(f"Errors   : {errors}")
        print(f"Warnings : {warnings}")

    except FileNotFoundError:
        print("Log file not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <logfile>")
        sys.exit(1)

    analyze_log(sys.argv[1])
