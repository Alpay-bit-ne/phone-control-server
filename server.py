import socket
import threading

clients = []

def handle_client(client_socket, addr):
    print(f"[+] {addr} bağlandı.")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"[{addr}] {data.decode()}")
        except:
            break
    print(f"[-] {addr} ayrıldı.")
    clients.remove(client_socket)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9090))  # Render'da otomatik IP atanır
    server.listen()
    print("[*] Sunucu başlatıldı, bağlantılar bekleniyor...")

    while True:
        client, addr = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

start_server()
