# **<u>nigelhaney.me</u>**

This project features the majority of the code used for my site at [nigelhaney.me](https://nigelhaney.me). In this readme, you will find descriptions of the different directories present in this project.

## FishGame

This directory features the source code for the game *Stay Off the Line!*  found at https://nigelhaney.me/games/fish. It has been modified slightly to support submitting to the global leaderboard.

## backend

This directory features the entire codebase for the backend service powering my website. It is a RESTful API using the Python Flask framework. To run the API, you must install a virtual environment using the installvenv script. After that you may run the production server with portfolioapi/run_prod.py and the development server with portfolioapi/run_dev.py. To run all tests run tests/MainTestRunner.py. 

## blogsubmitter

This directory is a small utility tool that I use to submit blog posts using the service. It converts a markdown file, title, and excerpt into the correct JSON request format for my server.

## frontend

This directory features the frontend of my website. It is written in React JS and styled using react-bootstrap. 

## sql_statements

This directory features the schemas of my database tables that I use for my website. 
