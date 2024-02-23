# Use pkill to kill killmenow proccess

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
