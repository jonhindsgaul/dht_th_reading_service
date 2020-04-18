# Remember to run: "chmod +x ./Reload_dhtreader_service.sh"
# Must be run as 'sudo'
systemctl stop dhtreader.service
systemctl daemon-reload
systemctl start dhtreader.service
systemctl enable dhtreader.service
systemctl status dhtreader.service