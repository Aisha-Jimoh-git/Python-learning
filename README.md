# Sentinel — Security Log Analyzer

**Sentinel** is a Python-based security log analysis tool designed to simulate some of the basic functionality of a Security Information and Event Management (SIEM) system.

The project was developed as a hands-on cybersecurity learning project to strengthen my understanding of Computer fundamentals and problem solving including; **Python programming, security log analysis, event detection, network security concepts, and SOC analyst workflows**.

Sentinel reads security events from a CSV log file, analyses the events, identifies potentially suspicious activity, and generates a security report.

> **Project Status:** Actively Developing
---
## Project Objectives

The main objectives of Sentinel are to:
* Analyse security events from external log files
* Identify suspicious login activity
* Detect repeated failed authentication attempts
* Analyse SSH-related activity
* Identify potentially suspicious source IP addresses
* Categorise security events
* Produce a structured security report
* Practise Python programming through a cybersecurity-focused project
* Develop skills relevant to **SOC Analyst / Security Operations** work
---
## Current Features
### CSV Log Analysis

Sentinel now reads security events from a CSV file rather than relying on manually entered Python dictionaries like it did initially.
Example event:

```csv
timestamp,source_ip,destination,username,status
2026-10-18 09:01:00,192.168.1.5,web-server,admin,failed
```

This makes it easier to work with larger datasets and simulate real-world security log ingestion.
---
### Authentication Monitoring
Sentinel analyses authentication events and identifies:
* Successful login attempts
* Failed login attempts
* Unknown or unrecognised authentication statuses
* Repeated authentication failures
* Suspicious source IP addresses

Example detection:

```text
ALERT: Multiple failed login attempts detected from 192.168.1.5
```
---
### Network & Security Event Analysis

The project is being expanded to analyse a wider range of security-related information, including:

* Source IP addresses
* Destination systems
* Ports
* Port numbers
* Network services
* SSH activity
* `sshd` events
* Authentication activity

This allows Sentinel to move beyond simple login monitoring towards broader security-event analysis.
---
### Asset / System Inventory

Sentinel is being developed to recognise different types of systems and infrastructure within the dataset.

Potential inventory categories include:
* Web servers
* Database servers
* SSH servers
* Workstations
* Network devices
* Other monitored systems

This provides additional context when analysing security events.
---
### Security Reporting

After analysing the events, Sentinel produces a security report containing information such as:

* Number of events analysed
* Successful authentication attempts
* Failed authentication attempts
* Unknown events
* Suspicious IP addresses
* Detected security alerts
* Relevant event information

The report is generated automatically and saved within the project directory.
---
## Detection Logic

Sentinel currently uses rule-based detection logic.
For example, repeated failed authentication attempts from the same IP address can be identified as potentially suspicious activity.
```text
Security Logs
     │
     ▼
CSV File
     │
     ▼
Sentinel
     │
     ├── Parse Events
     │
     ├── Analyse Authentication
     │
     ├── Analyse IP Addresses
     │
     ├── Analyse SSH Activity
     │
     ├── Check Detection Rules
     │
     ▼
Security Alerts
     │
     ▼
Security Report
```
The detection approach is intentionally simple at this stage, with the project being gradually expanded as I develop my Python and cybersecurity skills.
---
## Technologies & Tools

* **Python 3**
* **CSV**
* **VS Code**
* **Git & GitHub**
* **Windows**
* Cybersecurity and SOC concepts

### Python Concepts Used
* Variables
* Lists
* Dictionaries
* Loops
* Conditional statements
* Functions
* File handling
* CSV processing
* Exception handling
* Path management
* Basic data analysis
---
## Project Structure

```text
sentinel_security_log_analyzer/
│
├── main.py
├── sample_log.csv
├── Sentinel_report.txt
└── README.md
```

### `main.py`
The main Python program responsible for loading, analysing and processing security events.

### `sample_log_120.csv`
Contains the security events used as Sentinel's input data.
### `Sentinel_report.txt`

Automatically generated report containing the results of the analysis.
---
## How to Run Sentinel

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/sentinel-security-log-analyzer.git
```
### 2. Open the Project
```bash
cd sentinel-security-log-analyzer
```
### 3. Run Sentinel
```bash
python main.py
```
Sentinel will load the CSV security log, analyse the events and generate the security report.
---
## Example Workflow
```text
Input:
100+ security events
        │
        ▼
CSV Log File
        │
        ▼
Sentinel Analysis
        │
        ├── Authentication Events
        ├── Failed Logins
        ├── Source IPs
        ├── SSH Events
        ├── Ports
        └── Security Services
        │
        ▼
Detection Rules
        │
        ▼
Alerts & Statistics
        │
        ▼
Sentinel Security Report
```
---
## Planned Features
Sentinel is an ongoing project. Future improvements may include:
* [ ] Expand the security event dataset
* [ ] Add more authentication detection rules
* [ ] Improve SSH/`sshd` detection
* [ ] Add port-based detection
* [ ] Detect possible port scanning behaviour
* [ ] Add severity levels to alerts
* [ ] Add timestamps to generated alerts
* [ ] Improve IP reputation analysis
* [ ] Add configurable detection thresholds
* [ ] Add JSON log support
* [ ] Add Windows event log support
* [ ] Add Linux authentication log support
* [ ] Develop a graphical dashboard
* [ ] Add visual security statistics
* [ ] Improve reporting and alert prioritisation
* [ ] Explore anomaly-detection techniques
---
## Learning Purpose

Sentinel is primarily a **learning and portfolio project**.
I am using the project to combine my developing knowledge of:

* Python programming
* Network security
* Linux
* Authentication
* SSH
* Log analysis
* SIEM concepts
* Security monitoring
* Incident detection
* SOC operations
The project is being developed incrementally rather than attempting to build a complete SIEM from the beginning.
---
## About the Developer

I am currently studying for an **MSc in Cybersecurity** and developing practical skills in security operations, log analysis, network security and Python.
My cybersecurity learning journey includes practical work with technologies and platforms such as:
* Splunk
* Wireshark
* Linux
* Kali Linux
* Cisco technologies
* TryHackMe
* LetsDefend
* Python

Sentinel represents my ongoing effort to turn cybersecurity concepts into practical, working security tools.
---
## Disclaimer
Sentinel is an educational cybersecurity project intended for **learning, experimentation and portfolio development**.
The detection rules are intentionally simplified and should not be considered a replacement for a production SIEM or professional security monitoring platform.
---
## Project Status

**Active Development**

New detection capabilities, log types and security analysis features are being added as the project develops.
