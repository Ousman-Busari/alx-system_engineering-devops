# creates a file in /tmp, with \"I love Puppet\" as the content
# and \"www-data\" as the owner and group
file {'/tmp/school':
  ensure  => 'file',
  group   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  }
