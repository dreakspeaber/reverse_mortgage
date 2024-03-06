# reverse_mortgage


To start the project : 
       python -m venv env #create environment 
       python manage.py runserver

Project components : -

   API app : serving API / http endpoints with template and JSON responses

   mortgage package : Serving key mortgage classes (That does the mortgage calculations, and have mortgage key configurations) with respective tests for them.  
   

   Design choices : - 
         
         Key global mortgage configuration are initiated as Class variables. These class variables have been initialized statically inside the class, which can also
         be plugged from environment variables or better from an initial db connection, and have any configuration update in the database trigger the class variable update.



     