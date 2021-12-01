FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV NUMBERS "4693,4677,8607"

CMD [ "python", "./main.py" ]
