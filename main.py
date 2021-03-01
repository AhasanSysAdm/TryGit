from flask import Flask, render_template ,request, send_from_directory,Response
from flask import jsonify
import json
import re
import os
import scipy.misc
import warnings
import sys
import compare_image
import time
from werkzeug.utils import secure_filename

app = Flask(__name__)
 


@app.route('/compare_faces', methods=['POST'])
def compare_faces():
    target = request.files['target']
    face =  request.files["face"]
    target_filename=secure_filename(target.filename)
    face_filename=secure_filename(face.filename)
    response=[]
    start = time.time()
    confidence,result = compare_image.main(target,face)
    end=time.time()
    response={
           'result':str(result),
           'confidence':round(confidence,2),
           'time_taken':round(end-start,3),
           'target':target_filename,
           'face':face_filename
        }
    python2json = json.dumps(response)
    return app.response_class(python2json, content_type='application/json') 

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8000)