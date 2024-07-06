import requests
import base64
import cv2 as cv


# opencv 图片
def personattr_detect(img):

    request_url1 = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num"
    request_url2 = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
    print('url')
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image": base64_image}
    access_token = '24.078cda99151d3b02a7a3a409ffde500c.2592000.1722754125.282335-90561887'
    request_url1 = request_url1 + "?access_token=" + access_token
    request_url2 = request_url2 + "?access_token=" + access_token
    print('request')
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response1 = requests.post(request_url1, data=params, headers=headers)
    response2 = requests.post(request_url2, data=params, headers=headers)
    num = 0
    No = 1
    if response1 and response2:
        print('response12')
        data1 = response1.json()
        data2 = response2.json()
        num = data1['person_num']
        print(num)
        for item in data2['person_info']:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            cv.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            print('rectangle')
            gender = item['attributes']['gender']
            print('gender')
            age = item['attributes']['age']
            print('age')
            facemask = item['attributes']['face_mask']
            print('facemask')
            smoke = item['attributes']['smoke']
            print('smoke')
            bag = item['attributes']['bag']
            print('bag')
            vehicle = item['attributes']['vehicle']
            print('vehicle')
            cellphone = item['attributes']['cellphone']
            print("all")
            with open('data/RecordOut.txt', 'a') as file:
                file.write(f"Person {No}: Gender {gender},Age {age}, Facemask {facemask}, Smoke {smoke},Bag {bag}, Vehicle {vehicle}, Cellphone {cellphone} \n")
            No += 1
        # 定义要绘制的文字
        #     text = item['type']
        #     print('type')
        #     position = (x1, y1-2)
        #     print('position')
        #     font = cv.FONT_HERSHEY_SIMPLEX
        #     font_scale = 1
        #     print('font')
        #     color = (0, 0, 255)  # 红色
        #     thickness = 2
        #     print('thickness')
        #     img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
        #     print('img')
            # cv.imshow('Rectangle', img)
    return img, num
    # return num
    print('response')
    # # 等待按键，然后关闭窗口
    # cv.waitKey(0)
    # cv.destroyAllWindows()
