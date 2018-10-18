from twisted.web.client import getPage, defer
from twisted.internet import reactor


# 2. 基于装饰器（一）
def all_done(arg):
    reactor.stop()

def onedone(response):
    print(response)


@defer.inlineCallbacks
def task(url):
    deferred = getPage(bytes(url, encoding='utf8'))
    deferred.addCallback(onedone)
    yield deferred


deferred_list = []

url_list = ['http://www.bing.com', 'http://www.baidu.com', ]
for url in url_list:
    deferred = task(url)
    #  deferred = getPage(url)
    # deferred.addCallback(onedone)
    deferred_list.append(deferred)

dlist = defer.DeferredList(deferred_list)
dlist.addBoth(all_done)

reactor.run()