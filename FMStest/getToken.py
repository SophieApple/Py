import requests,json

class get_Token():
    def __init__(self):
        self.tokenurl = []
        self.headers = {'token':'ZGV2LDE1Njc4Mzg4NTk1NTcsNWZkMGE4YTE4NjQzMzE4ZGVmOGY3ZjhmZDc4MjBmZTI='}
        pass

    def gettoken(self,start,end):
        for i in range(start,end):
            try:
                response = requests.get('http://192.168.83.200:8088/api/users/{}/token'.format(i),headers=self.headers).text
            except Exception as e:
                print(e)
            jr = len(json.loads(response).keys())
            if jr == 1:
                self.tokenurl.append(response)
        # print(self.tokenurl)

    def getpin(self,start=0,perpage=100):
        """
        api:/api/users?page=1&perpage=20&filter_name=
        """
        self.pinlist = []
        response_user = json.loads(requests.get('http://192.168.83.200:8088/api/users?page=1&perpage={}&filter_name='.format(perpage),headers=self.headers).text)
        for i in range(start,perpage):
            try:
                self.pinlist.append(response_user['users'][i]['pin'])
            except Exception as e:
                pass



a = get_Token()
# a.gettoken(1,100)
# print(a.tokenurl)
# print(len(a.tokenurl))
# print(len(set(a.tokenurl)))
a.getpin()
print(a.pinlist)
print(len(a.pinlist))
print(len(set(a.pinlist)))