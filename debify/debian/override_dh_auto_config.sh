#!/bin/bash

source debian/vars.sh

set -x

/opt/cpanel/ea-php74/root/usr/bin/phpize

./configure \
    --with-php-config=/opt/cpanel/ea-php74/root/usr/bin/php-config

make
