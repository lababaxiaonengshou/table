import requests
import  json

class TranslateMedical():
    def __init__(self):
        super().__init__()
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            'token': 'Fk89AxyDz2bEDCdyxVW5LqGBA+g=',
            'cookie': '_ga=GA1.2.86242203.1550501303; Hm_lvt_d9c0d68230697bbc3fbe9ec1490021c1=1591699815,1591752583,1591769987,1592474918; Hm_lpvt_d9c0d68230697bbc3fbe9ec1490021c1=1592474918; _gid=GA1.2.1509640543.1592474918'
        }

        self.TranslateData = {
            'target': 'en',
            'source': 'zh',
            'text': '你好',
            'type': '1'
        }

        

        self.TranslateUrl = 'https://www.geenmedical.com/api/translate'
        self.QueryUrl = 'https://www.geenmedical.com/api/translate/history?p=0'
        self.DetectUrl = 'https://www.geenmedical.com/api/translate/detect'

    def getdetection(self,world):
        DetectData = {
            'text' : world
        }
        self.TranslateData['text'] = world
        try :
            Detection = requests.post(self.DetectUrl,headers=self.headers,data = DetectData )
            Detresult = json.loads(Detection.text)
            Lang = Detresult['data']['Lang']
            if Lang == 'en':
                self.TranslateData['target'] = 'zh'
                self.TranslateData['source'] = 'en'
            
        except :
            pass
       


    def getquery(self):
        try:
            query = requests.get(self.QueryUrl,headers = self.headers)
        except :
            pass
        

    def gettranslate(self):
        try:
            response = requests.post(self.TranslateUrl,headers = self.headers,data = self.TranslateData)
            text = json.loads(response.text)
            #print(response.text)
            result = text['data']['TargetTexts'][0]['Target']
            print(result)
            return result
        except :
            pass

    def run(self,world):
        self.getdetection(world)
        self.getquery()
        return self.gettranslate()

if __name__ == "__main__":
    tran = TranslateMedical()
    tran.run('National Institutes of Health Search database')
        
  