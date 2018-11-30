import requests
import json
#
# def post_detail():
#     url = []
#     for i in url:
#         i = requests.post(i,)

headers = {
'Host': 'www.pde.cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://www.pde.cn/PDEPORTAL2015/portal/html/coreContent.html?id=B7998992DC7146F2B061DE9EF5DFC6BB',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest',
'Content-Length': '40',
'Cookie': 'Hm_lvt_cd17d3ce3b64f227987cd92cd701cc58=1543473212; Hm_lpvt_cd17d3ce3b64f227987cd92cd701cc58=1543473212; nb-referrer-hostname=www.pde.cn; nb-start-page-url=http%3A%2F%2Fwww.pde.cn%2FPDEPORTAL2015%2Fportal%2Fhtml%2Findex.html%3Fv%3D2',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0'
}

def pp():
    yy = {}
    url = 'http://www.pde.cn/PDEPORTAL2015/PortalController/Solution/viewDetailByPK.do'
    dataall = ['A64A76CF63AA477B93FE95A22CCBFEFC',
'10DC724467A144E2B997EB4C4B851417',
'1379E56C8FD64129A68A5371D2E63500',
'74442BFA5DAA454D9860F15758113885',
'A0358D6BB5884F21922F55CD3784B4A8',
'A724DCD3E6CD455BA4A18EFA223889CD',
'8ACA6ABF2FC84DF8A1B9798C7BB117B3',
'F8DA02F17EB4428685CA45C99DA3F3C2',
'E216B9E74FF14E64BA643EFCFEB412F7',
'340EBB39490A4FE4A00B1A7D038631B9',
'C08F6E713AB94E509935812DE0B1FCE5',
'703F0BCB3B6F4356B3BB6CC6D9EBB9FC',
'BC161D07AF6C4C7688B7EEDAB4263BD7',
'D02AACAEBF3643A08940431030BEB5CD',
'0DE833950BC04E25B5B0A66B530FA6DA',
'2908D2485B9C41CDBFAB434EF6D329A4',
'81A87C2779B54338913EDA71C7755539',
'83886C631FCF4A598FFC4CAAE0F7F8CA',
'D7B64C40F58F430D90DBFDB4D915835B',
'E251655D1CE949A2AD1AF909C821626E']
    for j in dataall:
        # i ='CA2097161C9B4CF3B0107FEE99ED51C0'
        i=j
        data= 'solution_id={}'.format(i)
        # print(data)
        response= requests.post(url,data=data,headers=headers)
        contentdata = json.loads(response.text)
        print(contentdata)
        id= contentdata['result']['solution_id']
        ti=contentdata['result']['solution_title']
        print(ti)
        re= contentdata['result']['solution_content']
        print(re)
        yy.update()
        # print(id,ti,'\n',re,'\n')
#

if __name__ == '__main__':
    pp()