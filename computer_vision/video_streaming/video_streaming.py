import cv2
import socket
import pickle
import struct


def server_pickle_struct(port: int = 8888):
    """
    https://medium.com/@anshulsjr6/building-a-basic-video-streaming-application-in-python-with-opencv-cfb6995e2479
    Basic code to stream video from a webcam
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print("Server is listening...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} accepted")
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        frame_data = pickle.dumps(frame)
        client_socket.sendall(struct.pack("Q", len(frame_data)))
        client_socket.sendall(frame_data)
        cv2.imshow("Server", frame)
        if cv2.waitKey(1) == 13:
            break
    cap.release()
    cv2.destroyAllWindows()


def client_pickle_struct(server_ip_address: str, port: int = 8888):
    """
    https://medium.com/@anshulsjr6/building-a-basic-video-streaming-application-in-python-with-opencv-cfb6995e2479
    Basic code to receive video from a server streaming video
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(
        (server_ip_address, port)
    )  # Replace 'server_ip_address' with the actual server IPdata = b""
    payload_size = struct.calcsize("Q")
    data = b""
    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 4K buffer size
            if not packet:
                break
            data += packet
        if not data:
            break
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]
        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)  # 4K buffer size
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        cv2.imshow("Client", frame)
        if cv2.waitKey(1) == 13:
            break
    cv2.destroyAllWindows()
