# LionskKN-adventcalender-Evaluator

Small script to check if the numbers passed in the dockerfile won anything in the LionsKN Adventskalender 2021.

## Script

Crawls the website https://lionskn-adventskalender.de/gewinnnummern/ with BeautifulSoup4.

Parses the daily winners and the numbers passed in with the dockerfile.

Evaluates if you won something and prints it out.

## Docker
To build the docker:
``docker build -t [name]``

To run it afterwards:
``docker run [name]``

To check the Logs of the docker

Run ``docker ps`` to get the container id
Then ``docker logs [id]`` to see the results of the cronjob

### Environmental Variables

- NUMBERS: a string of numbers you want to check with the tool separated by a ","
