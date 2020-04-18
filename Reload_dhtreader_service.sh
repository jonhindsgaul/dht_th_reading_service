sudo systemctl stop dhtreader.servuce
sudo systemctl daemon-reload
sudo systemctl start dhtreader.service
sudo systemctl enable dhtreader.service
sudo systemctl status dhtreader.service