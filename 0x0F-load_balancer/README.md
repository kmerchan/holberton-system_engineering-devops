#0x0F-load_balancer
This directory contains initial work with configuring multiple web servers and using a load balancer to balance between the two.

0. Configure the second web server to be identical to the server created in 0x0C-web_server.  Add custom Nginx response header to track which server is answering HTTP requests and to track the way a load balancer works.
1. Writing a script to install and configure HAproxy on the load balancer server.
