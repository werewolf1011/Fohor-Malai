# Fohor-Malai
A waste complaining web app 

Installation
1. Install Python 3
Make sure you have Python 3 installed on your system. You can download it from the official Python website.

2. Install Django and Dependencies
Use pip to install Django and the required dependencies:

pip install django
pip install django-tinymce
pip install django-autoslug
pip install six
pip install social-auth-app-django


Running the Web App
1. Clone the Repository
Clone this repository to your local machine using Git:

git clone https://github.com/werewolf1011/Fohor_Malai.git

2. Navigate to the Project Directory
cd Fohor_Malai

  >>> Go to "info.py" in "Fohor Malai" app folder and use your own email and app password here:

  EMAIL_HOST_USER = "your_email@gmail.com"
  EMAIL_HOST_PASSWORD = "<your_email_host_password>"


  >>> Go to settings.py and use your own keys here:
  SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = (
      "<your_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY>"
  )
  SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "<your_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET>"


3. Run Migrations
Apply the database migrations:

python manage.py migrate

4. Start the Development Server
Start the Django development server:

python manage.py runserver


5. Access the Web App
Open your web browser and go to http://localhost:8000 to access the web app.
