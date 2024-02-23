# Install pip3 and then flask 2.1.0 with pip3

package { 'python3-pip':
  ensure   => '3.8.10',
  provider => 'apt',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
