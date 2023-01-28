import socket

def send_to_socket(data, callback=lambda x:x, host='localhost', port=3003):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host, port)

    for d in data:
        sock.sendto(bytes(str(callback(d)), 'ascii'),server_address)
    # Close the socket
    sock.close()


