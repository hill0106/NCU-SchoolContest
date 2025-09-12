import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


dataset1 = pd.read_csv('./dataset/first.csv')
biomedicineData1 = []
managementData1 = []
eecsData1 = []
engineerData1 = []
liberalData1 = []
earthData1 = []
scienceData1 = []
hakkaData1 = []
spaceData1 = []
# print(dataset1.shape[0])

dataset3 = pd.read_csv('./dataset/third.csv')
biomedicineData3 = []
managementData3 = []
eecsData3 = []
engineerData3 = []
liberalData3 = []
earthData3 = []
scienceData3 = []
hakkaData3 = []
spaceData3 = []
# print(dataset3.shape[0])

dataset5 = pd.read_csv('./dataset/fifth.csv')
biomedicineData5 = []
managementData5 = []
eecsData5 = []
engineerData5 = []
liberalData5 = []
earthData5 = []
scienceData5 = []
hakkaData5 = []
spaceData5 = []
# print(dataset5.shape[0])

totalData1 = []
totalData3 = []
totalData5 = []

path = 'output.txt'
f = open(path, 'w')

class job: 
    def __init__(self, workType, num): 
        self.workType = workType 
        self.num = num

class majorJob: 
    def __init__(self, workType, num, major): 
        self.major = major
        self.workType = workType 
        self.num = num

class college135: 
    def __init__(self, year, workType, num): 
        self.year = year
        self.workType = workType 
        self.num = num

def operateJobStr(d): 
    d["第一題"] = d["第一題"].str.replace("(以接案維生，或個人服務，如幫忙排隊…)","")
    d["第一題"] = d["第一題"].str.replace("(以接案維生或個人服務，例如撰稿人…)","")
    d["第一題"] = d["第一題"].str.replace("\（請跳答第13題）","")
    d["第一題"] = d["第一題"].str.replace("(請跳答第13題)","")
    d["第一題"] = d["第一題"].str.replace("\（包括公立及私立大學、高中、高職、國中小…等）","")
    d["第一題"] = d["第一題"].str.replace("(以接案維生，或個人服務，如幫忙排隊…)","")
    d["第一題"] = d["第一題"].str.replace("\（請跳答第6題、第13題）","")
    d["第一題"] = d["第一題"].str.replace("\（含職業軍人）","")
    d["第一題"] = d["第一題"].str.replace("\（包括民營企業或國營企業…等）","")
    d["第一題"] = d["第一題"].str.replace("\（請跳答第6題後，再跳答第13題）","")
    d["第一題"] = d["第一題"].str.replace("部分工時_請問您1週工作時數約_小時","")
    d["第一題"] = d["第一題"].str.replace("(建議以每週平均時數填報)*:*","") 
    d["第一題"] = d["第一題"].str.replace("\（請跳答第6題後，再跳答第14題）","")
    d["第一題"] = d["第一題"].str.replace("\（請跳答第14題）","")
    d["第一題"] = d["第一題"].str.replace("部分工時_請問您1週工作時數約_小時*:*","")
    d["第一題"] = d["第一題"].str.replace("請問您1週工作時數約_____小時","")
    d["第一題"] = d["第一題"].str.replace("\（請跳答第10、11、12題）","")
    d["第一題"] = d["第一題"].str.replace("\（請跳答第7題後，再跳答第10、11、12題）","")
    d["第一題"] = d["第一題"].str.replace("\**","")
    d["第一題"] = d["第一題"].str.replace("\(\)","")
    return d

