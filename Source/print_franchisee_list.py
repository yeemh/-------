#가맹점 리스트 출력

from beautifultable import BeautifulTable

def print_franchisee_list(fr_list):
    #검색 결과가 없는 경우
    if not fr_list:
        print("검색 결과가 없습니다.")
        return
    table = BeautifulTable()
    table.column_headers = ["상호명","업종","주소","전화번호"]
    for i in fr_list:
        table.append_row([i.cmpnm_nm.string, i.indutype_nm.string, i.refine_roadnm_addr.string, i.telno.string])
    print(table)

