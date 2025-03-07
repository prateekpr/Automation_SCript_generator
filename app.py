from flask import Flask, render_template, request, jsonify
import os
from backend.generator import generate_test_script

# Specify the correct paths for templates and static files
app = Flask(
    __name__,
    template_folder="templates",  # Path to templates folder
    static_folder="frontend/static"  # Path to static folder
)


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({"message": "File uploaded successfully", "filepath": filepath}), 200

@app.route("/generate", methods=["POST"])
def generate_scripts():
    data = request.json
    framework = data.get("framework")
    filepath = data.get("filepath")

    if not framework or not filepath:
        return jsonify({"error": "Framework or filepath missing"}), 400

    with open(filepath, "r") as f:
        test_cases = f.read()

    scripts = generate_test_script(framework, test_cases)
    return jsonify({"scripts": scripts})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)