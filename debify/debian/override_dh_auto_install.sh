#!/bin/bash

source debian/vars.sh

set -x

make install INSTALL_ROOT=$DEB_INSTALL_ROOT DESTDIR=$DEB_INSTALL_ROOT
install -m 755 -d $DEB_INSTALL_ROOT/$ext_prefix/$conf_dir
install -m 644 $SOURCE1 $DEB_INSTALL_ROOT/$ext_prefix/$conf_dir/
