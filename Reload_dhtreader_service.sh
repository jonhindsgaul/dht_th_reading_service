systemctl stop dhtreader.service
systemctl daemon-reload
systemctl start dhtreader.service
systemctl enable dhtreader.service
systemctl status dhtreader.service

