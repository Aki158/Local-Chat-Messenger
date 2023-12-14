from faker import Faker
import socket
import os


def main():
    # ソケットを作成する
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    # アドレスを定義する
    server_address = '127.0.0.1'

    try:
        # 前回の実行でソケットファイルが残っていた場合、そのファイルを削除する
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print('starting up on {}'.format(server_address))

    # サーバのアドレスをソケットに紐付ける
    sock.bind(server_address)

    print('\nwaiting to receive message')

    # クライエントのソケットからのデータを受信する
    data, address = sock.recvfrom(4096)

    # 受信したデータを表示する
    print('received data : {}'.format(data))

    # 偽データをクライエントに送り返す
    if data:
        fake = Faker()
        fakeText = fake.text().encode()
        sent = sock.sendto(fakeText, address)
        print('sent data : {}'.format(fakeText))

    # 最後にソケットを閉じてリソースを解放する
    print('closing socket')
    sock.close()

if __name__ == '__main__':
    main()
