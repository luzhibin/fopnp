[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 7<br>Server Architecture
# 第7章 服务器架构
---
### 以下是含有代码的章节
* 7.2 一个简单的协议
    * 代码清单7-1 支持《Python之禅》示例协议的数据与规则
    * 代码清单7-2 用于《Python之禅》示例协议的客户端程序
* 7.3 单线程服务器
    * 代码清单7-3 最简单的可用服务器是单线程的
* 7.4 多线程与多进程服务器
    * 代码清单7-4 多线程服务器
    * 代码清单7-5 使用标准库服务器模式构建的多线程服务器
* 7.5 异步服务器
    * 代码清单7-6 一个简单的异步事件循环
* 7.5.1 回调风格的asyncio
    * 代码清单7-7 回调风格的asyncio服务器
* 7.5.2 协程风格的asyncio
    * 代码清单7-8 协程风格的asyncio服务器
* 7.5.3 遗留模块的asyncore
    * 代码清单7-9 使用旧式的asyncore框架
* 7.6 在inetd下运行
    * 代码清单7-10 响应一个将套接字连接到stdin/stdout/stderr的客户端
    * 代码清单7-11 对一个或多个客户端连接做出响应，最终发生超时
---    
This is a directory of program listings from Chapter 7 of the book:

<dl>
<dt><i>Foundations of Python Network Programming</i></dt>
<dd>
Third Edition, October 2014<br>
by Brandon Rhodes and John Goerzen
</dd>
</dl>

You can learn more about the book by visiting the
[root of this GitHub source code repository](https://github.com/brandon-rhodes/fopnp#readme).

Although the scripts in this chapter were written for Python 3, nearly
all of them can also be run successfully under Python 2.  Simply use
[3to2](https://pypi.python.org/pypi/3to2) to convert them to the older
syntax.  The two that can run only under Python 3 are the two `asyncio`
scripts, because the `asyncio` framework depends upon the `yield from`
syntax that was not introduced until Python 3.

This chapter implements the same network service seven different ways.
The seven different servers look pretty much the same when run from the
command line, which is more or less the point.  What is interesting
about them is how differently they are written while yet providing
exactly the same network service.

Any of the server scripts, when run at the command line, will let the
single client script — the appropriately named `client.py` — connect and
ask a series of questions to which the server replies with answers.

```
$ python3 srv_single.py '' &>server.log &
```

```
$ python3 client.py localhost
b'Simple is better than?' b'Complex.'
b'Beautiful is better than?' b'Ugly.'
b'Explicit is better than?' b'Implicit.'
```

```
$ cat server.log
Listening at ('', 1060)
Accepted connection from ('127.0.0.1', 41285)
Client socket to ('127.0.0.1', 41285) has closed
```

You can run the `test.sh` script if you want to verify that all seven
work correctly on your platform.  The script will start each of the
servers in turn, and see whether the client can really connect or not.

Two final versions of the Zen-of-Python server require a bit of manual
configuration: the servers that are designed to run under the `inetd`
daemon.  You can try them in the [Playground](../../playground#readme)
on the `ftp.example.com` host, where `inetd` happens to already be
running to provide a Telnet service for the scripts in Chapter 16.  Once
you have the playground running, create a client host like `h1`:

    $ ssh h1

Because each client host auto-mounts the `py3` directory, you will have
access to the scripts and configuration file that need to be copied over
to `ftp.example.com` for the two services to run.  You can perform the
copy using the following commands on host `h1`:

    # cd /fopnp/py3/chapter07
    # scp in_zen1.py in_zen2.py zen_utils.py ftp.example.com:/
    # scp inetd.conf ftp.example.com:
    # ssh ftp.example.com

Once the `ssh` command has offered you a prompt on the `ftp` machine,
you can run `ps` to verify that `inetd` is indeed running.

    # ps axf
      PID TTY      STAT   TIME COMMAND
    ...
       36 ?        Ss     0:00 /usr/sbin/inetd
    ...

Next, add the Zen-of-Python service to the existing list of `inetd`
services, and mark the Python scripts as publicly readable so that they
can be run as the `brandon` user:

    # cat inetd.conf >> /etc/inetd.conf
    # /etc/init.d/openbsd-inetd reload
    # chmod a+r /*.py

You can now log back out of the `ftp` host and, from the `h1` host,
connect to the `inetd` powered servers on both of the port numbers
mentioned in `inet.conf`:

    # python3 client.py ftp.example.com -p 1060

    b'Beautiful is better than?' b'Ugly.'
    b'Explicit is better than?' b'Implicit.'
    b'Simple is better than?' b'Complex.'

    # python3 client.py ftp.example.com -p 1061

    b'Beautiful is better than?' b'Ugly.'
    b'Simple is better than?' b'Complex.'
    b'Explicit is better than?' b'Implicit.'

If you later log back in to the `ftp` host, you can view the logs of
both servers.

    # cat /tmp/zen.log

    Accepted connection from ('10.25.1.65', 49327)
    Client socket to ('10.25.1.65', 49327) has closed
    Accepted connection from ('10.25.1.65', 49328)
    Client socket to ('10.25.1.65', 49328) has closed
