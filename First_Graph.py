import csv
import matplotlib.pyplot as plt
import random

#from google.colab import files
#upload = files.upload()

# 파일 불러오기, 변수 선언 #
x = []
y = []

f= open('RawData2.csv')
data = csv.reader(f)
next(data)
data = list(data)

# 데이터 추출 #

for i in range(1,10,2):  # x 리스트에 연도를 담음(5개)
    x.append(int(data[1][i]))

for i in range(4,21):   # y 리스트에 도시를 담음(17개)
    y.append(data[i][0])

while (1000):
    print('도시 리스트 : 서울, 부산, 대구, 인천, 광주, 대전, 울산, 세종, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주')
    print('※프로그램을 끝내려면 "끝"을 입력하세요※')
    z = []
    findPlace = input('도시명을 입력해주세요 :')   # 입력받은 도시의 연도별 인구를 z 리스트에 담음(5개)

    if findPlace in y :
        findChart = y.index(findPlace)
        for i in range(1,10,2):
            z.append(data[findChart+4][i])

    elif findPlace == '끝' :
        print('분석을 종료하겠습니다')

    else :
        print('해당 도시는 자료에 존재하지 않습니다')
        print('다시 도시명을 입력해주세요')
        continue

    # 데이터 정리 #  -> z리스트의 값 수정하기
    Changed_z = ' '.join(k for k in z)         # 리스트를 문자열로 바꿈 (데이터 사이에 공백 추가)
    Changed2_z = Changed_z.replace(',','')     # 문자열의 콤마 제거
    z = list(map(int, Changed2_z.split(' ')))  # 문자열을 공백기준으로 분리함 -> 리스트 됨

    # 그래프 색깔 랜덤지정 #
    choice_color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]

    # 그래프 그리기 #
    plt.rc('font', family='NanumGothic')
    plt.title('도시별 인구증가 그래프', fontsize=15)
    plt.bar(x,z, color=choice_color, label='단위: 천명, 명/㎢')
    plt.legend(loc='upper right')
    plt.xlabel('연도', fontsize=10)
    plt.ylabel('인구', fontsize=10)
    plt.gca().set_facecolor('#eeeeee')
    plt.grid(True, axis='y', alpha=0.8, linestyle='--')
    plt.ylim(min(z)-100, max(z)+100)
    plt.show()