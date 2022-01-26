FROM python:3.7-buster
RUN apt-get install libcairo2-dev

# Codebase setup
RUN mkdir /srv/weatherboard/
WORKDIR /srv/weatherboard/
RUN pip3 install requests pillow flask gunicorn pytz pycairo matplotlib --no-cache-dir

# Add code
ENV PYTHONPATH /srv/weatherboard/server/
ADD . /srv/weatherboard/

# Add fonts
RUN cp /srv/weatherboard/fonts/* /usr/share/fonts && fc-cache

# Runtime
ENV PORT 80
CMD ["/bin/sh", "-c", "exec gunicorn --reload --bind :$PORT --workers 1 --threads 8 server:app"]
