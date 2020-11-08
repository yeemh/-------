# Suwon-Yongin-Franchisee-List
용인시와 수원시의 지역 화폐 가맹점 현황

# 수원, 용인 지역화폐 가맹점  분석

# 1. 프로젝트 목표 및 내용

 용인시와 수원시의 지역 화폐 가맹점 현황을 모두 받아와 수원 또는 용인시의 가맹점 리스트를 보여주고 지역구, 업종별로도 선택하여 볼 수 있게 한다. 용인과 수원 중 현재 위치를 선택하여 상호명을 입력하였을 시 현재 위치를 받아와 근처에 일치하는 가맹점이 있는지 찾아 출력하여 주도록 한다. 수원시와 용인시를 제외한 지역구, 업종, 상호명은 입력을 하지 않을 시 리스트에 포함되어 있는 모든 가맹점들을 출력하도록 한다.

# 2. 주제 선정 이유

 현재 코로나 사태로 인하여 경기도에서 경기도민들에게 경기도 재난 기본소득을 지급하였다. 경희대학교 국제캠퍼스 또한 경기도에 위치하여 있고 그로 인해 학교 근처에 거주하고 있는 주소지를 옮긴 학생들도 그 혜택을 받을 수 있게 되었다. 그런데 재난 기본소득은 주민등록상 거주지를 기준으로만 사용할 수 있고 학교의 위치 특성상 횡단보도 하나를 기준으로 용인시와 수원시로 바뀌게 되어 어느 지역의 지역 화폐가 사용 가능한지에 혼동이 올 수 있다. 현재 이를 확인하기 위한 방법으로 경기도에서 제공하는 웹페이지가 있지만 많은 사람이 접속하는 상황 속에서 서버가 다운되거나 느려지는 경우가 잦아 용인과 수원시에 한해서만 가맹점 정보를 받아와 빠르게 확인할 수 있도록 정보를 제공하고자 한다.

# 3. 데이터 획득

1. 경기데이터드림 - 지역화폐 가맹점 현황
 시군코드를 기준으로 가맹점 리스트를 받아오고 상호명과 위도 경도를 이용하여 현재 위치에서 일치하는 가맹점과 업종, 주소, 전화번호를 Beautiful Soup를 이용하여 파싱한다.<br>
 또한 지역화폐가맹점현황 파일을 받아와 수원시와 용인시 현황만 분류하고, 시군코드, 업종에 대한 데이터를 얻는다.
2. Google Cloud Platform - Geolocation API
 현재 위치에 대한 정보를 받아온다. 현재의 IP 주소를 참조하여 위치를 받아온다. 위도와 경도 그리고 정확도로 현재 위치를 알아낼 수 있다.

# 4. 참고문헌

1. 경기데이터드림: https://data.gg.go.kr/portal/data/service/selectServicePage.do?infId=3NPA52LBMO36CQEQ1GMY28894927&infSeq=1 (지역화폐 가맹점 현황)
2. Geolocation API: https://developers.google.com/maps/documentation/geolocation/intro?utm_source=google&utm_medium=cpc&utm_campaign=FY18-Q2-global-demandgen-paidsearchonnetworkhouseads-cs-maps_contactsal_saf&utm_content=text-ad-none-none-DEV_c-CRE_396485512938-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+~+Places+%7C+EXA+%7C+Google+Maps+Geolocation+API-KWID_43700049561316526-kwd-300650646226-userloc_1009877&utm_term=KW_google%20geolocation%20api-ST_google+geolocation+api&gclid=EAIaIQobChMIrPytw42h6QIVhmkqCh10EQXNEAAYASAAEgIMnfD_BwE#introduction (Geolocation API-Developer Guide)
3. 지역화폐 가맹점 현황_오픈API명세서.xls
4. 지역화폐가맹점현황.csv
5. 지역화폐가맹점현황_수원.csv/지역화폐가맹점현황_용인.csv
6. https://velog.io/@yvvyoon/python-current-location-coordinate (Python - 현재 위치 좌표 알아내기)
7. https://twpower.github.io/84-how-to-use-beautiful-soup ([Python] Beautiful Soup(뷰티플 수프) 사용법과 예제)
8. https://lovestudycom.tistory.com/entry/%EC%9C%84%EB%8F%84-%EA%B2%BD%EB%8F%84-%EA%B3%84%EC%82%B0%EB%B2%95 (위도, 경도 계산법)
9. https://pypi.org/project/beautifultable/ (beautifultable 공식 페이지)<br>
   https://beautifultable.readthedocs.io/en/latest/quickstart.html (beautifultable 공식 문서)
10. https://pypi.org/project/wcwidth/ (한글 정렬을 위한 wcwidth library)
