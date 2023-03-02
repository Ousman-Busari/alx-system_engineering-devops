# create a deafult index.html file to be serves by apache.

exec { 'fix-wordpress':
  command => 'touch /var/www/html/index.html',
  path    => '/usr/bin/:/bin/'
}
