# chnages the ssh-config

include stdlib
file_line { 'Disbale PasswordAuthentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '#   PasswordAuthentication yes'
  }

file_line { 'Declare IdentityFile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/schhol',
  }