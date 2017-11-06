# Pyramid Learning Journal Test Plan

## Home Page Tests
- Returning dictionary
- Returning list of all entires in database
- Any newly created posts are rendered on home page


## Detail Page Tests
- HTTPNotFound for non-existent posts
- Returning dictionary from database
- Returning specific entry data for one post
- POST request on this page brings you to edit view


## Edit Post Tests
- Updates existing post in database with edited information
- Returns existing title and text body if a GET request to edit page


## New Post Tests
- New entry is rendered to home page, and is persisted in database


## Delete Tests
- Post is deleted from database and is no longer rendered


### Coverage

