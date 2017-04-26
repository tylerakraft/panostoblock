import os
import untangle
import requests
import time

# Environment Specific Variables

Key = '&key=ADD YOUR API KEY HERE'

BaseUrl = 'ADD YOUR BASE URL HERE'

ThreatCall = 'ADD YOUR API CALL TO QUERY THE THREAT LOGS'

JobCall = '?type=log&action=get&job-id='

PathToBlackList = 'PATH TO THE BLACKLIST FILE'

FileName = 'NAME THE BLACKLIST FILE'

# Queue the Query and Parse the Job ID

JobId = requests.get(BaseUrl + ThreatCall + Key, verify=False)

JobCallResponse = untangle.parse(JobId.text)

GetJobId = JobCallResponse.response.result.job.cdata

# Give the job a bit to run 

time.sleep(30)

# Pull the logs

XmlLogs = requests.get(BaseUrl + JobCall + GetJobId + Key, verify=False)

# Convert the text to XML

ParsedXmlLogs = untangle.parse(XmlLogs.text)

# Open the blacklist and clear the file

os.chdir(PathToBlackList)

NewBlackList = open(FileName, 'r+')

NewBlackList.truncate()


# Dedupe and write the ip addresses to the blacklist

Ips = set()

for entry in ParsedXmlLogs.response.result.log.logs.entry:


    if entry.src.cdata not in Ips:
        NewBlackList.write(entry.src.cdata + '\n')
        Ips.add(entry.src.cdata)


# Close the blacklist


NewBlackList.close()
