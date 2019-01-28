import json
from os import listdir
from os.path import isfile, join
from flask import Flask, render_template, request, redirect


app = Flask(__name__)
app.static_url_path = '/static'


@app.route('/', methods=['GET'])
def HelloPage():
    page = "<html>\n<body>\n"
    page += "<h1> Hello World </h1>\n"
    basic = "<img src=\"{}\" alt='{}'>"
    mypath = 'static/images/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(onlyfiles)

    for f in onlyfiles:
        if f != '__init__.py':
            page += basic.format("/" + mypath + f, f)
            page += "\n<br>"
    page += "</body>\n</html>"

    print(page)

    return page


if __name__ == '__main__':
    # Actual address: http://<Wireless LAN adaptor Wi-Fi IP>:5000
    app.run(host='0.0.0.0', port=5000)
