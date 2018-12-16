#!/usr/bin/bash

# set LED red
echo 1 > /sys/class/leds/red/brightness
echo 0 > /sys/class/leds/green/brightness

sleep 5

echo "Script Starting" >> /media/changeLogo/changeLogo.log

if [[ -e /media/changeLogo/showLogo.new ]]; then
	echo "showLogo.new found!" >> /media/changeLogo/changeLogo.log
	# Mount system as RW 
	echo "Mounting as RW" >> /media/changeLogo/changeLogo.log
	results=$(mount -o remount,rw / 2<&1); if [[ $? != '0' ]]; then echo "FAILED: $results" >> /media/changeLogo/changeLogo.log; exit; fi
	# Backup showLogo
	if [[ ! -e /usr/sony/bin/showLogo.bak ]]; then
		echo "Backing up changeLogo" >> /media/changeLogo/changeLogo.log
		results=$(cp /usr/sony/bin/showLogo /usr/sony/bin/showLogo.bak 2<&1); if [[ $? != '0' ]]; then echo "FAILED: $results" >> /media/changeLogo/changeLogo.log; exit; fi
	fi
	# Backup sic
	if [[ ! -e /usr/bin/sic.bak ]]; then
		echo "Backing up sic" >> /media/changeLogo/changeLogo.log
		results=$(cp /usr/bin/sic /usr/bin/sic.bak 2<&1); if [[ $? != '0' ]]; then echo "FAILED: $results" >> /media/changeLogo/changeLogo.log; exit; fi
	fi
	# Copy new files from USB to system
	echo "Copying showLogo" >> /media/changeLogo/changeLogo.log
	results=$(cp /media/changeLogo/showLogo.new /usr/sony/bin/showLogo 2<&1); if [[ $? != '0' ]]; then echo "FAILED: $results" >> /media/changeLogo/changeLogo.log; exit; fi
	echo "Patching sic" >> /media/changeLogo/changeLogo.log
	results=$(echo '#!/bin/bash\necho "bite me Sony"' > /usr/bin/sic 2<&1); if [[ $? != '0' ]]; then echo "FAILED: $results" >> /media/changeLogo/changeLogo.log; exit; fi
else
	echo "showLogo.new NOT found!" >> /media/changeLogo/changeLogo.log
	# Copy original showLogo executable to USB
	if [[ ! -e /media/changeLogo/showLogo.orig ]]; then
		if [[ ! -e /usr/sony/bin/showLogo.bak ]]; then
			echo "Copying original showLogo to USB" >> /media/changeLogo/changeLogo.log
			results=$(cp /usr/sony/bin/showLogo /media/changeLogo/showLogo.orig 2<&1); if [[ $? != '0' ]]; then echo "FAILED: $results" >> /media/changeLogo/changeLogo.log; exit; fi
		else
			echo "Copying original showLogo to USB" >> /media/changeLogo/changeLogo.log
			results=$(cp /usr/sony/bin/showLogo.bak /media/changeLogo/showLogo.orig 2<&1); if [[ $? != '0' ]]; then echo "FAILED: $results" >> /media/changeLogo/changeLogo.log; exit; fi
		fi
	fi
fi

# set LED green
echo 0 > /sys/class/leds/red/brightness
echo 1 > /sys/class/leds/green/brightness

while True; do
	sleep 1
done