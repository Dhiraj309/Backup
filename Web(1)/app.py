from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Define the folder for static files (images, css, js, etc.)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Path to save uploaded files
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'jpg', 'jpeg', 'png', 'gif', 'mp4', 'mkv', 'avi', 'mov', 'csv', 'xlsx', 'xls'}

# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route for the sign-in page
@app.route('/sign')
def sign():
    return render_template('sign.html')

# Route for file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    # If the file is valid
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)  # Save the file
        
        # Redirect to uploaded file page with the filename
        return redirect(url_for('uploaded_file', filename=file.filename))
    else:
        return "Invalid file format, please upload a valid file."

# Route to display uploaded file (you can modify this to show file details)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return f'File {filename} uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)
