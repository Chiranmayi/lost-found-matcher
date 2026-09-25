##  Lost & Found Matcher

A beginner-friendly Python command-line application that helps users register lost and found items and identify possible matches based on category, location, and description keywords.



##  Project Overview

People may lose personal belongings such as bags, water bottles, ID cards, books, and other items.

The Lost & Found Matcher provides a simple system to:

* Register lost items
* Register found items
* Validate required fields
* Validate dates
* Search reports by category and location
* Find possible matches
* Calculate a matching score
* Update report status
* Display open reports
* Store data in JSON format

A possible match is only a suggestion and does not prove ownership.



##  Objectives

The main objective of this project is to create a simple Python application that connects lost and found item reports.

The system compares:

* Item category
* Location
* Description keywords

Based on these criteria, the system calculates a matching score and displays possible matches for review.



## Features

### Core Features

1. Register Lost Item

   * Report ID
   * Category
   * Description
   * Location
   * Date
   * Status

2. Register Found Item

   * Report ID
   * Category
   * Description
   * Location
   * Date
   * Status

3. Input Validation

   * Required fields cannot be empty
   * Date must follow `YYYY-MM-DD` format

4. Search

   * Search by category
   * Search by location
   * Search using both category and location

5. Possible Match Detection

   * Compares lost and found reports
   * Checks category
   * Checks location
   * Compares description keywords

6. Matching Score

   * Calculates a score out of 100
   * Displays the matching details

7. Status Management

   * Open
   * Matched
   * Returned

8. Open Reports

   * Displays all currently open lost reports
   * Displays all currently open found reports

9. JSON Storage

   * Saves reports in `data.json`
   * Loads previously saved reports when the application starts



##  Matching Algorithm

The application calculates a matching score out of 100 points.

| Matching Criteria         |  Points |
| ------------------------- | ------: |
| Category Match            |      40 |
| Location Match            |      30 |
| Description Keyword Match |      30 |
| Total                     |      100|

### How It Works

### 1. Category Match — 40 Points

If the lost item's category and found item's category are the same, the system adds 40 points.

Example:


Lost Category: Bags
Found Category: Bags


Result:
+40 points

 2. Location Match — 30 Points

If the locations are the same, the system adds 30 points.

Example:


Lost Location: Library Entrance
Found Location: Library Entrance


Result:
+30 points


### 3. Keyword Match — Up to 30 Points

The descriptions are converted to lowercase and split into keywords.

The system uses Python sets to find common keywords between the lost and found descriptions.

Example:

Lost:
blue college backpack with small front pocket

Found:
blue college backpack with front pocket


Common keywords include:
blue
college
backpack
with
front
pocket


The number of common keywords is used to calculate the keyword score.



##  Possible Match

A report is displayed as a possible match when its calculated score is 50 or above.

The application displays:


POSSIBLE MATCH FOUND
Lost Report
Found Report
Category Match
Location Match
Keyword Match
Match Score
Status: Review Required


The match is only a suggestion and should be reviewed before changing the report status.



##  Report Status

Each report starts with:
Open
The user can update the status to:

Open
Matched
Returned

##  Data Storage

The application uses a JSON file named:

data.json

The JSON file stores both:


lost_items
found_items


When the application starts, previously saved reports are loaded.

When the application finishes, the updated reports are saved back to the JSON file.



##  Testing

The project includes a separate test file:


test_main.py

Python's built-in unittest framework is used.

The tests cover:

* Required field validation
* Date validation
* Keyword extraction
* Matching score calculation
* Keyword match classification

### Run Tests

Open the terminal in the project folder and run:

python test_main.py


Expected result:


----------------------------------------------------------------------
Ran 5 tests

OK

##  Technologies Used

* Python
* JSON
* datetime
* unittest

Python sets are also used for comparing description keywords.


## Project Structure


lost-found-matcher/
│
├── main.py
├── test_main.py
├── data.json
└── README.md


##  How to Run

### Step 1: Open the project folder

bash
cd lost-found-matcher


### Step 2: Run the application
python main.py

### Step 3: Run the tests

python test_main.py

##  Sample Data

The project uses sample reports such as:

### Lost Report

ID: L301
Category: Bags
Description: Blue college backpack with small front pocket
Location: Library Entrance
Date: 2026-09-18
Status: Open


### Found Report

ID: F407
Category: Bags
Description: Blue college backpack with front pocket
Location: Library Entrance
Date: 2026-09-18
Status: Open

The system compares these reports and calculates a possible matching score.


##  Project Purpose
* Lists
* Dictionaries
* Sets
* Functions
* Loops
* Conditional statements
* Input validation
* File handling
* JSON
* Exception handling
* Unit testing
* Basic string processing
