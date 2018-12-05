from twisted.web.client import getPage, defer
from twisted.internet import reactor


# 4. 基于装饰器，永恒循环
def all_done(arg):
    reactor.stop()


def onedone(response):
    print("****"*20)
    print(response.decode('utf-8')[:120])


@defer.inlineCallbacks
def task():
    deferred2 = getPage(bytes("http://www.baidu.com", encoding='utf8'))
    deferred2.addCallback(onedone)
    yield deferred2

    stop_deferred = defer.Deferred()
    # stop_deferred.callback(None)
    print(3)
    yield stop_deferred


ret = task()
ret.addBoth(all_done)

reactor.run()