# Allauth - Django
This project demonstrates a basic implementation of authentication using Django Allauth. 
It includes functionality for user signup, login, logout, and third-party authentication using Google, Apple, Microsoft, and GitHub.

Setup Instructions

  ->Clone the Project-Create a directory, open a terminal in the directory path, and clone the  project:

      git clone https://github.com/abynxv/Authentication-DjangoAllauth.git
      
  ->Install Virtual Environment
  
      pip install virtualenv
      
  ->Create a virtual environment within the directory:

      python -m venv venv_name  # On Windows
      python3 -m venv venv_name  # On macOS/Linux

  ->Activate Virtual Environment

      venv_name\Scripts\activate       # On Windows
      source venv_name/bin/activate    # On macOS/Linux

  ->Install Requirements

      pip install django djangorestframework django-allauth

  ->Open the project in VS Code:

      code .

  ->Open a terminal in VS Code, navigate to the project directory, and run the server:
  
      cd myproject
      python manage.py runserver
      
API Endpoints

1. http://127.0.0.1:8000/
![Dashboard](https://github.com/abynxv/Authentication-DjangoAllauth/assets/154351820/55f35c43-3c0c-4bad-9865-d4124aed5708)
2.http://127.0.0.1:8000/accounts/login/
![Signin](https://github.com/abynxv/Authentication-DjangoAllauth/assets/154351820/e98ee628-1d9f-4f0a-8ee6-d2cfa858d243)
3.http://127.0.0.1:8000/accounts/signup/
![Signup](https://github.com/abynxv/Authentication-DjangoAllauth/assets/154351820/1901afd8-cbe2-482d-a18a-466ec892f9bf)
4.http://127.0.0.1:8000/accounts/logout/
![Logout](https://github.com/abynxv/Authentication-DjangoAllauth/assets/154351820/f8b884ea-41eb-4fba-961b-ee90f535943e)








