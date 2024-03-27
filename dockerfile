# Sử dụng image cơ sở
FROM alpine:latest

# Cài đặt các gói cần thiết
RUN apk --no-cache add curl

# Sao chép tệp .env vào container
COPY .env .

# Mở cổng được xác định bởi biến môi trường PORT
EXPOSE $PORT

# Thực thi lệnh curl khi container khởi động
CMD curl -s -S -L <https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/scripts/install.sh> | sh -s -- -v
