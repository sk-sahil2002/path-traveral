from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Vulnerable File Viewer</h1>
    <form method="GET" action="/view">
        <label for="filename">Enter file name:</label>
        <input type="text" id="filename" name="filename">
        <input type="submit" value="View File">
    </form>
    '''

@app.route('/view')
def view_file():
    filename = request.args.get('filename')
    if not filename:
        return "No file specified."

    # Vulnerable code that allows path traversal
    try:
        return send_file(os.path.join('uploads', filename))
    except FileNotFoundError:
        return abort(404, description="File not found")

if __name__ == '__main__':
    app.run(debug=True)