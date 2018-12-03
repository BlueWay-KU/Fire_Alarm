hc06 ADDR : 00:18:E5:04:8F:13

/* setting */
/etc/bluetooth/rfcomm.conf

//rfcomm.conf
rfcomm0 {
  # Automatically bind the device at startup
  bind yes;
  # Bluetooth address of the device
  device 00:18:E5:04:8F:13;
  # RFCOMM channel for the connection
  channel 1;
  # Description of the connection
  comment "This is Device 1's serial port.";
}

sudo rfcomm bind hci0 00:18:E5:04:8F:13 1

sudo hciconfig hci0 up

sudo rfcomm connect hci0 00:18:E5:04:8F:13

