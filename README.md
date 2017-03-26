Tsuki つき
-----
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/mokachokokarbon/Tsuki/issues)

A simple Twitter client application written in Python (backend) and PyQt (GUI) utilizing the TwitterAPI library.

Essential Tools
---------------
For the developers who want to get their hands dirty on this project, the essential tools are listed below and how to get them:

* [Python 3.6.0](https://www.python.org/downloads/release/python-360/)

* [PyQt 5.8.1](https://www.riverbankcomputing.com/software/pyqt/download5)

   `pip install PyQt5`

* [TwitterAPI 2.4.5](https://github.com/geduldig/TwitterAPI)

   `pip install TwitterAPI`

Make sure to download the 32-bit version of Python.

Configuration Files
-----------
To avoid any errors, here are the (2) important files  before running the application for development.

1. Create a `config.ini` and add the following lines of codes:

   ```ini
   [TOKENS]
   consumer_key: consumer key
   consumer_secret: consumer secret
   access_key: access key
   access_secret: access secret
   ```
   Provide your own keys by signing in to your Twitter account and creating an application on [Twitter Account Management](https://apps.twitter.com/).

2. Create a `constants.py` and add the following lines of codes:

   ```python
   import configparser
   import os

   config = configparser.ConfigParser()
   config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

   CONSUMER_KEY = config['TOKENS']['consumer_key']
   CONSUMER_SECRET = config['TOKENS']['consumer_secret']
   ACCESS_KEY = config['TOKENS']['access_key']
   ACCESS_SECRET = config['TOKENS']['access_secret']
   ```
   Then save these files to `src/resources` directory and you are good to go.

   **CAVEAT**: Never let this files be part of your commit --I warned you :)
