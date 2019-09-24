#1/bin/bash

config-pin P9_19 i2c
config-pin P9_20 i2c

while [ "1" = "1" ]; do
    TEMP=`i2cget -y 2 0x48`
    TEMP2=`i2cget -y 2 0x49`
    AVGT=$((($TEMP+$TEMP2)/2))
    TEMPF=$(((($AVGT*9)/5)+32))
    echo -ne "${TEMPF}"
    sleep 1.0
    echo -ne "\\r"
    
done