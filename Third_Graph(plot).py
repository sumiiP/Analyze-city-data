import csv
import matplotlib.pyplot as plt

#from google.colab import files
#upload = files.upload()

# 파일 불러오기, 변수 선언 #
x = [] # 연도 5개
y = [] # 도시 17개 (전체 도시를 의미함)
place1 = [] # 첫번째 도시 인구밀도
place2 = [] # 두번째 도시 인구밀도

f= open('RawData2.csv') # 가지고 있는 data 파일명으로 변경 필요
data = csv.reader(f)
next(data)
data = list(data)

# 데이터 추출 #

for i in range(1,10,2):  # x 리스트에 연도를 담음(5개)
    x.append(int(data[1][i]))

for i in range(4,21):   # y 리스트에 도시를 담음(17개)
    y.append(data[i][0])

print('도시 리스트 : 서울, 부산, 대구, 인천, 광주, 대전, 울산, 세종, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주')

findPlace1 = input('첫번째 도시를 입력해주세요 :')  # 입력받은 도시의 연도별 인구밀도를 place1,place2 리스트에 담음(5개)
findPlace2 = input('두번째 도시를 입력해주세요 :')

if findPlace1 in y and findPlace2 in y :
    findChart1 = y.index(findPlace1)
    findChart2 = y.index(findPlace2)
    for i in range(2,11,2):
        place1.append(data[findChart1+4][i])
        place2.append(data[findChart2+4][i])
else :
    print('해당 도시는 자료에 존재하지 않습니다')

# 데이터 정리 #  -> place1, place2 리스트의 값 수정하기
Changed_1 = ' '.join(k for k in place1)         # 리스트를 문자열로 바꿈 (데이터 사이에 공백 추가)
Changed_2 = Changed_1.replace(',','')           # 문자열의 콤마 제거
place1 = list(map(int, Changed_2.split(' ')))   # 문자열을 공백기준으로 분리함 -> 리스트 됨

Changed_1 = ' '.join(k for k in place2)
Changed_2 = Changed_1.replace(',','')
place2 = list(map(int, Changed_2.split(' ')))

# 그래프 그리기 #
plt.rc('font', family='NanumGothic')
plt.title('도시 간의 인구밀도 비교', fontsize=15)
plt.xlabel('연도', fontsize=10)
plt.ylabel('인구밀도', fontsize=10)
plt.grid(True, axis='y', alpha=0.8, linestyle='--')
plt.plot(x, place1, label=findPlace1, color='r', marker = 'o', linestyle = 'solid')
plt.plot(x, place2, label=findPlace2, color='green', marker = 'o', linestyle = 'solid')
plt.gca().set_facecolor('#eeeeee')
plt.xticks(x)
plt.legend()
plt.show()
