# 가맹점 검색
import get_franchisee_list
import get_location
import find_cur_location_franchisee
import find_franchisee_name
import print_franchisee_list

def search_fr():
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

    #현재 위치 범위 받아오기
    loc = get_location.get_current_location()

    #현재 위치 기반 가맹점 리스트 받아오기
    fr_list = find_cur_location_franchisee.current_location_franchisee_list(fr_list, loc)

    #상호명 입력
    cmp_nm = input("\n\n상호명(※입력 없을 시 모두 출력): ")
    #일치하는 가맹점 찾기
    fr_list = find_franchisee_name.find_franchisee(fr_list, cmp_nm)
    print_franchisee_list.print_franchisee_list(fr_list)
