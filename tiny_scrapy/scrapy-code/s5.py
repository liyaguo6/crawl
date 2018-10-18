from twisted.web.client import getPage, defer
from twisted.internet import reactor

running_list = []
stop_deferred = None

def all_done(arg):
    reactor.stop()

def onedone(response,url):
    print(response)
    running_list.remove(url)

def check_empty(response):
    if not running_list:
        stop_deferred.callback(None)

@defer.inlineCallbacks
def open_spider(url):
    deferred2 = getPage(bytes(url, encoding='utf8'))
    deferred2.addCallback(onedone, url)
    deferred2.addCallback(check_empty)
    yield deferred2

@defer.inlineCallbacks
def stop(url):
    global stop_deferred
    stop_deferred = defer.Deferred()
    yield stop_deferred

@defer.inlineCallbacks
def task(url):
    yield open_spider(url)
    yield stop(url)


running_list.append("http://www.baidu.com")
ret = task("http://www.baidu.com")
ret.addBoth(all_done)

reactor.run()