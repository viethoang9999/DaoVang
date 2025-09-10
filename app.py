from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    # Đường dẫn đến file game (giả lập)
    game_path = "/app/game/GameSetup.exe"
    
    # Kiểm tra nếu file tồn tại
    if os.path.exists(game_path):
        return send_file(game_path, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)