# Django CRM Application

This is a basic CRM (Customer Relationship Management) application built with Django. It provides user registration, login, and logout functionality, along with the ability to manage customer records.

## Features

- User Registration: Users can create new accounts by providing a username, email address, and password.
- User Login: Registered users can securely log in to the application using their credentials.
- User Logout: Users can log out of the application to securely end their session.

### Record Management

- Record Table: Users can view a table displaying all customer records, including relevant information such as name, contact details.
- Individual Record Page: Clicking on a id of record in the table opens a page displaying detailed information about the customer.
- Update Record: Users can update the information of a customer record, including their name, contact details.
- Delete Record: Users can delete a customer record if it is no longer needed.

## Getting Started

To run the Django CRM application on your local machine, follow these steps:

1. Clone the repository to your local machine (Run the following command):
    - `git clone https://github.com/Kunal-R-Prajapati/Django-crm.git`

2. Navigate to the project directory

3. Create a virtual environment by running the following command:
     - `python -m venv venv`

4. Activate the virtual environment by tho following command :
    - For Windows:
     `venv\Scripts\activate`
    
    - For macOS/Linux:
      `source venv/bin/activate`


6. Install the project dependencies by running the following:
   - `python -m pip install Django`
   - `pip install mysql`
   - `pip install mysql-connector`
   - `pip install mysql-connector-python`
   

7. Set up the database:
    1. Install MySql on your local machine
    2. Setup the root user and password
    3. In mydb.py enter the password
    4. Name Your database
    5. Run the following commands in your venv shell
        - `python manage.py makemigrations`
        - `python manage.py migrate`

8. Start the development server by:
   - `python manage.py runserver`

9. Open your web browser and visit `http://localhost:8000` to access the application.

## Contributing

If you'd like to contribute to the development of the Django CRM application, please follow these guidelines:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch for your feature or bug fix.
3. Make the necessary changes.
4. Commit your changes and push the branch to your forked repository.
5. Open a pull request on the main repository, providing a clear description of the changes made.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We would like to thank the Django community and all contributors for their valuable contributions to the framework.

If you have any questions or need assistance with the Django CRM application, please feel free to contact us at prajapatikunal392@gmail.com
