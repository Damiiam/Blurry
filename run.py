from app import app
from os import environ as env

if __name__ == '__main__':
    port = int(env.get('PORT', 5000))
    app.run(port=port)