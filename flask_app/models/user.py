from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        result = connectToMySQL('users_schema').query_db(query, data)
        if len(result) < 1:
            return False
        row = result[0]
        user = cls(row)
        return user
    
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users(first_name, last_name) VALUES(%(first_name)s, %(last_name)s)'
        user_id = connectToMySQL('users_schema').query_db(query, data)
        return user_id
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s WHERE id = %(id)s'
        user_id = connectToMySQL('users_schema').query_db(query, data)

    
    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s'
        user_id = connectToMySQL('users_schema').query_db(query, data)

