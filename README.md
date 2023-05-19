# Wealthtracker

## Distinctiveness and Complexity
The project employs Django's built-in authentication system to ensure secure user registration and login. By
implementing robust authentication measures, such as password hashing and protection against common vulnerabilities,
the project ensures the confidentiality and integrity of user data.

The project allows users to manage their money wisely within a single platform. Users can view their account balance 
and track transactions.

The project leverages Django's database models and ORM (Object-Relational Mapping) to efficiently store and retrieve 
account-related data. 

An essential aspect of financial management, expense tracking, is seamlessly integrated into the project. Users can 
track their spending habits.

Managing sensitive financial data securely is a complex task. The project implements robust security measures, such
as data encryption, access control, and validation, is crucial to safeguard user information and prevent unauthorized
access.

JavaScript plays a pivotal role in creating an interactive user interface. I utilize JavaScript to enhance the user 
experience. Implementing dynamic features, such as real-time updates, and data synchronization, adds complexity to 
the project.

Integrating Django with JavaScript requires establishing efficient communication between the front-end and the 
back-end components. This involves developing robust APIs (Application Programming Interfaces) and handling data 
serialization and deserialization. The complexity lies in synchronizing data between the client-side and server-side 
components and ensuring smooth interactions.

## views.py
### index(request)
This function servers as the entry point of the application. It checks if the user is authenticated or if the user
exists in the session. If either of these conditions are met, it renders the "index.html" template. Otherwise it
redirects the user to the login page.

### transactions(request)
This function is an API endpoint that handles the HTTP post request related to creating a new transaction.It expects 
the request body to contains JSON data with this fields "amount", "transaction_type", and "memo". It creates a new 
transaction object with the provided data, associated it with the authenticated user, and saves it to the database. 
Depending on the transaction type ("deposit" or "point of sale"), it updates the user balance accordingly. Finally, 
it returns a JSON response with a success message or a list of transactions if the request is get.

### users(request)
This function works as an API endpoint and returns a JSON response with a serialized data of the authenticated user.

### thismonth_transactions(request)
This function is an API endpoint that retrieves the transactions for the current month for the authenticated user. it
serializes them, and returns a JSON response.

### login(request)
This function handles the login process. If the request method is post, it attempts to authenticate the user with the 
provided username and password. If successful, it logs in the user, sets the "user_id" in the session if the 
"remember me" checkbox is checked, and redirects to the index page. If the authentication fails, it renders the login 
page with an error message.

### register(request)
this function handles the registration process. If the request method is post, it create a new user with provided 
username and password, saves it to the database, logs in the user, and redirects to the index page. If the username 
is already taken, it renders the registration page with an error message.

### logout(request)
this function logs out the user, removes the removes "user_id" from the session, and redirects to the login page.

## index.js
After the HTML document has been fully loaded. The following functions are called in sequence displayBalance(), 
displayMonthlyDepositAndSpending(). DisplayBalance() is an asynchronous function that sends a get request to the 
"/users" API endpoint to fetch the current user's data, parses the response data as a JSON, and displays the user's 
balance in the UI. displayMonthlyDepositAndSpending() is an asynchronous function that sends a get request to the 
"/transactions/thismonth" API endpoint to fetch user's transactions for the current month, parses the response data 
as JSON, calculates the monthly deposit and spending amounts by iterating over the transactions and summing up the 
amounts based on the transaction type, and updates the monthly spending and deposit amount in the UI. When the create 
new transaction form is submitted, the listener triggers an asynchronous function that sends a post request to the 
"/transactions" API endpoint with the transaction data provided by the user, and calls an asynchronous function that 
sends a get request to the "/transactions" API endpoint to fetch the user's transactions, parses the response data as 
JSON, creates a table row for each transaction, and updates the transaction count in the UI.

## Quickstart
```
# Create new migrations
python3 manage.py makemigration

# Migrate
python3 manage.py migrate

# Start development server 
python3 manage.py runserver

# In browser, navigate to generated URL (typically local host http://127.0.0.1:8000/)
```