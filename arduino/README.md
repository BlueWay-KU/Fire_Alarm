hc06 ADDR : 00:18:E5:04:8F:13

#TO DO LIST FOR QYUN

sudo hciconfig hci0 up
hcitool scan

sudo bluetoothctl
trust 00:18:E5:04:8F:13
pair 00:18:E5:04:8F:13

sudo rfcomm connect hci0 00:18:E5:04:8F:13
--> already in use라고 뜨면
sudo rfcomm release 0 한번 작성 후 다시 connect 시도할 것

연결되면 새 cmd 창 열어서 파이썬 코드 돌리기!


#TO DO LIST FOR BEGINNER

sudo apt-get install python
sudo apt-get install python-pip
sudo apt-get install bluez
sudo apt-get install bluetooth bluez-tools
sudo apt-get install bluetooth bluez-tools blueman
sudo apt-get install python-serial


sudo apt-get update
sudo apt-get upgrade

sudo hciconfig hci0 up
hcitool scan
sudo rfcomm bind hci0 00:18:E5:04:8F:13 1

sudo bluetoothctl

power on
agent on
default-agent
pairable on
discoverable on
trust 00:18:E5:04:8F:13
pair 00:18:E5:04:8F:13 --> pin code: 0000

sudo rfcomm connect hci0 00:18:E5:04:8F:13
--> already in use라고 뜨면
sudo rfcomm release 0 한번 작성 후 다시 connect 시도할 것
