#현재 위치 기반 가맹점 리스트

def current_location_franchisee_list(fr_list, curr_loc):
    find_list=[]
    for i in fr_list:
        if i.refine_wgs84_lat.string is not None: #위경도 없는 가맹점 제외
            if curr_loc[0][0] <= float(i.refine_wgs84_lat.string) <= curr_loc[0][1]: #위도 범위 안의 가맹점
                if curr_loc[1][0] <= float(i.refine_wgs84_logt.string) <= curr_loc[1][1]: #경도 범위 안의 가맹점
                    find_list.append(i)
    return find_list
                
