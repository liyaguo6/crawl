from twisted.web.client import getPage, defer
from twisted.internet import reactor

running_list = []
stop_deferred = None

def all_done(arg):
    print(9)
    reactor.stop()

def onedone(response,url):
    print(3)
    print(response.decode('utf-8')[:120].replace("\n",""))
    print(4)
    # running_list.remove(url)

def check_empty(response):
    print(5)
    if not running_list:
        print(stop_deferred)
        stop_deferred.callback(None)

@defer.inlineCallbacks
def open_spider(url):
    deferred2 = getPage(bytes(url, encoding='utf8'))
    deferred2.addCallback(onedone, url)
    deferred2.addCallback(check_empty)
    print(2)
    yield deferred2

@defer.inlineCallbacks
def stop(url):
    global stop_deferred
    # print(stop_deferred)
    print(7)
    stop_deferred = defer.Deferred()
    running_list.remove(url)
    # stop_deferred.callback(check_empty)
    print(8)
    yield stop_deferred

@defer.inlineCallbacks
def task(url):
    print(1)
    yield open_spider(url)
    print(6)
    yield stop(url)


running_list.append("http://www.baidu.com")
ret = task("http://www.baidu.com")

ret.addBoth(all_done)


reactor.run()