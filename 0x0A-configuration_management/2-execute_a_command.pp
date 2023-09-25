# execute a kill command
exec {'pkill killmenow':
  path => '/usr/bin',
  }
