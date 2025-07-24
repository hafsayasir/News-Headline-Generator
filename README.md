# News Headline Generator (Pakistan Edition)

A fun Python CLI app that generates fictional news headlines in Politics, Sports, and Entertainment. Built for learning and raising awareness about how easily news style text can be fabricated. Includes custom topic support, file saving, and terminal styling.

---

## Project Overview

In today's digital world, fake news and clickbait headlines are spreading faster than ever. Understanding how headlines are constructed and how easily they can be manipulated is essential for digital literacy.

This project is a Python based command line application that generates fictional news headlines by combining predefined subjects, actions, and objects. The content is themed around Pakistan’s politics, sports, and entertainment in a way that is fun, harmless, and respectful. Users can also create their own custom categories.

This project serves both as a learning tool for beginner programmers and as a simple demonstration of how easily headlines can be fabricated, encouraging users to think critically about the media they consume.

---

## Features

- Generate fictional news headlines in three categories:
  - Politics
  - Sports
  - Entertainment
- Support for custom topics created by the user
- Ability to save generated headlines to a local file
- Option to view all saved headlines during the session
- Colored terminal interface using the `colorama` library
- Input validation and clean command-line flow

---

## Why I Built This

This project was built as a way to improve my Python skills while exploring the logic behind headline generation. With so much misinformation circulating online, I wanted to create a small educational tool that highlights how structured—and sometimes misleading—headlines are formed. The app is not intended to spread any real news or misinformation; it's purely for educational and personal development purposes.

---

## Technologies Used

- Python 3
- `colorama` for terminal text styling
- Standard Python libraries (`random`, `input`, `file I/O`)

---


## How to Use

To run this project on your local machine:

1. Open your terminal or command prompt.

2. Clone the repository:

git clone https://github.com/hafsayasir/news-headline-generator.git

cd news-headline-generator


3. Make sure you have Python 3 installed. You can check it using:
python --version


4. Install the required package (`colorama`) using pip:
pip install colorama


5. Run the script:python headline_generator.py



6. Follow the instructions in the terminal to:
- Choose a news category (Politics, Sports, Entertainment, or Custom)
- Generate fun headlines
- Save them to a file if you want
- View all saved headlines before exiting

