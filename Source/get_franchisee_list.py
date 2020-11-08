#수원/용인 가맹점 리스트 받아오기

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

API_KEY = '3a1c50808284421e8999527c4b4d9c92'
S_CD = [41110, 41460] #시군코드->수원:41110, 용인:41460

def get_franchisee(s_cd):
    #지역화폐 가맹점 api 받아오기
    url = "https://openapi.gg.go.kr/RegionMnyFacltStus?Key={0}&SIGUN_CD={1}&pIndex=6&pSize=1000".format(API_KEY, S_CD[s_cd])
    #BeautifulSoup 이용하여 파싱
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    franchisee = soup.find_all("row")
    return franchisee

