# kill process named killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
