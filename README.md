# RPi2-Web
Web control of RPi2 GPIOs. Tested on Raspbian Jessie.

sudo apt-get install lighttpd
place index.html file at /var/www/html
sudo service lighttpd start and browse to board url ensure lighttpd is active
sudo apt-get install python-flup
place web.py file at /var/www & be certain it's lighttpd executable (chmod 755)
ls -l /usr/bin/python produced lrwxrwxrwx 1 root root SOME DATE /usr/bin/python -> python2.7
sudo cp /usr/bin/python2.7 /usr/bin/pythonRoot
sudo chmod u+s /usr/bin/pythonRoot
ls -l /usr/bin/pythonRoot produced -rwsr-xr-x 1 root root SOME DATE TIME /usr/bin/pythonRoot
edit /etc/lighttpd/lighttpd.conf to include mod_fastcgi
sudo service lighttpd restart
