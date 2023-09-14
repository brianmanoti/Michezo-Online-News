"""
#!/usr/bin/python3

script to verify fask installation
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
