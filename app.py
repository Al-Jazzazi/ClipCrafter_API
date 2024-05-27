from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import timedelta 

app = Flask(__name__)
app.secret_key = "Me Yousef "
app.permanent_session_lifetime = timedelta(minutes= 2)

@app.route('/')
def hello():
    return "Video Processor API"


@app.route('/download_video', methods=['POST'])
def download_video_endpoint():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    output_path = 'videos/%(title)s-%(id)s.%(ext)s'
    try:
        download_video(url, output_path)
        return jsonify({"video_url": output_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)




