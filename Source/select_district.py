#구 선택

def select_district(fr_list, district):
    find_list=[]

    for i in fr_list:
        adrr = i.refine_lotno_addr.string #주소 받아오기
        adrr = adrr.split(' ')[2] #구만 추출
        if adrr == district:
            find_list.append(i)
    return find_list
