# create /tmp/school
file { '/tmp/school':
  ensure  => 'file',           # Ensure it's a file
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
