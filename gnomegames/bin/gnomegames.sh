#!/bin/sh

GAME="${1}"
ARCH="armel"
# Check if the Kindle is ARMHF or ARMEL
if [ -f /lib/ld-linux-armhf.so.3 ]; then
    ARCH="armhf"
fi

# Check if the game is installed
if [ ! -f /mnt/us/extensions/gnomegames/bin/${ARCH}/${GAME} ]; then
    # kh_msg "Game not installed" W v "Game not installed"
    exit 1
fi

export GSETTINGS_SCHEMA_DIR=/mnt/us/extensions/gnomegames/share/glib-2.0/schemas

/mnt/us/extensions/gnomegames/bin/${ARCH}/${GAME}