# Coke Machine 🥤

A simple Python program that simulates a vending machine that sells a Coke for 50 cents.

## About the Project

The program accepts coins one at a time and keeps track of the amount inserted. The machine only accepts coins worth 25, 10, or 5 cents.

If the inserted amount is less than 50 cents, the program shows the remaining amount due. Once the user has inserted enough money, the program displays the change owed.

Invalid coin values are ignored.

## How It Works

The program starts with an amount due of 50 cents.

For each coin entered:

* `25` cents is accepted
* `10` cents is accepted
* `5` cents is accepted
* Other values are ignored

For example:

```text
Insert Coin: 25
Amount Due: 25
Insert Coin: 10
Amount Due: 15
Insert Coin: 25
Change Owed: 10
```

## What I Practiced

* `while` loops
* `input()`
* `int()` conversion
* `if` statements
* `while` conditions
* Tracking values with variables
* Input validation
* Handling repeated user input

## Technologies

* Python

## Course

This project was completed as part of **CS50's Introduction to Programming with Python** by Harvard University.
