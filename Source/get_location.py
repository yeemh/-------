#현재 위치 범위 받아오기

import requests

def get_current_location():
    LOCATION_API_KEY = 'AIzaSyBkHAyQsn6hP1a1zOQZ-JapCPcAvJE-VzY'

    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={LOCATION_API_KEY}'

    data = {
        'considerIp': True,
        }

    result = requests.post(url, data).json()

    lat = result['location']['lat'] #위도
    lng = result['location']['lng'] #경도
    accuracy = result['accuracy'] #정확도->원의 반지름 크기(단위:m)

    #범위 계산
    lat_range = calculate_latitude_accuracy(lat, accuracy)
    lng_range = calculate_longitude_accuracy(lng, accuracy)
    
    location = [lat_range, lng_range]
    return location

#위도 오차범위
def calculate_latitude_accuracy(lat, acc):
    #위도 1도는 111km
    acc = acc / 111000
    grid_range = [lat - acc, lat + acc]
    return grid_range

#경도 오차범위
def calculate_longitude_accuracy(lng, acc):
    #경도 1도는 약 89km
    acc = acc / 89000
    grid_range = [lng - acc, lng + acc]
    return grid_range
