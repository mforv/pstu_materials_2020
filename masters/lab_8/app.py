#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
import pandas as pd

app = flask.Flask(__name__)
app.debug = True

@app.route('/')
def index():
    with open('./data.txt', 'r', encoding='utf-8') as f:
        dataframe = pd.read_csv(f, sep='\t', names=['name', 'version', 'size', 'date'], parse_dates=[3])
        print(dataframe)
    return flask.render_template('index.html', data=dataframe.iterrows())

@app.route('/api')
def api_like():
    return flask.render_template('api.html')

@app.route('/list', methods=['GET'])
def list_packages():
    '''Примет API-подобного ответа на запрос'''
    packages = []
    with open('./data.txt', 'r', encoding='utf-8') as f:
        dataframe = pd.read_csv(f, sep='\t', names=['name', 'version', 'size', 'date'])
        for row in dataframe.iterrows():
            packages.append(row[1].to_dict())
    return flask.jsonify(packages)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)
