# Employee API Task

# How to use this branch

To get this running, simply run the  the following 

## Step 1: Install requirements.txt

`pip install -r requirements.txt`

## Step 2: Create databases

Create the databases and the initial migrations with the following command:
`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`

You should now be able to go to localhost:8000/api/ see available endpoints.

Use the POSTMAN API tool  and import the EmployeeAPI.postman_collection.json file and
test the endpoints.