def classifyJob(d):
    dataset5["第四題"] = dataset5["第四題"].str.replace("(", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(")", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace("\*:*", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace("B", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace("M", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" A", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" C", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" D", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" E", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" F", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" G", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" H", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" I", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" J", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" K", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" L", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" M", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" N", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" O", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" P", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" Q", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" R", "")
    dataset5["第四題"] = dataset5["第四題"].str.replace(" S", "")

    d['第二題'] = d['第二題'].str.replace('\*:*', '')
    d['第二題'] = d['第二題'].str.replace('\*:*', '') 
    d['第二題'] = d['第二題'].str.replace('資訊科技類', '出版、影音製作傳播及資通訊服務業')
    d['第二題'] = d['第二題'].str.replace('製造類', '製造業')
    d['第二題'] = d['第二題'].str.replace('金融財務類', '金融及保險業')
    d['第二題'] = d['第二題'].str.replace('科學、技術、工程、數學類', '專業 、科學及技術服務')
    d['第二題'] = d['第二題'].str.replace('企業經營管理類', '專業 、科學及技術服務')
    d['第二題'] = d['第二題'].str.replace('醫療保健類', '醫療保健及社會工作服務業')
    d['第二題'] = d['第二題'].str.replace('建築營造類', '營建工程業')
    d['第二題'] = d['第二題'].str.replace('藝文與影音傳播類', '出版、影音製作傳播及資通訊服務業') 
    d['第二題'] = d['第二題'].str.replace('教育與訓練類', '教育業')
    d['第二題'] = d['第二題'].str.replace('物流運輸類', '運輸及倉儲業')
    d['第二題'] = d['第二題'].str.replace('行銷與銷售類', '專業 、科學及技術服務')
    d['第二題'] = d['第二題'].str.replace('休閒與觀光旅遊類', '藝術、娛樂及休閒服務業')
    d['第二題'] = d['第二題'].str.replace('司法、法律與公共安全類', '專業 、科學及技術服務')
    d['第二題'] = d['第二題'].str.replace('個人及社會服務類', '醫療保健及社會工作服務業')
    d['第二題'] = d['第二題'].str.replace('政府公共事務類', '公共行政及國防、強制性社會安全')
    d['第二題'] = d['第二題'].str.replace('天然資源、食品與農業類', '農、林漁牧業')

    return d
    

def getCollegeWorkTypeData(s):
    data1 = []
    data3 = []
    data5 = []
    for k in dataset1['第二題'].unique():
        if(type(k)== str):
            data1.append(job(workType = k, num = 0))
        for obj in data1:
            condition = np.logical_and(dataset1['leave_school_name'] == s, dataset1['第二題']== obj.workType) 
            obj.num = dataset1[condition].shape[0]

    for k in dataset3['第二題'].unique():
        if(type(k)== str):
            data3.append(job(workType = k, num = 0))
        for obj in data3:
            condition = np.logical_and(dataset3['leave_school_name'] == s, dataset3['第二題']== obj.workType) 
            obj.num = dataset3[condition].shape[0]
    for k in dataset5['第四題'].unique():
        if(type(k)== str):
            data5.append(job(workType = k, num = 0))
        for obj in data5:
            condition = np.logical_and(dataset5['leave_school_name'] == s, dataset5['第四題']== obj.workType) 
            obj.num = dataset5[condition].shape[0]
    return data1, data3, data5

def getTotalWorkTypeData():
    data1 = []
    data3 = []
    data5 = []

    for k in dataset1['第二題'].unique():
        if(type(k)== str):
            data1.append(job(workType = k, num = 0))
    for k in dataset3['第二題'].unique():
        if(type(k)== str):
            data3.append(job(workType = k, num = 0))
    for k in dataset5['第四題'].unique():
        if(type(k)== str):
            data5.append(job(workType = k, num = 0))
    for obj in data1:
        obj.num = dataset1[dataset1['第二題']== obj.workType].shape[0]
    for obj in data3:
        obj.num = dataset3[dataset3['第二題']== obj.workType].shape[0]
    for obj in data5:
        obj.num = dataset5[dataset5['第四題']== obj.workType].shape[0]
    
    return data1, data3, data5

def getCollegeInJobData(s):
    data1 = []
    data3 = []
    data5 = []
    for k in dataset1['第一題'].unique():
        if(type(k)== str):
            data1.append(job(workType = k, num = 0))
        for obj in data1:
            condition = np.logical_and(dataset1['leave_school_name'] == s, dataset1['第一題']== obj.workType) 
            obj.num = dataset1[condition].shape[0]
    for k in dataset3['第一題'].unique():
        if(type(k)== str):
            data3.append(job(workType = k, num = 0))
        for obj in data3:
            condition = np.logical_and(dataset3['leave_school_name'] == s, dataset3['第一題']== obj.workType) 
            obj.num = dataset3[condition].shape[0]
    for k in dataset5['第一題'].unique():
        if(type(k)== str):
            data5.append(job(workType = k, num = 0))
        for obj in data5:
            condition = np.logical_and(dataset5['leave_school_name'] == s, dataset5['第一題']== obj.workType) 
            obj.num = dataset5[condition].shape[0]
    return data1, data3, data5

def getTotalInJobData():
    data1 = []
    data3 = []
    data5 = []
    for k in dataset1['第一題'].unique():
        if(type(k)== str):
            data1.append(job(workType = k, num = 0))
        for obj in data1:
            obj.num = dataset1[dataset1['第一題']== obj.workType].shape[0]
    for k in dataset3['第一題'].unique():
        if(type(k)== str):
            data3.append(job(workType = k, num = 0))
        for obj in data3:
            obj.num = dataset3[dataset3['第一題']== obj.workType].shape[0]
    for k in dataset5['第一題'].unique():
        if(type(k)== str):
            data5.append(job(workType = k, num = 0))
        for obj in data5:
            obj.num = dataset5[dataset5['第一題']== obj.workType].shape[0]
    return data1, data3, data5

def getMajorWorkTypeData(s):
    data1 = []
    major1 = dataset1['leave_school_name']== s
    dd = dataset1[major1]
    majorNum1 = dd['leave_dept_name'].unique().shape[0]
    for j in dd['leave_dept_name'].unique():
        for k in dd['第二題'].unique():
            if(type(k)== str):
                data1.append(majorJob(workType = k, num = 0, major=j))
    for obj in data1:
        condition = np.logical_and(dd['leave_dept_name'] == obj.major, dd['第二題']== obj.workType) 
        obj.num = dd[condition].shape[0]
    
    return data1, majorNum1

def plotWorkTypeTotal(s, data1, data3, data5):
    title = str(s)
    if(str(s)=='全校'):
        filename = 'university_135_year_employment_by_industry/university_135_year_employment_by_industry.png'
    else:
        filename = 'colleges_135_year_employment_by_industry/' + str(s) + '135年就業類別.png'
    t1 = []
    n1 = []
    t3 = []
    n3 = []
    t5 = []
    n5 = []
    for obj in data1:
        strr = str(obj.workType)
        if(len(strr)>10):
            s1 = ""
            for s in range(len(strr)):
                if s != 11:
                    s1 += strr[s]
                else:
                    s1 += (strr[s]+'\n')
            t1.append(s1)
        else:
            t1.append(strr)
        n1.append(obj.num)
    for obj in data3:
        strr = str(obj.workType)
        if(len(strr)>10):
            s1 = ""
            for s in range(len(strr)):
                if s != 11:
                    s1 += strr[s]
                else:
                    s1 += (strr[s]+'\n')
            t3.append(s1)
        else:
            t3.append(strr)
        n3.append(obj.num)
    for obj in data5:
        strr = str(obj.workType)
        # if(len(strr)>10):
        #     s1 = ""
        #     for s in range(len(strr)):
        #         if s != 11:
        #             s1 += strr[s]
        #         else:
        #             s1 += (strr[s]+'\n')
        #     t5.append(s1)
        # else:
        t5.append(strr)
        n5.append(obj.num)
    maxNum1 = max(n1)
    x1 = np.arange(len(t1))
    y1 = np.array(n1)
    maxNum3 = max(n3)
    x3 = np.arange(len(t3))
    y3 = np.array(n3)
    maxNum5 = max(n5)
    x5 = np.arange(len(t5))
    y5 = np.array(n5)

    cmap = cm.jet(np.linspace(0, 1, len(t1)))
    fig = plt.figure(figsize=(18, 8))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    
    plt.subplot(1,3,1)
    plt.barh(x1, n1, color=cmap)
    plt.yticks(x1, t1)
    plt.tick_params(axis='y', which='major', labelsize=14)
    plt.ylabel('工作類型', size=14, color='#004c99')
    plt.xlabel('就業人數', size=14, color='#004c99')
    plt.title('畢業後一年', size=18)
    for a,b in zip(y1,x1):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum1+500)

    plt.subplot(1,3,2)
    plt.barh(x3, n3, color=cmap)
    plt.yticks(x3, t3)
    plt.tick_params(axis='y', which='major', labelsize=14)
    plt.ylabel('工作類型', size=14, color='#004c99')
    plt.xlabel('就業人數', size=14, color='#004c99')
    plt.title('畢業後三年', size=18)
    for a,b in zip(y3,x3):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum3+500)

    plt.subplot(1,3,3)
    plt.barh(x5, n5, color=cmap) 
    plt.yticks(x5, t5)
    plt.tick_params(axis='y', which='major', labelsize=14)
    plt.ylabel('工作類型', size=14, color='#004c99')
    plt.xlabel('就業人數', size=14, color='#004c99')
    plt.title('畢業後五年', size=18)
    for a,b in zip(y5,x5):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum5+500)
    fig.suptitle(title, fontsize=20)
    plt.tight_layout()
    
    # plt.show()
    fig.savefig(filename)

def plotWorkType(s, data):
    title = str(s)
    filename = 'colleges_graduation_employment/' + title + '.png'
    t = []
    n = []
    for obj in data:
        strr = str(obj.workType)
        if(len(strr)>10):
            s1 = ""
            for s in range(len(strr)):
                if s != 7:
                    s1 += strr[s]
                else:
                    s1 += (strr[s]+'\n')
            t.append(s1)
        else:
            t.append(strr)
        n.append(obj.num)
    maxNum = max(n)
    x = np.arange(len(t))
    y = np.array(n)
    cmap = cm.jet(np.linspace(0, 1, len(t)))
    fig = plt.figure(figsize=(15, 8))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    plt.rc('ytick', labelsize=12) 
    plt.barh(x, n, color=cmap)
    plt.yticks(x, t)
    plt.ylabel('工作類型', size=14, color='#004c99')
    plt.xlabel('就業人數', size=14, color='#004c99')
    plt.title('畢業後一年\n'+title, size=18)
    for a,b in zip(y,x):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum+10)
    # plt.show()
    fig.savefig(filename)


