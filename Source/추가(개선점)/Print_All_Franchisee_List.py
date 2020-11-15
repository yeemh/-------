#모든 가맹점 리스트 받아오기
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

API_KEY = #deleted API_KEY
S_CD = [41110, 41460] #시군코드->수원:41110, 용인:41460

def get_franchisee(s_cd):
    #지역화폐 가맹점 api 받아오기
    franchisee=[]
    if s_cd == 0:
        for i in range(1,52):
            url = "https://openapi.gg.go.kr/RegionMnyFacltStus?Key={0}&SIGUN_CD={1}&pIndex={2}&pSize=1000".format(API_KEY, S_CD[s_cd],i)
            #BeautifulSoup 이용하여 파싱
            request = urllib.request.urlopen(url)
            xml = request.read()
            soup = BeautifulSoup(xml, 'html.parser')
            franchisee += soup.find_all("row")
    else:
        for i in range(1, 37):
            url = "https://openapi.gg.go.kr/RegionMnyFacltStus?Key={0}&SIGUN_CD={1}&pIndex={2}&pSize=1000".format(API_KEY, S_CD[s_cd],i)
            #BeautifulSoup 이용하여 파싱
            request = urllib.request.urlopen(url)
            xml = request.read()
            soup = BeautifulSoup(xml, 'html.parser')
            franchisee += soup.find_all("row")
    return franchisee

print(get_franchisee(1))
