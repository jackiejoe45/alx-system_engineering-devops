# installs package flask -v 2.1.0

exec { 'flask':
  command => '/usr/bin/apt-get -y pip3 flask -v 2.1.0',
}
