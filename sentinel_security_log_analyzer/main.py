from pathlib import Path
security_events = [
    {
    "timestamp": "2026-10-12 15:49",
    "source_ip": "192.168.1.5",
    "destination": "web-server",
    "username": "admin",
    "status": "failed",
},
{
    "timestamp": "2026-10-12 15:50",
    "source_ip": "192.168.1.5",
    "destination": "web-server",
    "username": "admin",
    "status": "failed",
},
{
    "timestamp": "2026-10-12 15:51",
    "source_ip": "192.168.1.7",
    "destination": "web-server",
    "username": "user2",
    "status": "failed",
},
{
    "timestamp": "2026-10-12 15:52",
    "source_ip": "192.168.1.5",
    "destination": "web-server",
    "username": "user1",
    "status": "failed",
},
{
    "timestamp": "2026-10-12 15:52",
    "source_ip": "192.168.1.8",
    "destination": "web-server",
    "username": "user3",
    "status": "successful",
},
{
    "timestamp": "2026-10-12 15:53",
    "source_ip": "192.168.1.9",
    "destination": "web-server",
    "username": "user4",
    "status": "successful",
},
{
    "timestamp": "2026-10-12 15:54",
    "source_ip": "192.168.1.10",
    "destination": "web-server",
    "username": "user5",
    "status": "unknown",
},
{
    "timestamp": "2026-10-12 15:55",
    "source_ip": "192.168.1.11",
    "destination": "web-server",
    "username": "user1",
    "status": "unknown",
}
]

failed_attempts = {}

# counters for login event statistics
successful_logins = 0
failed_logins = 0
unknown_logins = 0

for event in security_events:
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


report_path = Path("__file__").with_name("Sentinel_report.txt")

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
