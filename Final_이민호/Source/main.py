"""Start Page
가맹점 리스트 출력 / 가맹점 검색 선택
"""
import select_print_franchisee
import select_search_franchisee

userInput = ""

while userInput != "0":
    userInput = input("\nMenu: \n[1] 가맹점 리스트 출력 \n[2] 가맹점 검색 \n[0] 종료 \n\nSelect: ")
    
    if userInput == "1":
        #가맹점 리스트 출력
        select_print_franchisee.select_pr_fr()

    elif userInput == "2":
        #가맹점 검색
        select_search_franchisee.search_fr()

    elif userInput == "0":
        #프로그램 종료
        print("\n프로그램을 종료합니다.")

    else:
        print("\n잘못된 입력입니다!")

