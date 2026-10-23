import csv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

LOG_PATH = PROJECT_DIR / "sample_logs.csv"

try:
    with LOG_PATH.open("r", newline="", encoding="utf-8") as log_file:
        csv_reader = csv.DictReader(log_file)
        csv_events = list(csv_reader)

except FileNotFoundError:
    print(f"ERROR: Could not find the log file: {LOG_PATH}")
    raise SystemExit(1)

print("Number of events loaded:", len(csv_events))

if csv_events:
    print("First event loaded:", csv_events[0])
else:
    print("No events found in the csv file.")

failed_attempts = {}

# counters for login event statistics
successful_logins = 0
failed_logins = 0
unknown_logins = 0

for event in csv_events:
    print("checking event:", event)

    if event["status"] == "failed":
        failed_logins += 1
        ip_address = event["source_ip"]

        if ip_address not in failed_attempts:
            failed_attempts[ip_address] = 1
        else:
            failed_attempts[ip_address] += 1

        print("Alert: Failed login attempt detected!")
        print("Details: Username:", event["username"])
        print("Source IP:", event["source_ip"])
        print("Destination:", event["destination"])

    elif event["status"] == "successful":
        successful_logins += 1
        print("Info: Login attempt successful.")
    else:
        unknown_logins += 1
        print("Warning: Unrecognized login attempt.")

print("\n===== LOGIN EVENT SUMMARY =====")
print(f"successful login events: {successful_logins}")
print(f"failed login events: {failed_logins}")
print(f"unknown login events: {unknown_logins}")

print("Summary of failed login attempts:", failed_attempts)

#set threshold for suspicious activity
threshold = 3

print("\n===== Suspicious Activity Report =====")

# check for IP addresses in the failed login summary
for ip, count in failed_attempts.items():
    if count >= threshold:
        print(f"Alert: {ip} has {count} failed login attempts. Potential brute force attack detected!")
    else:
        print(f"Info: {ip} has {count} failed login attempt(s). No immediate threat.")

report_path = PROJECT_DIR / "Sentinel_report.txt"

with report_path.open("w", encoding="utf-8") as report:

    report.write("===== SENTINEL SECURITY REPORT =====\n\n")

#write login event statistics
    report.write(f"successful login events: {successful_logins}\n")
    report.write(f"failed login events: {failed_logins}\n")
    report.write(f"unknown login events: {unknown_logins}\n")
#write failed login attempts by IP address
    report.write("\n===== FAILED LOGIN ATTEMPTS BY IP ADDRESS =====\n")
    for ip, count in failed_attempts.items():
        report.write(f"{ip}: {count} failed attempt(s)\n")
#write suspicious activity findings based on threshold
    report.write("\n===== SUSPICIOUS ACTIVITY REPORT =====\n")
    for ip, count in failed_attempts.items():
        if count >= threshold:
            report.write(
                f"ALERT: {ip} has {count} failed login attempts. "
                "Potential brute force attack detected!\n"
                )
        else:
            report.write(
                f"INFO: {ip} has {count} failed login attempt(s). "
                "No immediate threat.\n"
                )
print(f"\nSentinel security report saved to: {report_path}")
print("Analysis complete.")
