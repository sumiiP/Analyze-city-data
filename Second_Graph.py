import csv
import matplotlib.pyplot as plt

#from google.colab import files
#upload = files.upload()

# 파일 불러오기, 변수 선언 #
x = []
y = []
z = []

f= open('RawData2.csv')
data = csv.reader(f)
next(data)
data = list(data)

# 데이터 추출 #
for i in range(4,21):          # y리스트에 도시를 담음(17개)
    y.append(data[i][0])

for i in range(1,10,2):        # z리스트에 연도를 담음(5개)
    z.append(data[1][i])

year = input('연도를 입력하세요 :')   # 연도를 입력받음
if year in z:                         # x리스트에 입력받은 연도에 따른 인구를 담음(17개)
    place = z.index(year)
    for i in range(4,21):
        x.append(data[i][place*2+1])
else :
    print('해당 연도는 자료에 존재하지 않습니다')

# 데이터 정리 # -> x리스트의 인구를 숫자형으로 변환함
Changed_x = ' '.join(k for k in x)         # 리스트를 문자열로 바꿈 (데이터 사이에 공백 추가)
Changed2_x = Changed_x.replace(',','')     # 문자열의 콤마 제거
x = list(map(int, Changed2_x.split(' ')))  # 문자열을 공백기준으로 분리함 -> 리스트 됨

# 그래프 그리기 #
plt.rc('font', family='NanumGothic')
plt.title("연도에 따른 도시별 인구분포", fontsize=15)
plt.pie(x,labels=y, autopct='%1.1f%%', radius=3.0, pctdistance=0.8, wedgeprops = {'width':1.5}, startangle=90, textprops = {'fontsize':15}, shadow=True, counterclock=False)
plt.legend(loc='upper right', shadow=True)
plt.show()