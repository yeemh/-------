# 구/업종별 가맹점 리스트 출력

import get_franchisee_list
import select_district
import select_industry
import print_franchisee_list
from beautifultable import BeautifulTable

def select_pr_fr():
    #시 선택
    s_cd = input("\n\n시: [1]수원 [2]용인 \n\nSelect: ")

    if s_cd == "1": #수원 선택
        s_cd = 0
        fr_list = get_franchisee_list.get_franchisee(s_cd)
    elif s_cd == "2": #용인 선택
        s_cd = 1
        fr_list = get_franchisee_list.get_franchisee(s_cd)
    else: #예외처리
        print("Invalid Number.")
        return

    #구 선택
    d_nm = input("\n\n구(※입력 없을 시 모두 출력): ")
    
    if d_nm != "": #사용자가 구 입력 시
        if d_nm[-1] != "구": #마지막 글자 구를 빼고 입력한 경우 끝에 구 추가
            d_nm = d_nm + "구"
        fr_list = select_district.select_district(fr_list, d_nm)

    #검색 결과가 없는 경우 예외처리
    if not fr_list:
        print("검색 결과가 없습니다.")
        return

    #업종별 선택
    print("\n\n업종명(※입력 없을 시 모두 출력):")
    #업종명 종류 보여주기
    table = BeautifulTable()
    table.append_row(["[1]숙박", "[2]여행", "[3]레저", "[4]문화/취미", "[5]의류/잡화/생활가전"])
    table.append_row(["[6]주유소", "[7]유통", "[8]서적/문구", "[9]학원", "[10]사무통신"])
    table.append_row(["[11]자동차판매", "[12]서비스", "[13]보험", "[14]병원", "[15]약국"])
    table.append_row(["[16]기타 의료기관", "[17]미용/안경/보건위생", "[18]일반/휴게음식", "[19]제과/음료식품", "[20]기타"])
    print(table)

    #업종명 선택
    indu_nm = input("\nSelect(※입력시 반드시 숫자만 입력하세요!): ")
    if indu_nm != "": #사용자가 업종명 입력 시
        indu_nm = int(indu_nm)
        fr_list = select_industry.select_industry(fr_list, indu_nm)
    print_franchisee_list.print_franchisee_list(fr_list)
