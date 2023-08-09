---

portfolio_project: Missing Person OSINT database
course: Nucamp SQL with Python
project_developer: Keith Jackson
date: 07-18-2023

---

# Missing Person Database

---
## Description
---
This is a raw SQL database for collecting data to make a data trail to help find missing persons. It provides a REST API to help create, find, index, and delete missing person info and the associated atttributes. 

---
## Schema Reference Table
---

                         List of relations
 Schema |                 Name                  | Type  |  Owner   
--------+---------------------------------------+-------+----------
 public | connections                           | table | postgres
 public | current_locations                     | table | postgres
 public | missing_person_info                   | table | postgres
 public | missing_person_info_connections       | table | postgres
 public | missing_person_info_current_locations | table | postgres
 public | missing_person_info_social_media      | table | postgres
 public | social_media                          | table | postgres
(7 rows)

---
### How did the project's design evolve over time?
The project did not evolve over time it just became a little more clear as to what I was trying to accomplish. I know it will evolve once I can go back and learn how to implement rawSQL into a three tier application which was not explained in this course. 

### Did you choose to use an ORM or raw SQL? Why?
raw SQL was used as I feel that I want to understand how to use the fundamentals before understanding a more complex variant.

### What future improvements are in store, if any?
Get my client object, requests, and functions understood(they are not at all right now). Once I can manipulate fake data then try and put it on a profile webpage and maintain/add to make it a database that can be used by all.