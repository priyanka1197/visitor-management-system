

## Technology Stack
- Django - Backend
- HTML, CSS, Bootstrap - Frontend
- Sqlite3 - Database
- Jinja - Templating engine
- way2sms Message API (You can use any API of your choice!)


## Local Machine development setup
- Clone the repository on your machine 
    ```
    git clone https://github.com/priyanka1197/visitor-management-system.git
    ```
    
- Install all dependencies by executing the following command:
    ```
    pip install -r requirements.txt
    ```
    
- You need to make some changes to the settings.py file inside visitor_management folder, go to bottom of the file
    ```
    UPDATE : EMAIL_HOST_USER = "your email id" 
    UPDATE : EMAIL_HOST_PASSWORD = "your email id password"
    ```
    ( Make sure you <a href='https://myaccount.google.com/lesssecureapps'>enable less secure apps</a> in your google account, so that it sends email ! )
   
- Now you need to edit some lines in views.py file inside accounts folder
  - INSIDE email function:
    ```
    UPDATE : sender = 'your email id'
    ```
  - GO to <a href='https://www.way2sms.com/'>way2sms</a>, create your account and genetrate your test apikey and secret key. Now go INSIDE sendsms function:
    ```
    UPDATE : 'apikey':'your api key',
    UPDATE : 'secret':'your secret key',
    UPDATE : 'senderid' : 'your way2sms account email id'
    ```
    
- Now go inside the main folder which was cloned (manage.py file will be present there), now open a terminal in that directory and run follwing commands:
    ```
    python manage.py createsuperuser
    # follow further instruction there
    
    - After super user is created 
    python manage.py makemigrations
    python manage.py migrate
    
    python manage.py runserver
    ```
- Now server will start at - http://127.0.0.1:8000/

### Credits :
- HTML mail templates are made on <a href="https://beefree.io/">beefree.io</
