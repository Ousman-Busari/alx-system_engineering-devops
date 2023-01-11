# chnages the ssh-config

include stdlib
file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   => '    PasswordAuthentication no',
  match  => '#   PasswordAuthentication yes',
  }

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   => '    IdentityFile ~/.ssh/schhol',
  match  => '#   IdentityFile ~/.ssh/id_ed25519',
  }