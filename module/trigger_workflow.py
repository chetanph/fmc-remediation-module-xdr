#!/usr/bin/env python
"""
Cisco Firepower Management Center (FMC) Remediation module for Cisco eXtended Detection and Response
(XDR) Automation workflow.
"""

import sys
import xml.etree.ElementTree as ET
import requests

# Read Webhook URL from instance.conf
tree = ET.parse("instance.conf")
webhook_url = tree.find("./config/string[@name='webhook_url']").text

# JSON Request Body for XDR Webhook
event = {
    "remediation_name": sys.argv[1],
    "src_ip_addr": sys.argv[2]
}

# Send data to XDR Automation Webhook
response = requests.post(webhook_url, json=event, timeout=30)

# Check if webhook accepted (HTTP 202) the request
if response.status_code == 202:
    print(f"XDR Automation Webhook accepted data: {event}")
else:
    print(f"Unexpected response from XDR Automation Webhook: {response.text}")
    sys.exit(129)
