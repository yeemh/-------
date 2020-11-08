#상호명 검색

def find_franchisee(fr_list,cmp_nm):
    find_list=[]
    for i in fr_list:
        name = i.cmpnm_nm.string #상호명 받아오기
        if cmp_nm in name:
            find_list.append(i)
    return find_list
