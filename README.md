# 28/08/24 - Oligarchy Data (#19)
This program is a CLI tool which extracts data (rank, company name, company code, country, market cap) from the top 500 global public companies and can list the data with some queries. These include:
- top 500 companies data
- view specific company data
- top companies by country
- number of companies by country

To run the app, run the app.py script to initialise the data and type in 'Flask help' to see which commands to put in for the CLI.

The data was extracted from [companiesmarketcap.com](https://companiesmarketcap.com) using requests and beautiful soup. I used SQLite for the database and Flask for the backend.

This is my first time doing web scraping (outside of a couple of labs in uni). It wasn't as difficult as expected but it was a little frustrating trying to find which data resided where in the DOM. The nice thing about webscraping as a miniproject is that it is an easy source of data. I think I will probably implement webscraping another time now that I know how to do it on my own.
