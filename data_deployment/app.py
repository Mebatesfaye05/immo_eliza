from modeling import process_house_data
from flask import Flask, request
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["Get"])
def check():
    return render_template('check.html')


@app.route('/process_house_data', methods=['Post'])
def receive_house_data():
    process_house_data = request.args
    processed_data = process_house_data(process_house_data)
    return processed_data


if __name__ == '__main__':
    app.run()


# this is giving me a method error
