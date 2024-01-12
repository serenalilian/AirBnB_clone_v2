#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static
# Check if Nginx is installed, and install it if not
if [ ! -x "$(command -v nginx)" ]; then
    echo "Nginx is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create required directories if they don't already exist
directories=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")
for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        echo "Creating directory: $dir"
        sudo mkdir -p "$dir"
        sudo chown -R ubuntu:ubuntu "$dir"
    fi
done

# Create a fake HTML file
html_file="/data/web_static/releases/test/index.html"
if [ ! -f "$html_file" ]; then
    echo "Creating fake HTML file: $html_file"
    echo "<html>
        <head>
            <title>Test Page</title>
        </head>
        <body>
            <h1>This is a test page.</h1>
        </body>
    </html>" | sudo tee "$html_file" > /dev/null
    sudo chown -R ubuntu:ubuntu "$html_file"
fi

# Create or recreate the symbolic link
current_link="/data/web_static/current"
if [ -L "$current_link" ]; then
    echo "Symbolic link already exists. Deleting and recreating..."
    sudo rm "$current_link"
fi
sudo ln -s /data/web_static/releases/test/ "$current_link"
sudo chown -h root:root "$current_link"

# Update Nginx configuration to serve the content of /data/web_static/current/
nginx_config="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static" "$nginx_config"; then
    echo "Updating Nginx configuration..."
    echo "
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
    " | sudo tee -a "$nginx_config" > /dev/null
fi

# Restart Nginx to apply changes
sudo service nginx restart

exit 0
