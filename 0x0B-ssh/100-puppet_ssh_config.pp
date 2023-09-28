# Define a Puppet class for SSH client configuration
  2 class ssh_client_config {
  3   file { '/home/ubuntu/.ssh/config':
  4     ensure => 'file',
  5     content => "
  6       # SSH client configuration
  7       Host your_server
  8         HostName 54.237.115.170  # Replace with your server's IP or domain
  9         User your_username ubuntu       # Replace with your SSH username
 10         IdentityFile ~/.ssh/school    # Path to your private key
 11         PasswordAuthentication no     # Disable password authentication
 12     ",
 13     owner  => 'ubuntu',       # Replace with your username
 14     group  => 'ubuntu',       # Replace with your username
 15     mode   => '0600',                # Set permissions to 0600 (readable/writable by owner)
 16   }
 17 }
 18 
 19 # Apply the SSH client configuration class
 20 include ssh_client_config
