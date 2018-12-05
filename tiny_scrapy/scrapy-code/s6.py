from twisted.web.client import getPage, defer
from twisted.internet import reactor

class ExecutionEngine(object):
    def __init__(self):
        self.stop_deferred = None
        self.running_list = []

    def onedone(self,response,url):
        print(response.decode("utf-8")[:120])
        self.running_list.remove(url)

    def check_empty(self,response):
        if not self.running_list:
            self.stop_deferred.callback(None)

    @defer.inlineCallbacks
    def open_spider(self,url):
        deferred2 = getPage(bytes(url, encoding='utf8'))
        deferred2.addCallback(self.onedone, url)
        deferred2.addCallback(self.check_empty)
        yield deferred2

    @defer.inlineCallbacks
    def stop(self,url):
        self.stop_deferred = defer.Deferred()
        yield self.stop_deferred

@defer.inlineCallbacks
def task(url):
    engine = ExecutionEngine()
    engine.running_list.append(url)

    yield engine.open_spider(url)
    yield engine.stop(url)

def all_done(arg):
    reactor.stop()

if __name__ == '__main__':
    url_list =["http://www.baidu.com","http://www.bing.com","http://www.google.com","http://www.github.com"]
    ret = task("http://www.baidu.com")
    ret.addBoth(all_done)

    reactor.run()