def plotInJobTotal(s, data1, data3, data5):
    if str(s) == '全校':
        title = '全校畢業後一、三、五年就職狀況'
        filename = 'university_employment_status'+'/employment_status_categories.png'
    else:
        title = str(s) + '畢業後一、三、五年就職狀況'
        filename = 'colleges_employment_status'+'/'+str(s)+'_3類別.png'
    fulltime1  = 0
    parttime1 = 0
    nojob1 = 0
    fulltime3  = 0
    parttime3 = 0
    nojob3 = 0
    fulltime5  = 0
    parttime5 = 0
    nojob5 = 0
    for obj in data1:
        if(obj.workType.__contains__('全職工作')):
            fulltime1+=(obj.num)
        elif(obj.workType.__contains__('目前非就業中') or obj.workType.__contains__('家管/料理家務者')):
            nojob1+=(obj.num)
        else:
            parttime1+=(obj.num)
    for obj in data3:
        if(obj.workType.__contains__('全職工作')):
            fulltime3+=(obj.num)
        elif(obj.workType.__contains__('目前非就業中') or obj.workType.__contains__('家管/料理家務者')):
            nojob3+=(obj.num)
        else:
            parttime3+=(obj.num)
    for obj in data5:
        if(obj.workType.__contains__('全職工作')):
            fulltime5+=(obj.num)
        elif(obj.workType.__contains__('目前非就業中') or obj.workType.__contains__('家管/料理家務者')):
            nojob5+=(obj.num)
        else:
            parttime5+=(obj.num)
    
    fpnNum1 = [fulltime1, parttime1, nojob1] #y
    fpnNum3 = [fulltime3, parttime3, nojob3]
    fpnNum5 = [fulltime5, parttime5, nojob5]
    FPN = ['全職工作', '部分工時', '目前非就業中'] #x
    x = np.arange(len(FPN))
    y1 = np.array(fpnNum1)
    y3 = np.array(fpnNum3)
    y5 = np.array(fpnNum5)
    cmap = cm.jet(np.linspace(0, 1, 3))
    fig = plt.figure(figsize=(10, 8))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False

    plt.subplot(1,3,1)
    plt.bar(x, fpnNum1, color=cmap)
    plt.xticks(x, FPN)
    plt.ylabel('人數', fontsize = 12)
    plt.xlabel('工作狀況', fontsize = 12)
    plt.title('畢業後一年', fontsize = 14, pad=15)
    for a,b in zip(x,y1):
        plt.text(a, b+0.5, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)
    plt.ylim(0,max(fpnNum1)+100)

    plt.subplot(1,3,2)
    plt.bar(x, fpnNum3, color=cmap)
    plt.xticks(x, FPN)
    plt.ylabel('人數', fontsize = 12)
    plt.xlabel('工作狀況', fontsize = 12)
    plt.title('畢業後三年', fontsize = 14, pad=15)
    for a,b in zip(x,y3):
        plt.text(a, b+0.5, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)
    plt.ylim(0,max(fpnNum3)+100)

    plt.subplot(1,3,3)
    plt.bar(x, fpnNum5, color=cmap)
    plt.xticks(x, FPN)
    plt.ylabel('人數', fontsize = 12)
    plt.xlabel('工作狀況', fontsize = 12)
    plt.title('畢業後五年', fontsize = 14, pad=15)
    for a,b in zip(x,y5):
        plt.text(a, b+0.5, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)
    plt.ylim(0,max(fpnNum5)+100)
    fig.suptitle(title, fontsize=20)
    plt.tight_layout()

    fig.savefig(filename)
    # plt.show()

