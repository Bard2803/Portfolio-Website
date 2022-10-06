# Portfolio-Website

## My portfolio website. Created with the following technologies:

1. HTML
2. CSS
3. Javascript
4. Python
5. Flask
6. AWS Elastic Beanstalk

#### Video Demo: https://youtu.be/WSfQ1r6RDB0
#### Deployed on: http://portfoliowebsite-env.eba-km3caqj7.eu-central-1.elasticbeanstalk.com/


This is my portfolio website. It serves as a presentation of myself along with the IT projects that i have done. It is deployed on AWS using the AWS Elastic Beanstalk orchestration service. 

The "application.py" is the main file. The name had to be changed from standard app.py to application.py in order for AWS services to recognize it on the server. It has a standard build of flask framework. It takes care of all templates rendering and redirection on the website. It is the "
heart" of this website. At the very end of code application.run() runs the application so it can be automatically launched on server.

The "requirements.txt" is the text file which contains listed versions of all dependencies needed to launch the application. It is neccessery in deployment through AWS Elastic Beanstalk, because that way all dependencies can be installed automatically on server. In general it is a good practice to always include such a file for later reproducibility. 

There are to .ignore files one is for Git and the other is for Elastic Beanstalk.

The main templates files are layout.html and index.html. the layout.html is a standard file for flask application and index.html is standard file for whole web development. Layout contains the main structure of the webpage, index.html contains the home page details. The best thing here is that thanks to flask they can share content. The layout.html playing a role of main template lets the index.html be extension of it.
cipher.html is a separate template for a Cipher project and as more projects will be added more dedicated templates will be created.

The static folder contains the css and js files. Css files play a role of properly placing the objects on the webpage as well as their visual side. The main.js make navigation bar more interactive. For example it appears at the top of the page when the user scrolls the down. The isotope.js has been copied under commercial use and controls the interactivity of the projects selection area. 

In this folder are also images that are displayed on the webpage. They are just linked in the html file to be displayed in proper sections.

Cipher folder containst the project that has been uploaded to the webpage. User can type some message and it gets ciphered. There is also a window to type the shifting number which tells the algorithm by how many places in the alphabet the letters have to be shifted.

The .ebextensions contains just the standard information for AWS Elastic Beanstalk that the application deployed is written in Python. It helps avoiding bug in deployment.