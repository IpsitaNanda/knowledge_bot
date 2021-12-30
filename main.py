from flask import Flask, request, jsonify, render_template, url_for,session
import json
import os
import uuid
import time
import numpy as np
import pandas as pd
from datetime import datetime
from google.cloud import bigquery
from oauthlib.oauth2 import WebApplicationClient
from google.oauth2 import service_account
import base64
import hashlib
# Setting up the credentials to connect to Big Query
gcp_service_account_file = 'advance-conduit-336823-2d9878a5ca24.json'
credentials = service_account.Credentials.from_service_account_file(gcp_service_account_file)

#Flask Route
app = Flask(__name__)
app.secret_key = 'super secret string'
@app.route('/')
def home():
    return "Welcome to knowledgebot"
@app.route('/admincatalog', methods=['GET','POST'])
def admincatalog():
    if request.method == 'POST':
        # read inputs from a html form and create a python dictionary
        Itemname = request.form.get("Itemname")
        Category=request.form.get("Category")
        Created_datetime = ct.strftime("%m/%d/%Y %H:%M:%S")
        Last_modified=ct.strftime("%m/%d/%Y %H:%M:%S")
        Category_id=id
        catlogdet={"Itemname":Itemname,"Category": Category,"Category_id":Category_id,"Created_datetime":Created_datetime,"Last_modified":Last_modified}
        print(catlogdet)
        return catlogdet
        bigquery_con_admin(catlogdet)
    else:
        return render_template('Catalog.html')
    if __name__ == "__main__":
        app.run(debug=False, port=os.environ.get('PORT'), host='0.0.0.0')