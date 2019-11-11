# Utilify

[![Build Status](https://dev.azure.com/tuckermmccoy/GitProjects/_apis/build/status/tmccoy14.Utilify?branchName=master)](https://dev.azure.com/tuckermmccoy/GitProjects/_build/latest?definitionId=1&branchName=master)

![Image description](https://www.portseattle.org/sites/default/files/2018-03/la-me-political-issues-public-utilities.png)

Utilify is an application that sends weekly updates of the utility bill. This is done through utilizing Python, and Azure DevOps.

What you'll need to run this application:

Create a credentials.py file and add the necessary variables or bake them into the pipeline

Clone the repository to preferred path
```
git clone https://github.com/tmccoy14/Utilify.git
```
Create and activate virtual environment
* macOS or Linux
```
python3 -m venv env
source env/bin/activate
```
* Windows
```
py -m venv env
.\env\Scripts\activate
```
[For more on virtual environments] (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Install the following packages
```
pip install -r requirements.txt
```

Setup free AzureDevops Account
```
https://azure.microsoft.com/en-us/services/devops/
Create a free account
Create an organization
Create a pipeline -> Choose Github -> Choose Repo -> Choose Existing Azure Pipeline Yaml File -> Choose Branch and Path to azure-pipelines.yaml -> Review and Run pipeline
```