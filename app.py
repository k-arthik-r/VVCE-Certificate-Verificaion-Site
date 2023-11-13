from flask import Flask, render_template, request
from configparser import ConfigParser
import pymongo

app = Flask(__name__)
config = ConfigParser()
config.read('config.ini')

print(config.sections())

client = pymongo.MongoClient(config['connection']['connection_string'])
db = client[config['database']['db_name']]
collection = db[config['database']['collection_name']]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    refid = request.form.get('refid')

    if refid:
        existing_refid = collection.find_one({'_id': refid})
        if existing_refid:
            db_message = existing_refid['message']
            message = db_message
            return render_template('index.html', message=message, success=True)
        else:
            message = "Invalid Reference ID"
            return render_template('index.html', message=message, success=False)
    else:
        return render_template('index.html', message="Something went wrong.", success=False)


if __name__ == '__main__':
    app.run()