def plotMajorWorkType(s, data, idx):
    t = []
    n = []
    m = dataset1['leave_school_name']== s
    dd = dataset1[m]
    title = str(s) + ' ' + str(dd['leave_dept_name'].unique()[int(idx)])
    filename = 'departments_graduation_employment/' + s + '/' +str(dd['leave_dept_name'].unique()[int(idx)])+'.png'
    for obj in data:
        if obj.major == dd['leave_dept_name'].unique()[idx]:
            n.append(obj.num)
    maxNum = max(n)
    for i in dd['第二題'].dropna().unique():
        strr = str(i)
        if(len(strr)>8):
            s1 = ""
            for s in range(len(strr)):
                if s != 7:
                    s1 += strr[s]
                else:
                    s1 += (strr[s]+'\n')
            t.append(s1)
        else:
            t.append(strr)
    x = np.arange(len(t))
    y = np.array(n)
    cmap = cm.jet(np.linspace(0, 1, len(t)))
    fig = plt.figure(figsize=(15, 8))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    plt.rc('ytick', labelsize=12) 
    plt.barh(x, n, color=cmap)
    plt.yticks(x, t)
    plt.ylabel('工作類型', size=14, color='#004c99')
    plt.xlabel('就業人數', size=14, color='#004c99')
    plt.title('畢業後一年\n'+title, fontsize = 20)
    for a,b in zip(y,x):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum+10)
    # plt.show()
    fig.savefig(filename)


