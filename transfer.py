import sqlite3
import json
import uuid

data = sqlite3.connect('instance/development.db')
data_cursor = data.cursor()

with open('user.json', 'r') as file:
    users = json.load(file)

for user in users:
    user_id = str(uuid.uuid4())
    data_cursor.execute(
        "INSERT INTO users(id, email, first_name, last_name, is_admin, password_hash, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
        (user_id, user['email'], user['first_name'], user['last_name'], user['is_admin'], user['password_hash'], user['created_at'], user['updated_at'])
    )

data.commit()
data_cursor.close()
data.close()
