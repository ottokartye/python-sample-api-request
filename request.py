import requests
from prettytable import PrettyTable

class UserService:
    request = None
    table = None

    # Populate the table and return it
    def get_table(self, fields, data):
        # Init table with the required fields
        table = PrettyTable()
        table.field_names = fields
        # Parse through the data
        for row in data:
            # Parse thorugh the fields
            currentRow = []
            for field in fields:
                currentRow.append(row[field])
            table.add_row(currentRow)
        return table

    # Get the data from the API
    def get_data(self, url): 
        # Get the list of todos
        return requests.get(url).json()

url_todos = 'https://jsonplaceholder.typicode.com/todos'
url_users = 'https://jsonplaceholder.typicode.com/users'
todos_field_names = ['userId', 'id', 'title', 'completed']
users_field_names = ['userId', 'id', 'title', 'body']
service = UserService()
data = service.get_data(url_todos)
table = service.get_table(todos_field_names, data)
print(table)
