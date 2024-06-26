0x1A. Application server
.................................................

Background Context
................................................

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

Resources
..............................................
Read or watch:
..............................................
i) Application server vs web server - https://www.nginx.com/resources/glossary/application-server-vs-web-server/
ii) How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally) - https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04
iii) Running Gunicorn - https://docs.gunicorn.org/en/latest/run.html
iv) Be careful with the way Flask manages slash in route - strict_slashes - https://werkzeug.palletsprojects.com/en/3.0.x/en/0.14.x/routing/
v) Upstart documentation - https://doc.ubuntu-fr.org/upstart
