# Continuous Intelligence Project 4 - 

## Project Description
This project is focused on the practice of following a typical workflow of a real interactive development project from start to finish. It will utilize Python, as well as the practice of creating and cloning a GitHub repo, creating and activating virtual environments, and installing packages.

## Project Setup
### Create a virtual Environment
``` shell
py -m venv .venv
py -m .\.venv\Scripts\activate
```

### Install Dependencies and Upgrade Pip
``` shell
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py -m pip install --upgrade -r requirements.txt
py -m pip install --upgrade pip setuptools
```

### Freeze Requirements
``` shell
py -m pip freeze > requirements.txt
```

### Add to .gitignore
``` shell
.venv/
.vscode/
```

## Dependencies Imported
``` shell
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins
from shiny import reactive, render, req
import seaborn as sns
import pandas as pd
```

## Build Client-Side App
```shell
shiny static-assets remove
shinylive export penguins docs
py -m http.server --directory docs --bind localhost 8008

## Git Add and Commit
``` shell
git add .
git commit -m "update message goes here"
git push origin master
```

## Credentials
This was a required project to be completed for the MS in Data Analytics degree at Northwest Missouri State University. Assisted instructions were given by Denise Case. Additionally AI was utilized to complete this project.
Deitel, P. (2021). *INTRO TO PYTHON FOR COMPUTER SCIENCE AND DATA SCIENCE : learning to program with ai, big data, and the cloud*, global edition. Pearson Education Limited.