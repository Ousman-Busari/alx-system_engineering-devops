# install flask version 2.1.0 from pip3
package {'flask':
  ensure   => 'installed',
  provider => 'pip3',
  }
