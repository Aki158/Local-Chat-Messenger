import socket
import os


def main():
    # ソケットを作成する
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    # アドレスを定義する
    server_address = '127.0.0.1'
    client_address = '127.0.0.2'
    
    try:
        # 前回の実行でソケットファイルが残っていた場合、そのファイルを削除する
        os.unlink(client_address)
    except FileNotFoundError:
        pass

    # クライアントのアドレスをソケットに紐付ける
    sock.bind(client_address)

    try:
        # コマンドラインからの入力をサーバに送信する
        message = input('Input message : ').encode()
        print('sending : {!r}'.format(message))
        sent = sock.sendto(message,server_address)

        # サーバからデータを受け取ってメッセージを表示する
        data, server = sock.recvfrom(4096)
        print('received : {!r}'.format(data))

    finally:
        # 最後にソケットを閉じてリソースを解放する
        print('closing socket')
        sock.close()


if __name__ == '__main__':
    main()