def plot135YearWorkType(s1, s2, data1, data3, data5):
    data1.sort(key=lambda x: str(x.workType), reverse=True)
    data3.sort(key=lambda x: str(x.workType), reverse=True)
    data5.sort(key=lambda x: str(x.workType), reverse=True)
    data135 = []

    for i in data1:
        strr = str(i.workType)
        data135.append(college135(year=1, workType=strr, num=round(i.num/dataset1.shape[0] * 100, 2)))

    for i in data3:
        strr = str(i.workType)
        data135.append(college135(year=3, workType=strr, num=round(i.num/dataset3.shape[0] * 100, 2)))

    for i in data5:
        strr = str(i.workType)
        data135.append(college135(year=5, workType=strr, num=round(i.num/dataset5.shape[0] * 100, 2)))

    data135.append(college135(year=1, workType='其他服務業', num=0))
    data135.append(college135(year=1, workType='電力及燃氣供應業', num=0))
    data135.append(college135(year=1, workType='用水供應及污染整治業', num=0))
    data135.append(college135(year=1, workType='支援服務業', num=0))
    data135.append(college135(year=1, workType='批發及零售業', num=0))
    data135.append(college135(year=1, workType='住宿及餐飲業', num=0))
    data135.append(college135(year=1, workType='礦業 及土石採取', num=0))
    data135.append(college135(year=1, workType='不動產業', num=0)) 
    data135.append(college135(year=3, workType='其他服務業', num=0))
    data135.append(college135(year=3, workType='電力及燃氣供應業', num=0))
    data135.append(college135(year=3, workType='用水供應及污染整治業', num=0))
    data135.append(college135(year=3, workType='支援服務業', num=0))
    data135.append(college135(year=3, workType='批發及零售業', num=0))
    data135.append(college135(year=3, workType='住宿及餐飲業', num=0))
    data135.append(college135(year=3, workType='礦業 及土石採取', num=0))
    data135.append(college135(year=3, workType='不動產業', num=0)) 

    data135.sort(key=lambda x: str(x.year), reverse=False)

    # for i in data135:
    #     print(i.year, i.workType, i.num)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    y8 = []
    y9 = []
    y10 = []
    y11 = []
    y12 = []
    y13 = []
    y14 = []
    y15 = []
    y16 = []
    y17 = []
    y18 = []
    y19 = []
    # print(len(data135))
    for i in data135:
        if i.workType == '電力及燃氣供應業':
            y1.append(i.num)
        if i.workType == '金融及保險業':
            y2.append(i.num)
        if i.workType == '醫療保健及社會工作服務業':
            y3.append(i.num)
        if i.workType == '運輸及倉儲業':
            y4.append(i.num)
        if i.workType == '農、林漁牧業':
            y5.append(i.num)
        if i.workType == '製造業':
            y6.append(i.num)
        if i.workType == '藝術、娛樂及休閒服務業':
            y7.append(i.num)
        if i.workType == '礦業 及土石採取':
            y8.append(i.num)
        if i.workType == '用水供應及污染整治業':
            y9.append(i.num)
        if i.workType == '營建工程業':
            y10.append(i.num)
        if i.workType == '教育業':
            y11.append(i.num)
        if i.workType == '支援服務業':
            y12.append(i.num)
        if i.workType == '批發及零售業':
            y13.append(i.num)
        if i.workType == '專業 、科學及技術服務':
            y14.append(i.num)
        if i.workType == '出版、影音製作傳播及資通訊服務業':
            y15.append(i.num)
        if i.workType == '其他服務業':
            y16.append(i.num)
        if i.workType == '公共行政及國防、強制性社會安全':
            y17.append(i.num) 
        if i.workType == '住宿及餐飲業':
            y18.append(i.num)
        if i.workType == '不動產業':
            y19.append(i.num) 

    #plot start
    x = [1,3,5]
    cmap = cm.jet(np.linspace(0, 1, 19))
    fig = plt.figure(figsize=(15, 8))
    if(str(s1)=='全校'):
        filename = 'university_135_year_employment_by_industry/' + str(s1) + '135年就業情況.png'
    else:
        filename = 'colleges_135_year_employment_by_industry/' + str(s2) + '135年就業情況.png'
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False

    plt.subplot(5,4,1)
    plt.plot(x, y1, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y1):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y1)+2)
    plt.title('電力及燃氣供應業', size=12, pad=15)

    plt.subplot(5,4,2)
    plt.plot(x, y2, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y2):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y2)+2)
    plt.title('金融及保險業', size=12, pad=15)

    plt.subplot(5,4,3)
    plt.plot(x, y3, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y3):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.yticks(range(0,int(max(y3)+2),2))
    plt.title('醫療保健及社會工作服務業', size=12, pad=15)

    plt.subplot(5,4,4)
    plt.plot(x, y4, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y4):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y4)+2)
    plt.title('運輸及倉儲業', size=12, pad=15)
   
    plt.subplot(5,4,5)   
    plt.plot(x, y5, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y5):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=12)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y5)+2)
    plt.title('農、林漁牧業', size=12, pad=15)

    plt.subplot(5,4,6)
    plt.plot(x, y6, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y6):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y6)+2)
    plt.title('製造業', size=12, pad=15)

    plt.subplot(5,4,7)
    plt.plot(x, y7, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y7):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y7)+2)
    plt.title('藝術、娛樂及休閒服務業', size=12, pad=15)

    plt.subplot(5,4,8)
    plt.plot(x, y8, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y8):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y8)+2)
    plt.title('礦業 及土石採取', size=12, pad=15)

    plt.subplot(5,4,9)
    plt.plot(x, y9, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y9):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y9)+2)
    plt.title('用水供應及污染整治業', size=12, pad=15)

    plt.subplot(5,4,10)
    plt.plot(x, y10, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y10):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y10)+2)
    plt.title('營建工程業', size=12, pad=15)

    plt.subplot(5,4,11)
    plt.plot(x, y11, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y11):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y11)+2)
    plt.title('教育業', size=12, pad=15)

    plt.subplot(5,4,12)
    plt.plot(x, y12, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y12):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y12)+2)
    plt.title('支援服務業', size=12, pad=15)

    plt.subplot(5,4,13)
    plt.plot(x, y13, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y13):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y13)+2)
    plt.title('批發及零售業', size=12, pad=15)

    plt.subplot(5,4,14)
    plt.plot(x, y14, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y14):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y14)+2)
    plt.title('專業 、科學及技術服務', size=12, pad=15)

    plt.subplot(5,4,15)
    plt.plot(x, y15, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y15):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y15)+2)
    plt.title('出版、影音製作傳播及資通訊服務業', size=12, pad=15)

    plt.subplot(5,4,16)
    plt.plot(x, y16, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y16):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y16)+2)
    plt.title('其他服務業', size=12, pad=15)

    plt.subplot(5,4,17)
    plt.plot(x, y17, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y17):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y17)+2)
    plt.title('公共行政及國防、強制性社會安全', size=12, pad=15)

    plt.subplot(5,4,18)
    plt.plot(x, y18, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y18):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y18)+2)
    plt.title('住宿及餐飲業', size=12, pad=15)

    plt.subplot(5,4,19)
    plt.plot(x, y19, marker='o', markersize=5, color=cmap[18])
    for a, b in zip(x, y19):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份(年)', size=10)
    plt.ylabel('就業百分比(%)', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y19)+2)
    plt.title('不動產業', size=12, pad=15)

       
    if(str(s1)=='全校'):
        fig.suptitle(str(s1)+str(s2)+"\n畢業後一、三、五年各產業就業百分比", fontsize="x-large")
    else:
        fig.suptitle(str(s2)+"\n畢業後一、三、五年各產業就業百分比", fontsize="x-large")
    plt.tight_layout()
    fig.align_ylabels()
    # plt.show()
    fig.savefig(filename)
       
        
