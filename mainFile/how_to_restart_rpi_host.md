Steps to follow to start rpi wifi:
* Start terminal in rpi
* Run the following commands:
  * `sudo systemctl stop dnsmasq`
  * `sudo systemctl stop hostapd`
  * `sudo service dhcpcd restart`
  * `sudo systemctl start hostapd`
  * `sudo systemctl start dnsmasq`
* Ready to go
