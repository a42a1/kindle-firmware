#!/bin/sh
BIN=$(basename "$0" .sh)
ARCH="armel"
if [ -f /lib/ld-linux-armhf.so.3 ]; then
    ARCH="armhf"
fi
/mnt/us/extensions/gnomegames/bin/${ARCH}/${BIN} "$@"