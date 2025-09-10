import time
from datetime import datetime

# Đây chỉ là mô phỏng keylogger để minh họa
# Trong thực tế, việc sử dụng keylogger mà không có sự đồng ý là bất hợp pháp

def simulate_keylogger():
    print("Keylogger simulation started...")
    print("This is only for educational purposes!")
    
    # Giả lập ghi lại phím trong 2 phút
    start_time = time.time()
    end_time = start_time + 120  # 2 phút
    
    log_data = []
    
    print("Simulating keylogging for 2 minutes...")
    while time.time() < end_time:
        # Giả lập ghi phím
        simulated_key = f"Key pressed at {datetime.now()}"
        log_data.append(simulated_key)
        time.sleep(5)  # Giả lập mỗi 5 giây ghi một phím
    
    # Giả lập gửi email
    print("Simulating email sending to chamhoi8620@gmail.com...")
    print(f"Collected {len(log_data)} simulated keystrokes")
    
    # Lưu log vào file
    with open('keylog.txt', 'w') as f:
        for entry in log_data:
            f.write(entry + '\n')
    
    print("Simulation completed. Check keylog.txt for details.")

if __name__ == "__main__":
    simulate_keylogger()