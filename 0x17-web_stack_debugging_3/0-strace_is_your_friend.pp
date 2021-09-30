# Script Fix Wordpress
exec { 'Fix-Wordpress':
  path     => '/usr/bin',
  provider => shell,
  command  => 'sudo sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php'
}