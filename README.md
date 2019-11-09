# Utilify

![Image description](https://www.portseattle.org/sites/default/files/2018-03/la-me-political-issues-public-utilities.png)

Utilify is an application that sends weekly updates of the utility bill. This is done through utilizing Python, and Azure DevOps.

What you'll need to run this application:

Create a credentials.py file and add the necessary variables

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

Run Dockerfile
Make sure you have [Docker] (https://docs.docker.com/install/) installed
```
docker build -t utilify /file/path/to/utilifyHomeDirectory
```

# MORE UPDATES TO COME
