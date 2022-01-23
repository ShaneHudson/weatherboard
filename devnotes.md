

https://gist.githubusercontent.com/kizniche/5cea47b44cc1bfd15da837a1b634b9a5/raw/e8f2c2a1409a6f1730aa9ae718c0a212f6d86f87/flask_nginx_gunicorn.md

sudo service weatherboard restart



Crontab:
0 * * * * curl localhost/?api_key=[API KEY] -o /home/pi/weatherboard/screenshot.jpg | python /home/pi/weatherboard/displayImage.py /home/pi/weatherboard/screenshot.jpg
