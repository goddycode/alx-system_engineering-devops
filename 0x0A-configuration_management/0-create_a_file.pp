# creating a file in /temp using puppet
file { 'school':
	path => '/tmp/school',
	own => 'www-data',
	mode => '0744'
	group => 'www-data'
	content => 'I love Puppet'
} 
~ 
~
