from flask import Flask, request, render_template_string
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            # file.save(f'./uploads/{filename}')  # Tùy chọn lưu tệp nếu cần thiết
            return f"Uploaded: {filename}"
    return render_template_string('''
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <input type="submit" value="Upload">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
