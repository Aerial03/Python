import urllib.request

# 다운로드 할 이미지 경로
url = "https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"

# 저장할 파일 경로 및 이름
imgName = "C://Users/효준/Desktop/google.png"

# 파일 다운로드
# urlretrieve(URL, imgName)
urllib.request.urlretrieve(url, imgName)

print('저장 완료')