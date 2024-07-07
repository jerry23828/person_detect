import requests
import base64
import cv2 as cv


# opencv 图片
def personattr_detect(img):

    global gender, age, smoke
    request_url1 = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num"
    request_url2 = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image": base64_image}
    access_token = '24.078cda99151d3b02a7a3a409ffde500c.2592000.1722754125.282335-90561887'
    request_url1 = request_url1 + "?access_token=" + access_token
    request_url2 = request_url2 + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response1 = requests.post(request_url1, data=params, headers=headers)
    response2 = requests.post(request_url2, data=params, headers=headers)
    num = 0
    if response1 and response2:
        data1 = response1.json()
        data2 = response2.json()
        num = data1['person_num']
        for item in data2['person_info']:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            cv.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            gender = item['attributes']['gender']['name']
            age = item['attributes']['age']['name']
            facemask = item['attributes']['face_mask']['name']
            smoke = item['attributes']['smoke']['name']
            bag = item['attributes']['bag']['name']
            vehicle = item['attributes']['vehicle']['name']
            cellphone = item['attributes']['cellphone']['name']
            with open('data/RecordOut.txt', 'a') as file:
                file.write(f"Person : Gender {gender},Age {age}, Facemask {facemask}, Smoke {smoke},Bag {bag}, Vehicle {vehicle}, Cellphone {cellphone} \n")
    return img, num, gender, age, smoke, facemask

