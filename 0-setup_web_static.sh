#!/usr/bin/env bash
#script that deploys airbnb for serving 

# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt update
    sudo apt install nginx -y
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
sudo touch /data/web_static/releases/test/index.html
echo "<html><head><title>Test Page</title></head><body><h1>This is a test page</h1></body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Set ownership recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/hbnb_static/ d' /etc/nginx/sites-available/default
sudo sed -i 's/^\s*server_name\s.*/&\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}\n/' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0

