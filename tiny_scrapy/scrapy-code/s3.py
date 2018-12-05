from twisted.web.client import getPage, defer
from twisted.internet import reactor


# 2. 基于装饰器（二）
def all_done(arg):
    reactor.stop()


def onedone(response):
    print(response.decode('utf-8')[:100])


@defer.inlineCallbacks
def task():
    deferred2 = getPage(bytes("http://www.baidu.com", encoding='utf8'))
    deferred2.addCallback(onedone)
    print(1)
    yield deferred2

    print("##################")
    deferred1 = getPage(bytes("http://www.github.com", encoding='utf8'))
    deferred1.addCallback(onedone)
    print(2)
    yield deferred1


ret = task()
ret.addBoth(all_done)

reactor.run()