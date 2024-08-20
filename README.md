# Tentips

## Description

**Tentips** is a simple website that provides ten valuable tips from various kinds of books. Whether you're interested in self-improvement, business, or just looking for some inspiration, Tentips has you covered. This README file provides an overview of the website's structure.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Project Details](#project-details)
- [Source Code](#source-code)

## Features

- Create an account to personalize your Tentips experience and save your favorite tips.
- Display ten valuable tips from different books.
- Tips categorized by genre for easy navigation.
- Favorite section to keep all your favorite books at one place.
- Pick color theme from five different colors according to your liking.
- Simple and responsive design for a seamless user experience.

## Project Structure

Here's an overview of the project's directory structure:

```
/tentips
├── app.py # Flask application
├── myfunc.py # Custom functions used in app.py
├── static/ # Static assets (CSS, JavaScript, images)
├── templates/ # HTML templates
├── tentips.db # SQL db 
├── requirements.txt # Python dependencies
└── README.md # Project README
```

## Project Details

The Tentips website is built using the Flask web framework, a Python-based tool that allows for the creation of dynamic web applications. At its core, the project consists of several key files and directories that work together to deliver its functionality.

- The central Flask application file, app.py, handles the routing and logic of the website. It defines the routes for rendering pages, handling user account management, and fetching book tips from the database. "myfunc.py" contains the helper functions for app.py.

- Template contains all HTML pages. The html pages contain a similar structure designed in "layout.html". Index page contains two view - Homepage view and search view which are switched accodingly using javascript.

- The static directory stores all static assets required for the website, such as CSS stylesheets, JavaScript files, and image resources. These assets are responsible for styling and interactivity.

- requirement.txt  lists all the Python dependencies required to run the Flask application and readme.md provides essential documentation for the project.

## Website Screenshots

Here are some screenshots of the Tentips website to give you a visual overview of its user interface and features:

![register](https://github.com/user-attachments/assets/3a91c2ff-5556-4590-9a21-231bb9c05834)
![homepage](https://github.com/user-attachments/assets/074b7131-8ba0-4b7f-9caa-3d5f779a0d1b)
![tips page](https://github.com/user-attachments/assets/19ebae3b-fe44-4d4c-b8ba-78cb8228569c)
![favorites](https://github.com/user-attachments/assets/1ceb9c43-dfd2-4231-b6ff-eb5a523571f2)

## Source Code

 Clone or download the Tentips repository from [GitHub](https://github.com/Xerx81/tentips).

   ```bash
   git clone https://github.com/Xerx81/tentips.git
