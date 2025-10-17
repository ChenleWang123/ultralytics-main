import re  # 为了正则表达式
import requests  # 请求网页url
import os  # 操作系统
import time,sys

num = 0  # 给图片名字加数字
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    'Cookie': 'BDqhfp=%E7%95%AA%E8%8C%84%E6%97%A9%E7%96%AB%E7%97%85%26%26NaN-1undefined%26%26612%26%262; BIDUPSID=08923450BAABF97604AC0326EE7A8F45; PSTM=1689258975; BAIDUID=08923450BAABF976A5AD764BB3688D10:SL=0:NR=10:FG=1; MCITY=-233%3A; BDUSS=hXd1VheWFObHBVMWxKcmE4NjlpNzRZQUV4UEJmOVFIVkpvTHZEc3lJdHd4dWxrRVFBQUFBJCQAAAAAAAAAAAEAAADSimpSQ2hhcmxlc19XYW5nMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHA5wmRwOcJkbX; BDUSS_BFESS=hXd1VheWFObHBVMWxKcmE4NjlpNzRZQUV4UEJmOVFIVkpvTHZEc3lJdHd4dWxrRVFBQUFBJCQAAAAAAAAAAAEAAADSimpSQ2hhcmxlc19XYW5nMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHA5wmRwOcJkbX; BAIDUID_BFESS=08923450BAABF976A5AD764BB3688D10:SL=0:NR=10:FG=1; ZFY=w7WlNk:BAPdQ43BPotuj09x7k8w5VpLXkw:BvlEQtHhjs:C; ariaDefaultTheme=undefined; delPer=0; BA_HECTOR=a0818g0l04a18080aha4210q1id106e1o; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; userFrom=www.baidu.com; PSINO=6; H_PS_PSSID=36552_39112_38831_39114_39121_39037_38918_26350_39138_39137_39100_39043; ZD_ENTRY=baidu',
    # 根据自己的浏览器情况自行填写
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}  # 请求头，谷歌浏览器里面有

species = 'image'
keyword = '大街路口图片' # 关键字
max_page = 3
i=1 # 记录图片数

for page in range(1,max_page+1):
    page = page*30
    # 网址
    # url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='\
    #         +keyword+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word='\
    #         +keyword+'&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=wallpaper&pn='\
    #         +str(page)+'&rn=30&gsm=1e&1596899786625='


    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11047437738312072929&ipn=rj&ct=201326592&is=&fp=result&fr=' \
          '&word=' + keyword + '&queryWord=' + keyword + '&cl=2&lm=-1' \
          '&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=' \
          '&qc=&nc=1&expermode=&nojc=&isAsync=&pn=' + str(page) + '&rn=30&gsm=1e&1691399176268='

    # 图片页面的url
    # url = 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MTEsMCw0LDIsMywxLDYsNSwsNyw4LDk%3D&word=%E7%95%AA%E8%8C%84%E6%97%A9%E7%96%AB%E7%97%85'
    # 通过requests库请求到了页面
    html = requests.get(url, headers=header)
    # 防止乱码
    html.encoding = 'utf8'
    # 打印页面出来看看
    print(html.text)

    json = html.json()
    if json.get('data'):
        for item in json.get('data')[:30]:

            path = 'C:/Users/WCL/Desktop/' +'/'+ species +'/'+ keyword
            if not os.path.exists(path):
                os.makedirs(path)

            # 图片地址
            img_url = item.get('thumbURL')
            # 获取图片
            image = requests.get(url=img_url)
            # 下载图片
            file_name = 'C:/Users/WCL/Desktop/' +'/'+ species +'/'+ keyword + '/picture' + str(
                i) + ".jpg"  # 给下载下来的图片命名。加数字，是为了名字不重复
            f = open(file_name, "wb")  # 以二进制写入的方式打开图片
            f.write(image.content)  # 往图片里写入爬下来的图片内容，content是写入内容的意思

            print(i,'.',img_url)  # 看看有哪些url

            i += 1
