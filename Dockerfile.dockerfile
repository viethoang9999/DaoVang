FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Tạo thư mục downloads nếu chưa tồn tại
RUN mkdir -p downloads

# Tải file game từ link bạn cung cấp (giả lập)
RUN echo "This would download the actual game file" > downloads/game.exe

EXPOSE 5000

CMD ["python", "app.py"]