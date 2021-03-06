## Virus Total's parent company is Google Inc.
- It contains several antivirus (ex: kaspersky, avast, McAfee, etc.)
- You can use it for scanning any type of files
- You can integrate it to your website or application for scanning purpose, ex: file scanner while uploading files on the website

## Create Virus Total API Key
- Go to below link and create your api key, which you need to place in config file (ex: config.py)
- Also you find API documentation from the below link itself.
<a href="https://developers.virustotal.com/v3.0/reference">Create API</a>


## Run the project

1. Create virtual/conda environment

2. Install all the libraries
    >> pip install requirements.txt

3. Set the configurations to the config file, which includes,
    - set email and password of the created email(gmail preferred) [in config.py file]
    
    Go to below link and enable "Allow less secure apps: OFF"
    <a href="https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NUDQ2XKMSmGhmQWrcfr9u2CSSasWsPdDxux8qHOjE_5X4BUXPR_0NHGD_oVsciC-jQN9b7SDo0FKMUhkiQpC23-Du9Xg">
    Click here</a>
    For any more query: <a href="https://realpython.com/python-send-email/">Go here</a>

4. Set the URL in config file

5. Run the project
    >> python main.py


## A general summary of the project files or code layout

- config
    This file contains the configuration for the project

- data
    Used as dummy(unused) storage if required

- Scanned_Result
    It stores the generated scanned files report in json format

- src
    It contains email.py file which helps in sending the email
    Note: Chnage the email message from this 'email.py' if required

- templates
    It contains 2 html files
    1. home.html : It is the main landing page of the app where user need to upload the text file
    2. result.html : It shows the generated report's data in tabular format

- main.py
    It is the main file of the project which will run the application and loads other required resources

- requirements.txt
    This file contains all the list of the used libraries for this project



## Technology stack used

- This file can be run on any OS just by following the above steps.



## Required dependencies not normally installed on the system
- requirement.txt
Just install the libraries/packages from the above file(mentionedon the top in procedure)


## Issues encountered, and how you addressed them
- This project is very simple all the issues can be handled easily by checking top results from the google
- But here you might encounter error due to libraries/packages make sure you have installed exect mentioned libraries.
- Other issue you might encounter for sending the email, refer below link its very simple to perform
    <a href="https://realpython.com/python-send-email/">https://realpython.com/python-send-email/</a>