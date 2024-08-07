# executes a command

# kill process killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  path    => ['/usr/bin', '/usr/sbin'],
}

exec { 'pkill_flask':
  command => 'pkill -f flask',
  onlyif  => 'pgrep -f flask',
  path    => ['/usr/bin', '/usr/sbin'],
  require => Exec['install_flask'],
}
