# Script fix nginx
exec { 'Fix-nginx':
  path     => '/usr/bin',
  provider => shell,
  command  => 'sudo sed -i s/15/4096/  /etc/default/nginx  ; sudo service nginx restart'
}