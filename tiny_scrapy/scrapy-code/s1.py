from twisted.web.client import getPage, defer
from twisted.internet import reactor


def all_done(arg):
    reactor.stop()  #所有爬虫执行完后，终止循环

def callback(contents):
    print("#########\n")   #每一个爬虫结束后，自动执行
    print(contents)



deferred_list = []

url_list = ['http://www.bing.com', 'http://www.baidu.com', ]
for url in url_list:
    deferred = getPage(bytes(url, encoding='utf8'))  #创建一个请求对象
    deferred.addCallback(callback) #下载完成后执行回调函数 实现单线程的并发效果
    deferred_list.append(deferred)

dlist = defer.DeferredList(deferred_list)
dlist.addBoth(all_done)

reactor.run()  #事件循环