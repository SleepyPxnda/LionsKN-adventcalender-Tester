# Lionskn-Evaluator

Small script to check if the numbers passed in the dockerfile won anything in the LionsKN Adventskalender 2021.

Might add some cronjob to the dockerfile and change it to and ubuntu docker.

## Script

Crawls the website https://lionskn-adventskalender.de/gewinnnummern/ with BeautifulSoup4.

Parses the daily winners and the numbers passed in with the dockerfile.

Evaluates if you won something and prints it out.

## Docker
To build the docker:
``docker build -t [name]``

To run it afterwards:
``docker run [name]``

Since there is nothing special about this docker-container its simple as that

### Environmental Variables

- NUMBERS: a string of numbers you want to check with the tool separated by a ","
