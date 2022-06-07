import os
from app import app
from flask import request, jsonify
from worker.utils import test_size
from werkzeug.utils import secure_filename
from worker.blur import blur_check, blur_test


@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413


@app.route('/check', methods=['POST'])
def check():
    if 'file' in request.files:
        file = request.files['file']
        if test_size(file, app.config['MAX_CONTENT_LENGTH']):
            filename = secure_filename(file.filename)
            if filename != '':
                ext = os.path.splitext(filename)[1]
                if ext.lower() in app.config['UPLOAD_EXTENSIONS']:
                    res = blur_check(file)
                    if not res['error']:
                        return jsonify(msg='Image processed successfully.', blur_coefficient=res['blur_coefficient']), 200
                    else:
                        return jsonify(msg='Ups. Something went wrong!'), 500
                else:
                    return jsonify(msg=f'Support only {app.config["UPLOAD_EXTENSIONS"]} files.'), 415
        else:
            return jsonify(msg=f'File too large. Max. {app.config["MAX_CONTENT_LENGTH"]}.'), 413
        
    return jsonify(msg='Empty request.'), 204

@app.route('/test', methods=['POST'])
def test():
    if not request.is_json:
        blur_accepted = float(request.form['blur_accepted']) if request.form and request.form['blur_accepted'] else None
        
        if 'file' in request.files:
            file = request.files['file']
            if test_size(file, app.config['MAX_CONTENT_LENGTH']):
                filename = secure_filename(file.filename)
                if filename != '':
                    ext = os.path.splitext(filename)[1]
                    if ext.lower() in app.config['UPLOAD_EXTENSIONS']:
                        res = blur_test(file, blur_accepted)
                        if not res['error']:
                            return jsonify(msg='Image processed successfully.', blur_coefficient=res['blur_coefficient'],  accepted=bool(res['accepted'])), 200
                        else:
                            return jsonify(msg='Ups. Something went wrong!'), 500
                    else:
                        return jsonify(msg=f'Support only {app.config["UPLOAD_EXTENSIONS"]} files.'), 415
            else:
                return jsonify(msg=f'File too large. Max. {app.config["MAX_CONTENT_LENGTH"]}.'), 413
            
        return jsonify(msg='Empty request.'), 204
    
    return jsonify(msg='Bad request.'), 400
