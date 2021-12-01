FROM python:3-alpine

# ========== Configure Project ==========
RUN mkdir /code
WORKDIR /code

ADD . /code

ENV NUMBERS "4677,4693"

RUN pip install -r requirements.txt
# ========== CRON ==========
# Configure cron
COPY crontab /etc/cron/crontab

# Init cron
RUN crontab /etc/cron/crontab

CMD ["crond", "-f"]
