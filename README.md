# CANADIAN CHEESE DIRECTORY

## VIDEO DEMO:  https://vimeo.com/660772040

## AUTHOR:
**Name: **      William Javier Bernal
**Email:**      bern0295@algonquinlive.com
**City:**       Ottawa, Ontario
**Country:**    Canada

## DESCRIPTION:

The Canadian Cheese Directory is a web-based application created by using JavaScript, Flask, Python, and SQL,
intended to present all the information about cheese made in Canada, and collected by the Government of Canada.
he Government of Canada has a comprehensive database dedicated solely to Canadian cheeses made from cow, goat, sheep,
or buffalo milk. The Canadian Cheese Directory is compiled and updated by the Canadian Dairy Information Centre (CDIC)
in collaboration with the Ministère de l'Agriculture, des Pêcheries et de l'Alimentation du Québec (MAPAQ).
The Publisher is the Agriculture and Agri-Food Canada organization.

This directory is available in the following [Link](https://open.canada.ca/data/en/dataset/3c16cd48-3ac3-453f-8260-6f745181c83b)

Currently The Directory is served only to be downloaded as a file formatted as CSV, XML, or JSON. Even those
formats can be manipulated in different ways. They are not friendly for end users.

### Why this project was created - Justification

According to the CSV File produced by the Canadian Dairy Information Centre (CDIC) in collaboration with
the Ministère de l'Agriculture, des Pêcheries et de l'Alimentation du Québec (MAPAQ), there are around 182 cheese manufacturers.
This figure includes big industries and small farms as well.  Not all of them have a website to exhibit their products.

A website to show the Canadian Cheese directory with a friendly user Interface does not exist yet. There is a website
created by the [Canadian Dairy Information Centre (CDIC)](https://cheese-fromage.agr.gc.ca/) which is not easy to search in.
The idea to create the Canadian Cheese Directory is to allow the end user to fiend as much information as possible with
the minimum amount of clicks per search.

This project for the CS50 course is the first step on the desired result. In a future release, not covered in the current project scope,
the end user is going to have options to filter, sort, add, or update products. Also, to complete the manufacturer information.


## PURPOSE OF THE CANADIAN CHEESE DIRECTORY WEBSITE:

The current project creates a new website that does not already exist, to allow to upload the CSV file into
a database within the website. The website has a page that allow to load the file, which is then read and parsed
into a database table.

From that table, it is possible to show the information inside a website, in a friendly way to depict all the
information in a better way.

The main page shows a welcome to the Canadian Cheese Directory and shows randomly 5 rows of cheeses.
That page shows the nav bar, with a menu of three options.

1. Home
2. Search a Cheese
3. Load

Initially that page shows some pictures in a carousel.

## OPERATION MANUAL

### Home Page

The main title of the page is shared across all the pages.

In the Home page you can see some facts about the cheese industry in Canada. There are some pictures
sliding in a carousel for decoration purposes only. You will se button `Go to the Directory` that takes you
to the web page `Search Cheese`.


In the bottom of the page you will see a grid with  5 rows and 5 Columns showing the Province, Cheese Name, Manufacturer,
Milk Type, and Fat Content percent. Those five rows are randomly read from the database. So every time you load
the home page, you will get 5 different rows.

At the footer of the homepage, you will see:

- The source link for the [CSV file](https://open.canada.ca/data/en/dataset/3c16cd48-3ac3-453f-8260-6f745181c83b)
- The [License](https://open.canada.ca/en/open-government-licence-canada) to use that information
- a Link to the LinkedIn web page of the project creator - [William Bernal ](https://www.linkedin.com/in/wbernal-it/)

### Search Cheese

This webpage shows a grid with the total of rows in the database (currently there are 1374 rows) in chunks of 20 rows.
In the background you will see two different images creating a parallax-effect. The images are the same images used
in the carousel from the home page.

The header of the grid depicts the total rows in the database, the initial row number in the page and final row number
showed in the current page.

Inside the grid, you can see 7 columns:

- Row#
- Province where the manufacturer is settled
- Cheese Name
- Manufacturer
- Milk Type (whether it comes from cow, goat, ewe, sheep, or buffalo milk)
- Fat Content percent
- a button `more` to see more information

The button `more` will open a modal-window to show all the detail for the selected cheese-row.
information available:

Cheese Name, Manufacturer Name, Manufacturer Province, Manufacturing Type (industrial, farmstead, artisan),
Manufacturer Website, Fat Content Percent, Moisture Percent, Particularities, Flavour, Characteristics,
Ripening time, Organic, Category Type (firm, fresh, soft, hard, semi-soft, cheese), Milk Type,
Milk Treatment Type (pasteurized, raw milk, thermised), Rind type, Last update date in the CSV file.

You can press the links:

- Previous Page
- Next Page

To move across the database.


### Load CSV

This webpage shows an option to select the CSV file from your local computer.
You have to previously downloaded the CSV file from the The source link for the [CSV file](https://open.canada.ca/data/en/dataset/3c16cd48-3ac3-453f-8260-6f745181c83b)
Once you select the file, you can press the button `Upload Data`.

This process will parse the CSV file and will insert all the available information into the database.


## PROJECT TECHNICAL INFORMATION

This project was created using the CS50 IDE:

- CS50 infrastructure
- Database SQLite
- Front-End Framework: Flask
- Back-End programming language: Python
- Bootstrap
- JavaScript (jQuery)
- CSS
- HTML

### Files

The application.py file is the controller of the web application. In manages the routes and end points.
The javaScript file `cheese_script.js` inside the folder static is called inside the webpage
`search a cheese`. It is responsible to show the modal window that contain the information detail
for the selected cheese row.

Following is the tree structure of the project:

#### Folder project:
- application.py
- helpers.py
- README.md
- **Folder Model**
  - cheesedir.db  This file is the database file
  - cheeseModel.py  This file manages the database model

- **Folder static**
  - cheese_script.js
  - styles.css
  - **Folder files**
    - canadianCheeseDirectory.csv
  - **Folder images**
    - CanadaFlag.pn
    - cheese-64.png
    - cheesesbg1.jpg
    - cheesesbg2.jpg
    - **Folder carousel**
      - cheese1.jpg
      - cheese2.jpg
      - cheese3.jpg
      - cheese4.jpg
  - **Folder templates**
    - index.html
    - layout.html
    - loadtable.html
    - search.html

## Image Credits
All the images depicted in the index.html page come from:

* [pixabay image 1](https://pixabay.com/images/id-3373604/)

* [pixabay image 2](https://pixabay.com/images/id-3652274/)

* [Photo by Polina Tankilevitch from Pexels](https://www.pexels.com/@polina-tankilevitch?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)

* [Photo by Irita Antonevica from Pexels](https://www.pexels.com/@irita?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)

* [Photo by Elle Hughes from Pexels](https://www.pexels.com/@elletakesphotos?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)

* [Photo by Cup of Couple from Pexels](https://www.pexels.com/@cup-of-couple?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)

* [Photo by Adonyi Gábor from Pexels](https://www.pexels.com/@adonyi-foto?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)
