
# Project Title

Lab-Scheduler: Server Infrastructure Client to Update Google Sheets to Display Relevant Information


## Authors

- [@Felipe-Ma](https://github.com/Felipe-Ma)


## Installation

Install lab-scheduler with git clone 

```bash
  git clone https://github.com/Felipe-Ma/lab-scheduler.git
```

Create a python3 virtual environment 

```bash
  python3 -m venv lab-scheduler-venv
```

Install Pip modules
#### Windows
```bash
  lab-scheduler-venv\Scripts\activate
  pip install --upgrade pip
  pip install pygsheets pyyaml py-cpuinfo
```

#### Linux
```bash
source lab-scheduler-venv/bin/activate
pip install --upgrade pip
pip install pygsheets pyyaml py-cpuinfo
```


    
## Configuration

Configure config.yaml

```bash
# Example Configuration
serverName: Solidigm Example
folderPath: "/home/solidigm/lab-scheduler/"
credentialsName: credentials.json
workBook: Example workbook
workSheet: Example worksheet
region: Rancho Cordova
drivebays: 8
connectiontype: U.2
```

#### Linux
Configure lab-scheduler.sh
```bash
# Example shell script
source /home/nsg/lab-scheduler-ven/bin/activate
/home/nsg/lab-scheduler-venv/bin/python3 /home/nsg/lab-scheduler/main.py
deactivate
```
## Automation

How to Automate Script Upon Startup

#### Linux
Setup crontab to shell Script

sudo crontab -e
```bash
  @reboot sudo /home/nsg/lab-scheduler/lab-scheduler.sh
```