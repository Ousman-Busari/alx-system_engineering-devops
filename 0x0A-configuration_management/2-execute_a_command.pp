# execute a pkill command on a process - killmenow
exec {'pkill killmenow':
  command => '/usr/bin/pkill -15 killmenow',
  }
