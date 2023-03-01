# create a deafult index.html file to be serves by apache.

exec { 'create_index_html':
  command => 'touch /var/www/html/index.html',
  path    => '/usr/bin/:/bin/'
}