def getGradMajorFig():
    biomedicineData1, majorN1 = getMajorWorkTypeData('生醫理工學院')
    for i in range(majorN1):
        plotMajorWorkType('生醫理工學院', biomedicineData1, i)
    

    managementData1, majorN1= getMajorWorkTypeData('管理學院')
    for i in range(majorN1):
        plotMajorWorkType('管理學院', managementData1, i)

    eecsData1, majorN1 = getMajorWorkTypeData('資訊電機學院')
    for i in range(majorN1):
        plotMajorWorkType('資訊電機學院', eecsData1, i)
   

    engineerData1, majorN1 = getMajorWorkTypeData('工學院')
    for i in range(majorN1):
        plotMajorWorkType('工學院', engineerData1, i)
    

    liberalData1, majorN1 = getMajorWorkTypeData('文學院')
    for i in range(majorN1):
        plotMajorWorkType('文學院', liberalData1, i)
   

    earthData1, majorN1 = getMajorWorkTypeData('地球科學學院')
    for i in range(majorN1):
        plotMajorWorkType('地球科學學院', earthData1, i)
    
    
    scienceData1, majorN1 = getMajorWorkTypeData('理學院')
    for i in range(majorN1):
        plotMajorWorkType('理學院', scienceData1, i)
   
    hakkaData1, majorN1 = getMajorWorkTypeData('客家學院')
    for i in range(majorN1):
        plotMajorWorkType('客家學院', hakkaData1, i)
    

    spaceData1, majorN1 = getMajorWorkTypeData('太空及遙測研究中心')
    for i in range(majorN1):
        plotMajorWorkType('太空及遙測研究中心', spaceData1, i)
    
