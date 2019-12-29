#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/in_zen2.py
# Multi-shot server for the use of inetd(8).
# 代码清单7-11 对一个或多个客户端连接做出响应，最终发生超时

import socket, sys, zen_utils

if __name__ == '__main__':
    listener = socket.fromfd(0, socket.AF_INET, socket.SOCK_STREAM)
    sys.stdin = open('/dev/null', 'r')
    sys.stdout = sys.stderr = open('/tmp/zen.log', 'a', buffering=1)
    listener.settimeout(8.0)
    try:
        zen_utils.accept_connections_forever(listener)
    except socket.timeout:
        print('Waited 8 seconds with no further connections; shutting down')
