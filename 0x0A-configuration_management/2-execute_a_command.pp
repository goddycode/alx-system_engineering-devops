# This script will call pkill
exec {'killmenow':
  command => '/usr/bin/pkill -f killmenow'
}
