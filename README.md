# WeatherSearch
> A web-app based on python, flask, Bootstrap-CSS and HTML5.
The app uses the OpenWeatherMap API to collect weather rellated infos of a specific location defined by the users input, and displays it for the user. Finally, making it easier to know more about the weather!

##### DISCONTINUED - This repository will not receive new updates.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
* [License](#license)


## General Information
The purpose of the project was, initialy, to develop my personal skills on python and web-development, based on that I did some idea-search on [App-Ideas github](https://github.com/florinpop17/app-ideas) and find the "Weather App" one.

The project tries making easier the search for weather rellated infos.



## Technologies Used
- Python - version 3.9.6
- Flask (python web-development framework) - version 2.0.2
- OpenWeatherMap API
- Bootstrap CSS - version 5.1.3
- HTML

## Features
- Temperature search on a specific city.
- Wind-speed search on a specific city.
- Humidity search on a specific city.


## Screenshots / Demonstration
![Home page](https://github.com/P-py/WeatherSearch/blob/main/imgs/weathersearch0.PNG?raw=true)
![Result page](https://github.com/P-py/WeatherSearch/blob/main/imgs/weathersearch1.PNG?raw=true)


## Setup
The pip requirements are listed on requirements.txt

First of all you will need python and git, I'll not teach you how to install these here, so if you need one of those or don't have they installed yet just go to:
- [Python.org](https://www.python.org/downloads/)
- [Git page](https://git-scm.com/)
- [How to install git on windows](https://phoenixnap.com/kb/how-to-install-git-windows)
- [How to install git on Mac](https://phoenixnap.com/kb/install-git-on-mac)
- [How to install git on Linux](https://www.tutorialspoint.com/how-to-install-git-on-linux)

*If you are on Linux you probably don't need to install python*

*To check if you have python or git on windows go on cmd/shell and type `python --version`*

Now, let's install the requirements.

On Linux:
`pip3 install flask`

On Windows:
`pip install flask`

Clone the repository:
`git clone https://github.com/P-py/WeatherSearch.git`

## Usage
Go on your shell/console and access the folder directory on the code, you need to this after the steps listed on [Setup](#setup), after that just type in:
`flask run`

Finally, your project should start running on local host `127.0.0.1:5000`

## Project Status
Project is: _in progress_ - Just implemented and deployed the version 1.0 and working on the new features for 1.0.1


## Room for Improvement
Improvements to be done:
- Visual improvements on the logo
- UI improvements on the result page and home page.

To do:
- Weather description and representation through SVGs


## Acknowledgements
- This project was inspired by [Florinpop17's App-Ideas](https://github.com/florinpop17/app-ideas)
- This project was based on [Legion Script's tutorial](https://www.youtube.com/channel/UCF7k5gX55WvJ-SFXGsPsLTg)

## Contact
Created by [@p-py](https://P-py.github.io) - feel free to contact me!



## License
This project is open source and available under the [MIT License](https://github.com/P-py/WeatherSearch/blob/main/LICENSE).
