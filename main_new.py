## History ##
# Modify EXCEL FILE & OVERLAY for guide update - 2026/02/28
from flask import Flask, render_template ,request
from flask import send_file
from fab2 import EXCEL_TO_TEXT_SPD_NEW_r3,F2_NIKON_ASML_MERGE_SPD_NEW_r1
from fab2 import F2_OVERLAY_MAIN_MERGE_HC18_r1,F2_OVERLAY_MAIN_MERGE_SPD_NEW_r3
import os, datetime

# 전역변수 
OUT_FILE = None
# Flask 객체 인스턴스 생성
app = Flask(__name__)
date = datetime.datetime.now().strftime("%y%m%d")

UPLOAD_FOLDER = 'upload'  # File Upload Folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/') # 접속 url
def index():
  return render_template('index_F2.html')
 
@app.route('/FAB2_PHOTOKEY')
def FAB2_PHOTOKEY():
  return render_template('FAB2_PHOTOKEY_r1.html')

@app.route('/GEN_FAB2_PHOTOKEY', methods=['POST','GET'])
def GEN_FAB2_PHOTOKEY():
    if 'file' not in request.files:
        return '[File not found]'
    file = request.files['file']
    if file.filename == '':
        return '[File name not found]'
    
    # Photokey guide file upload
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    if request.method == 'POST':
       process = request.form.get('Process')
    # Guide file path & name
    file_name = file.filename
    file_location = file_path
    
    EXCEL_TO_TEXT_SPD_NEW_r3.photokey_files(file_name,process) # Split the input_file.
    if ('HC18' in process) or ('BD13' in process): # Check for Si-Capacitor process.
       F2_OVERLAY_MAIN_MERGE_HC18_r1.main(process) # Si-Capacitor process.(GDS-2type)
    else:
       F2_OVERLAY_MAIN_MERGE_SPD_NEW_r3.main(process)   # Normal & SiC process.
    OUT_FILE = F2_NIKON_ASML_MERGE_SPD_NEW_r1.main(process) # Si-Capacitor & Normal & SiC process.
    return render_template('FAB2_OUTPUT.html',OUT_FILE=OUT_FILE)

@app.route('/FAB2_OUTPUT_FILE')
def FAB2_OUTPUT_FILE():
    global OUT_FILE
    if OUT_FILE and os.path.exists(OUT_FILE):
        return send_file(OUT_FILE, as_attachment=True)
    else:
        return '[Output photokey-gds not found]'

if __name__=="__main__":
  # app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  app.run(host="0.0.0.0", port="5050", debug=True)