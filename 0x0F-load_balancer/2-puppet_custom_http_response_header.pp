#!/usr/bin/env bash
# we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'header':
	command  => 'sudo apt-get update -y;
	sudo apt-get install nginx -y;
	sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
	sudo service nginx start',
	provider => shell,
}
