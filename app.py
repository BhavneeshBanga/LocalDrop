from flask import Flask, render_template, request, send_from_directory
import os
import socket
import qrcode

app = Flask(__name__)

# Folder where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def get_lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def print_qr_in_terminal(url):
    qr = qrcode.QRCode(border=1)
    qr.add_data(url)
    qr.make(fit=True)
    print("\n" + "="*50)
    print(f"  📱 Scan this QR to open on mobile:")
    print(f"  🔗 {url}")
    print("="*50 + "\n")
    qr.print_ascii(invert=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return "❌ No file part in the request."
    
    files = request.files.getlist('files')
    if not files:
        return "❌ No files selected."
    
    saved_files = []
    for file in files:
        if file.filename != '':
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            saved_files.append(file.filename)
    
    if not saved_files:
        return "⚠️ No valid files uploaded."
    
    uploaded_list = "<br>".join(saved_files)
    return f"✅ Uploaded {len(saved_files)} files successfully!<br><br>{uploaded_list}"

@app.route('/files')
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    if not files:
        return "<h3>No files uploaded yet.</h3>"
    return '<br>'.join([f"<a href='/download/{file}'>{file}</a>" for file in files])

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    PORT = 5173
    lan_ip = get_lan_ip()
    url = f"http://{lan_ip}:{PORT}"
    print_qr_in_terminal(url)
    app.run(host='0.0.0.0', port=PORT, debug=True)