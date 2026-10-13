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
    "source_ip": "192.168.1.6",
    "destination": "web-server",
    "username": "user1",
    "status": "failed",
},
{
    "timestamp": "2026-10-12 15:51",
    "source_ip": "192.168.1.7",
    "destination": "web-server",
    "username": "user2",
    "status": "successful",
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
    "status": "successful",
}
]

for event in security_events:
    print("checking event:", event)
    
    if event["status"] == "failed":
        print("Alert: Failed login attempt detected!")
    else:
        print("Info: Login attempt successful.")