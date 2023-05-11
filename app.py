from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    xml_data = request.data
    root = etree.fromstring(xml_data)
    return f"Received: {etree.tostring(root, pretty_print=True).decode()}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
