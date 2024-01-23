Command for Running gunicorn server
gunicorn epsilonpos_backend.config.wsgi:application

nginx configuration
1. Install nginx
    sudo apt update
    sudo apt install nginx
    
2. setup server block

# /etc/nginx/sites-available/epsilonpos

server {
    listen 80;
    server_name localhost;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /var/www/epsilonposv2/epsilonpos_backend/config/static/;
        expires 30d;
    }
    location /media/ {
        root /var/www/epsilonposv2/epsilonpos_backend/config/media/;
        expires 30d;
    }

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
        proxy_connect_timeout 600s;
        proxy_send_timeout 600s;
        proxy_read_timeout 600s;
        send_timeout 600s;
    }

    location ~ /\.ht {
        deny all;
    }
}
