import socket

HOST = "0.0.0.0"
PORT = 31337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            conn.sendall(
                b"HTTP/1.1 200 OK\r\n"
                b"Server: MysteryTrainingService/1.0\r\n"
                b"Content-Type: text/plain\r\n"
                b"Connection: close\r\n\r\n"
                b"You found the service on TCP/31337.\n"
                b"uHvvZPjAxIPfZJuDMRPEHIAvW1njHoz7\n"
            )