def printWorkTypeData(s, d1, d2, d3):
    print(s, "畢業後一年各產業就業人數：", file=f)
    for i in d1:
        print(i.workType, i.num, file=f)
    print('------------------------------------------------------', file=f)
    print(s, "畢業後三年各產業就業人數：", file=f)
    for i in d2:
        print(i.workType, i.num, file=f)
    print('------------------------------------------------------', file=f)
    print(s, "畢業後五年各產業就業人數：", file=f)
    for i in d3:
        print(i.workType, i.num, file=f)

def printInJobData(s, d1, d2, d3):
    print(s, "畢業後一年就業情況：", file=f)
    for i in d1:
        print(i.workType, i.num, file=f)
    print('------------------------------------------------------', file=f)
    print(s, "畢業後三年就業情況：", file=f)
    for i in d2:
        print(i.workType, i.num, file=f)
    print('------------------------------------------------------', file=f)
    print(s, "畢業後五年就業情況：", file=f)
    for i in d3:
        print(i.workType, i.num, file=f)
    

def getGradCollegeFig():
    biomedicineData1, biomedicineData3, biomedicineData5 = getCollegeWorkTypeData('生醫理工學院')
    plot135YearWorkType('各學院', '生醫理工學院', biomedicineData1, biomedicineData3, biomedicineData5)
    plotWorkType('生醫理工學院', biomedicineData1)
    printWorkTypeData('生醫理工學院', biomedicineData1, biomedicineData3, biomedicineData5)
    print('------------------------------------------------------', file=f)
    biomedicineData1, biomedicineData3, biomedicineData5 = getCollegeInJobData('生醫理工學院')
    plotInJobTotal('生醫理工學院', biomedicineData1, biomedicineData3, biomedicineData5)
    printInJobData('生醫理工學院', biomedicineData1, biomedicineData3, biomedicineData5)
    print('------------------------------------------------------', file=f)

    managementData1, managementData3, managementData5 = getCollegeWorkTypeData('管理學院')
    plot135YearWorkType('各學院', '管理學院', managementData1, managementData3, managementData5)
    plotWorkType('管理學院', managementData1)
    printWorkTypeData('管理學院', managementData1, managementData3, managementData5)
    print('------------------------------------------------------', file=f)
    managementData1, managementData3, managementData5 = getCollegeInJobData('管理學院')
    plotInJobTotal('管理學院', managementData1, managementData3, managementData5)
    printInJobData('管理學院', managementData1, managementData3, managementData5)
    print('------------------------------------------------------', file=f)

    eecsData1, eecsData3, eecsData5 = getCollegeWorkTypeData('資訊電機學院')
    plot135YearWorkType('各學院', '資訊電機學院', eecsData1, eecsData3, eecsData5)
    plotWorkType('資訊電機學院', eecsData1)
    printWorkTypeData('資訊電機學院', eecsData1, eecsData3, eecsData5)
    print('------------------------------------------------------', file=f)
    eecsData1, eecsData3, eecsData5 = getCollegeInJobData('資訊電機學院')
    plotInJobTotal('資訊電機學院', eecsData1, eecsData3, eecsData5)
    printInJobData('資訊電機學院', eecsData1, eecsData3, eecsData5)
    print('------------------------------------------------------', file=f)

    engineerData1, engineerData3, engineerData5 = getCollegeWorkTypeData('工學院')
    plot135YearWorkType('各學院', '工學院', engineerData1, engineerData3, engineerData5)
    plotWorkType('工學院', engineerData1)
    printWorkTypeData('工學院', engineerData1, engineerData3, engineerData5)
    print('------------------------------------------------------', file=f)
    engineerData1, engineerData3, engineerData5 = getCollegeInJobData('工學院')
    plotInJobTotal('工學院', engineerData1, engineerData3, engineerData5)
    printInJobData('工學院', engineerData1, engineerData3, engineerData5)
    print('------------------------------------------------------', file=f)

    liberalData1, liberalData3, liberalData5 = getCollegeWorkTypeData('文學院')
    plot135YearWorkType('各學院', '文學院', liberalData1, liberalData3, liberalData5)
    plotWorkType('文學院', liberalData1)
    printWorkTypeData('文學院', liberalData1, liberalData3, liberalData5)
    print('------------------------------------------------------', file=f)
    liberalData1, liberalData3, liberalData5 = getCollegeInJobData('文學院')
    plotInJobTotal('文學院', liberalData1, liberalData3, liberalData5)
    printInJobData('文學院', liberalData1, liberalData3, liberalData5)
    print('------------------------------------------------------', file=f)

    earthData1, earthData3, earthData5 = getCollegeWorkTypeData('地球科學學院')
    plot135YearWorkType('各學院', '地球科學學院', earthData1, earthData3, earthData5)
    plotWorkType('地球科學學院', earthData1)
    printWorkTypeData('地球科學學院', earthData1, earthData3, earthData5)
    print('------------------------------------------------------', file=f)
    earthData1, earthData3, earthData5 = getCollegeInJobData('地球科學學院')
    plotInJobTotal('地球科學學院', earthData1, earthData3, earthData5)
    printInJobData('地球科學學院', earthData1, earthData3, earthData5)
    print('------------------------------------------------------', file=f)

    scienceData1, scienceData3, scienceData5 = getCollegeWorkTypeData('理學院')
    plot135YearWorkType('各學院', '理學院', scienceData1, scienceData3, scienceData5)
    plotWorkType('理學院', scienceData1)
    printWorkTypeData('理學院', scienceData1, scienceData3, scienceData5)
    print('------------------------------------------------------', file=f)
    scienceData1, scienceData3, scienceData5 = getCollegeInJobData('理學院')
    plotInJobTotal('理學院', scienceData1, scienceData3, scienceData5)
    printInJobData('理學院', scienceData1, scienceData3, scienceData5)
    print('------------------------------------------------------', file=f)

    hakkaData1, hakkaData3, hakkaData5 = getCollegeWorkTypeData('客家學院')
    plot135YearWorkType('各學院', '客家學院', hakkaData1, hakkaData3, hakkaData5)
    plotWorkType('客家學院', hakkaData1)
    printWorkTypeData('客家學院', hakkaData1, hakkaData3, hakkaData5)
    print('------------------------------------------------------', file=f)
    hakkaData1, hakkaData3, hakkaData5 = getCollegeInJobData('客家學院')
    plotInJobTotal('客家學院', hakkaData1, hakkaData3, hakkaData5)
    printInJobData('客家學院', hakkaData1, hakkaData3, hakkaData5)
    print('------------------------------------------------------', file=f)

    spaceData1, spaceData3, spaceData5 = getCollegeWorkTypeData('太空及遙測研究中心')
    plot135YearWorkType('各學院', '太空及遙測研究中心', spaceData1, spaceData3, spaceData5)
    plotWorkType('太空及遙測研究中心', spaceData1)
    printWorkTypeData('太空及遙測研究中心', spaceData1, spaceData3, spaceData5)
    print('------------------------------------------------------', file=f)
    spaceData1, spaceData3, spaceData5 = getCollegeInJobData('太空及遙測研究中心')
    plotInJobTotal('太空及遙測研究中心', spaceData1, spaceData3, spaceData5)
    printInJobData('太空及遙測研究中心', spaceData1, spaceData3, spaceData5)


def getTotalFig():
    totalData1, totalData3, totalData5= getTotalWorkTypeData()
    plot135YearWorkType('全校', '',totalData1, totalData3, totalData5)
    plotWorkTypeTotal('全校',totalData1, totalData3, totalData5)
    print('------------------------------------------------------', file=f)
    printWorkTypeData('全校', totalData1, totalData3, totalData5)
    totalData1, totalData3, totalData5= getTotalInJobData()
    plotInJobTotal('全校', totalData1, totalData3, totalData5)
    print('------------------------------------------------------', file=f)
    printInJobData('全校', totalData1, totalData3, totalData5)



if __name__ == "__main__":
    dataset1 = operateJobStr(dataset1)
    dataset3 = operateJobStr(dataset3)
    dataset5 = operateJobStr(dataset5)
    # print(dataset1['第一題'].unique())
    # print('畢業後一、三年產業類別')
    # for i in dataset1['第二題'].unique():
    #     if(type(i)==str):
    #         print(i)
    dataset1 = classifyJob(dataset1)
    dataset3 = classifyJob(dataset3)
    getGradMajorFig()
    getGradCollegeFig()
    getTotalFig()
    
