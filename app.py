from flask import Flask, render_template, redirect, url_for, request, session, flash 
from datetime import timedelta 
# import json 
from video_download import download_video

app = Flask(__name__)
app.secret_key = "Me Yousef "
app.permanent_session_lifetime = timedelta(minutes= 2)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/download', methods = ["POST", "GET"])
def download(): 
    if request.method == "POST": 
        url = request.form["url"]
        return redirect(url_for("video", url = url))
    else:
        return render_template("download.html")
    

@app.route('/video/<url>')
def video(url): 
    download_video(url)
    return render_template("video_link.html", url = url)

# @app.route('/download_video', methods=['POST'])
# def download_video_endpoint():
#     data = request.json
#     url = data.get('url')
#     if not url:
#         return jsonify({"error": "URL is required"}), 400
    
#     output_path = 'videos/%(title)s-%(id)s.%(ext)s'
#     try:
#         download_video(url, output_path)
#         return jsonify({"video_url": output_path})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)




