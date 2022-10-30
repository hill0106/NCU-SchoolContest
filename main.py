from cmath import nan
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
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

totalData1 = []
totalData3 = []
totalData5 = []

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

def operateJobStr(): 
    dataset1["第一題"] = dataset1["第一題"].str.replace("(以接案維生，或個人服務，如幫忙排隊…)","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("(以接案維生或個人服務，例如撰稿人…)","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("\（請跳答第13題）","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("(請跳答第13題)","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("\（包括公立及私立大學、高中、高職、國中小…等）","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("(以接案維生，或個人服務，如幫忙排隊…)","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("\（請跳答第6題、第13題）","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("\（含職業軍人）","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("\（包括民營企業或國營企業…等）","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("\（請跳答第6題後，再跳答第13題）","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("部分工時_請問您1週工作時數約_小時","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("(建議以每週平均時數填報)*:*","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("部分工時_請問您1週工作時數約_小時*:*","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("\**","")
    dataset1["第一題"] = dataset1["第一題"].str.replace("\(\)","")

def classifyJob():
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
    dataset5["第四題"] = dataset5["第四題"].str.replace("專業 、科學及技術服務", "科學、技術、工程、數學類")
    dataset5["第四題"] = dataset5["第四題"].str.replace('出版、影音製作傳播及資通訊服務業', '個人及社會服務類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('製造業', '製造類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('金融及保險業', '金融財務類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('藝術、娛樂及休閒服務業', '休閒與觀光旅遊類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('運輸及倉儲業', '物流運輸類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('教育業', '教育與訓練類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('營建工程業', '建築營造類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('公共行政及國防、強制性社會安全', '政府公共事務類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('其他服務業', '個人及社會服務類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('電力及燃氣供應業', '天然資源、食品與農業類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('用水供應及污染整治業', '天然資源、食品與農業類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('支援服務業', '個人及社會服務類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('醫療保健及社會工作服務業', '醫療保健類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('批發及零售業', '行銷與銷售類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('住宿及餐飲業', '休閒與觀光旅遊類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('礦業 及土石採取', '天然資源、食品與農業類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('農、林漁牧業', '天然資源、食品與農業類')
    dataset5["第四題"] = dataset5["第四題"].str.replace('不動產業', '建築營造類')
    dataset1['第二題'] = dataset1['第二題'].str.replace('\*:*', '')
    dataset3['第二題'] = dataset3['第二題'].str.replace('\*:*', '')
    

def getData(s):
    data1 = []
    data3 = []
    data5 = []
    for k in dataset1['第二題'].dropna().unique():
        data1.append(job(workType = k, num = 0))
        for obj in data1:
            condition = np.logical_and(dataset1['leave_school_name'] == s, dataset1['第二題']== obj.workType) 
            obj.num = dataset1[condition].shape[0]

    for k in dataset3['第二題'].dropna().unique():
        data3.append(job(workType = k, num = 0))
        for obj in data3:
            condition = np.logical_and(dataset3['leave_school_name'] == s, dataset3['第二題']== obj.workType) 
            obj.num = dataset3[condition].shape[0]
    for k in dataset5['第四題'].dropna().unique():
        data5.append(job(workType = k, num = 0))
        for obj in data5:
            condition = np.logical_and(dataset5['leave_school_name'] == s, dataset5['第四題']== obj.workType) 
            obj.num = dataset5[condition].shape[0]
    return data1, data3, data5

def getTotalData():
    data1 = []
    data3 = []
    data5 = []

    for k in dataset1['第二題'].dropna().unique():
        data1.append(job(workType = k, num = 0))
    for k in dataset3['第二題'].dropna().unique():
        data3.append(job(workType = k, num = 0))
    for k in dataset5['第四題'].dropna().unique():
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
    for k in dataset1['第一題'].dropna().unique():
        data1.append(job(workType = k, num = 0))
        for obj in data1:
            condition = np.logical_and(dataset1['leave_school_name'] == s, dataset1['第一題']== obj.workType) 
            obj.num = dataset1[condition].shape[0]
    for k in dataset3['第一題'].dropna().unique():
        data3.append(job(workType = k, num = 0))
        for obj in data3:
            condition = np.logical_and(dataset3['leave_school_name'] == s, dataset3['第一題']== obj.workType) 
            obj.num = dataset3[condition].shape[0]
    for k in dataset5['第一題'].dropna().unique():
        data5.append(job(workType = k, num = 0))
        for obj in data5:
            condition = np.logical_and(dataset5['leave_school_name'] == s, dataset5['第一題']== obj.workType) 
            obj.num = dataset5[condition].shape[0]
    return data1, data3, data5

def getTotalInJobData():
    data1 = []
    data3 = []
    data5 = []
    for k in dataset1['第一題'].dropna().unique():
        data1.append(job(workType = k, num = 0))
        for obj in data1:
            obj.num = dataset1[dataset1['第一題']== obj.workType].shape[0]
    for k in dataset3['第一題'].dropna().unique():
        data3.append(job(workType = k, num = 0))
        for obj in data3:
            obj.num = dataset3[dataset3['第一題']== obj.workType].shape[0]
    for k in dataset5['第一題'].dropna().unique():
        data5.append(job(workType = k, num = 0))
        for obj in data5:
            obj.num = dataset5[dataset5['第一題']== obj.workType].shape[0]
    return data1, data3, data5

def getMajorData(s):
    data1 = []
    data3 = []
    data5 = []
    major1 = dataset1['leave_school_name']== s
    dd = dataset1[major1]
    majorNum1 = dd['leave_dept_name'].dropna().unique().shape[0]
    for j in dd['leave_dept_name'].dropna().unique():
        for k in dd['第二題'].dropna().unique():
            data1.append(majorJob(workType = k, num = 0, major=j))
    for obj in data1:
        condition = np.logical_and(dd['leave_dept_name'] == obj.major, dd['第二題']== obj.workType) 
        obj.num = dd[condition].shape[0]

    major3 = dataset3['leave_school_name']== s
    dd = dataset3[major3]
    majorNum3 = dd['leave_dept_name'].dropna().unique().shape[0]
    for j in dd['leave_dept_name'].dropna().unique():
        for k in dd['第二題'].dropna().unique():
            data3.append(majorJob(workType = k, num = 0, major=j))
    for obj in data3:
        condition = np.logical_and(dd['leave_dept_name'] == obj.major, dd['第二題']== obj.workType) 
        obj.num = dd[condition].shape[0]

    major5 = dataset5['leave_school_name']== s
    dd = dataset5[major5]
    majorNum5 = dd['leave_dept_name'].dropna().unique().shape[0]
    for j in dd['leave_dept_name'].dropna().unique():
        for k in dd['第四題'].dropna().unique():
            data5.append(majorJob(workType = k, num = 0, major=j))
    for obj in data5:
        condition = np.logical_and(dd['leave_dept_name'] == obj.major, dd['第四題']== obj.workType) 
        obj.num = dd[condition].shape[0]
    return data1, majorNum1, data3, majorNum3, data5, majorNum5

def plotTotal(s, data):
    filename = '全校資料/' +  '全校畢業後'+ str(s)+ '年就業.png'
    title = '全校畢業後' + str(s) +'年就職情況'
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
    plt.title(title, size=18)
    for a,b in zip(y,x):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum+10)
    # plt.show()
    fig.savefig(filename)

def plot1(s, data):
    title = str(s)
    filename = '各學院畢業就業/' + title + '.png'
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

def plot3(s, data):
    title = str(s)
    filename = '各學院三年就業/' + title + '.png'
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
    plt.title('畢業後三年\n'+title, size=18)
    for a,b in zip(y,x):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum+10)
    # plt.show()
    fig.savefig(filename)

def plot5(s, data):
    title = str(s)
    filename = '各學院五年就業/' + title + '.png'
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
    plt.title('畢業後五年\n'+title, size=18)
    for a,b in zip(y,x):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum+10)
    # plt.show()
    fig.savefig(filename)

def plotInJob(s, data, idx):
    title = '畢業後' + str(idx) + '年\n'+str(s)
    filename = '各學院就職情況/'+ str(s) + '/3類別＿'+ title + '.png'
    fulltime  = 0
    parttime = 0
    nojob = 0
    for obj in data:
        if(obj.workType.__contains__('全職工作')):
            fulltime+=(obj.num)
        elif(obj.workType.__contains__('部分工時')):
            parttime+=(obj.num)
        else:
            nojob+=(obj.num)
    
    fpnNum = [fulltime, parttime, nojob] #y
    FPN = ['全職工作', '部分工時', '目前非就業中 & 家管/料理家務者'] #x
    x = np.arange(len(FPN))
    y = np.array(fpnNum)
    cmap = cm.jet(np.linspace(0, 1, len(FPN)))
    fig = plt.figure(figsize=(10, 8))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    plt.rc('xtick', labelsize=12) 
    plt.bar(x, fpnNum, color=cmap)
    plt.xticks(x, FPN)
    plt.ylabel('人數', fontsize = 14)
    plt.xlabel('工作狀況', fontsize = 14)
    plt.title(title, fontsize = 18)
    for a,b in zip(x,y):
        plt.text(a, b+0.5, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)
    plt.ylim(0,max(fpnNum)+100)
    fig.savefig(filename)
    # plt.show()

def plotInJobTotal(idx, data):
    title = '全校畢業後' + str(idx) + '年\n就職狀況'
    filename = '全校資料/'+'/3類別＿'+ title + '.png'
    fulltime  = 0
    parttime = 0
    nojob = 0
    for obj in data:
        if(obj.workType.__contains__('全職工作')):
            fulltime+=(obj.num)
        elif(obj.workType.__contains__('部分工時')):
            parttime+=(obj.num)
        else:
            nojob+=(obj.num)
    
    fpnNum = [fulltime, parttime, nojob] #y
    FPN = ['全職工作', '部分工時', '目前非就業中 & 家管/料理家務者'] #x
    x = np.arange(len(FPN))
    y = np.array(fpnNum)
    cmap = cm.jet(np.linspace(0, 1, len(FPN)))
    fig = plt.figure(figsize=(10, 8))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    plt.rc('xtick', labelsize=12) 
    plt.bar(x, fpnNum, color=cmap)
    plt.xticks(x, FPN)
    plt.ylabel('人數', fontsize = 14)
    plt.xlabel('工作狀況', fontsize = 14)
    plt.title(title, fontsize = 18)
    for a,b in zip(x,y):
        plt.text(a, b+0.5, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)
    plt.ylim(0,max(fpnNum)+100)
    fig.savefig(filename)
    # plt.show()

def plotMajor1(s, data, idx):
    t = []
    n = []
    m = dataset1['leave_school_name']== s
    dd = dataset1[m]
    title = str(s) + ' ' + str(dd['leave_dept_name'].unique()[int(idx)])
    filename = '各系畢業就業/' + s + '/' +str(dd['leave_dept_name'].unique()[int(idx)])+'.png'
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

def plotMajor3(s, data, idx):
    t = []
    n = []
    m = dataset3['leave_school_name']== s
    dd = dataset3[m]
    title = str(s) + ' ' + str(dd['leave_dept_name'].unique()[int(idx)])
    filename = '各系三年就業/' + s + '/' +str(dd['leave_dept_name'].unique()[int(idx)])+'.png'
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
    plt.title('畢業後三年\n'+title, fontsize = 20)
    for a,b in zip(y,x):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum+10)
    # plt.show()
    fig.savefig(filename)

def plotMajor5(s, data, idx):
    t = []
    n = []
    m = dataset5['leave_school_name']== s
    dd = dataset5[m]
    title = str(s) + ' ' + str(dd['leave_dept_name'].unique()[int(idx)])
    filename = '各系五年就業/' + s + '/' +str(dd['leave_dept_name'].unique()[int(idx)])+'.png'
    for obj in data:
        if obj.major == dd['leave_dept_name'].unique()[idx]:
            n.append(obj.num)
    maxNum = max(n)
    for i in dd['第四題'].dropna().unique():
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
    plt.title('畢業後五年\n'+title, fontsize = 20)
    for a,b in zip(y,x):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum+10)
    # plt.show()
    fig.savefig(filename)


def plot135(s1, s2, data1, data3, data5):
    data1.sort(key=lambda x: str(x.workType), reverse=True)
    data3.sort(key=lambda x: str(x.workType), reverse=True)
    data5.sort(key=lambda x: str(x.workType), reverse=True)
    data135 = []

    for i in data1:
        strr = str(i.workType).split('*')[0]
        data135.append(college135(year=1, workType=strr, num=i.num))

    for i in data3:
        strr = str(i.workType).split('*')[0]
        data135.append(college135(year=3, workType=strr, num=i.num))

    for i in data5:
        strr = str(i.workType).split('(')[0]
        data135.append(college135(year=5, workType=strr, num=i.num))
    data135.append(college135(year=5, workType='資訊科技類', num=0))
    data135.append(college135(year=5, workType='藝文與影音傳播類', num=0))
    data135.append(college135(year=5, workType='司法、法律與公共安全類', num=0))
    data135.append(college135(year=5, workType='企業經營管理類', num=0)) 

    for i in data135:
        print(i.year, i.workType, i.num)

    
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
    print(len(data135))
    for i in data135:
        if i.workType == '金融財務類':
            y1.append(i.num)
        if i.workType == '醫療保健類':
            y2.append(i.num)
        if i.workType == '資訊科技類':
            y3.append(i.num)
        if i.workType == '製造類':
            y4.append(i.num)
        if i.workType == '行銷與銷售類':
            y5.append(i.num)
        if i.workType == '藝文與影音傳播類':
            y6.append(i.num)
        if i.workType == '科學、技術、工程、數學類':
            y7.append(i.num)
        if i.workType == '物流運輸類':
            y8.append(i.num)
        if i.workType == '教育與訓練類':
            y9.append(i.num)
        if i.workType == '政府公共事務類':
            y10.append(i.num)
        if i.workType == '建築營造類':
            y11.append(i.num)
        if i.workType == '天然資源、食品與農業類':
            y12.append(i.num)
        if i.workType == '司法、法律與公共安全類':
            y13.append(i.num)
        if i.workType == '個人及社會服務類':
            y14.append(i.num)
        if i.workType == '休閒與觀光旅遊類':
            y15.append(i.num)
        if i.workType == '企業經營管理類':
            y16.append(i.num)

    #plot start
    x = [1,3,5]
    cmap = cm.jet(np.linspace(0, 1, 16))
    fig = plt.figure(figsize=(15, 8))
    filename = str(s1) + '135年就業/' + str(s1) + str(s2) + '.png'
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False

    plt.subplot(4,4,1)
    plt.plot(x, y1, marker='o', markersize=5, color=cmap[0])
    for a, b in zip(x, y1):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y1)+2)
    plt.title('金融財務類', size=12, pad=15)

    plt.subplot(4,4,2)
    plt.plot(x, y2, marker='o', markersize=5, color=cmap[1])
    for a, b in zip(x, y2):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y2)+2)
    plt.title('醫療保健類', size=12, pad=15)

    plt.subplot(4,4,3)
    plt.plot(x, y3, marker='o', markersize=5, color=cmap[2])
    for a, b in zip(x, y3):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y3)+2)
    plt.title('資訊科技類', size=12, pad=15)

    plt.subplot(4,4,4)
    plt.plot(x, y4, marker='o', markersize=5, color=cmap[3])
    for a, b in zip(x, y4):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y4)+2)
    plt.title('製造類', size=12, pad=15)
   
    plt.subplot(4,4,5)   
    plt.plot(x, y5, marker='o', markersize=5, color=cmap[4])
    for a, b in zip(x, y5):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=12)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y5)+2)
    plt.title('行銷與銷售類', size=12, pad=15)

    plt.subplot(4,4,6)
    plt.plot(x, y6, marker='o', markersize=5, color=cmap[5])
    for a, b in zip(x, y6):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y6)+2)
    plt.title('藝文與影音傳播類', size=12, pad=15)

    plt.subplot(4,4,7)
    plt.plot(x, y7, marker='o', markersize=5, color=cmap[6])
    for a, b in zip(x, y7):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y7)+2)
    plt.title('科學、技術、工程、數學類', size=12, pad=15)

    plt.subplot(4,4,8)
    plt.plot(x, y8, marker='o', markersize=5, color=cmap[7])
    for a, b in zip(x, y8):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y8)+2)
    plt.title('物流運輸類', size=12, pad=15)

    plt.subplot(4,4,9)
    plt.plot(x, y9, marker='o', markersize=5, color=cmap[8])
    for a, b in zip(x, y9):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y9)+2)
    plt.title('教育與訓練類', size=12, pad=15)

    plt.subplot(4,4,10)
    plt.plot(x, y10, marker='o', markersize=5, color=cmap[9])
    for a, b in zip(x, y10):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y10)+2)
    plt.title('政府公共事務類', size=12, pad=15)

    plt.subplot(4,4,11)
    plt.plot(x, y11, marker='o', markersize=5, color=cmap[10])
    for a, b in zip(x, y11):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y11)+2)
    plt.title('建築營造類', size=12, pad=15)

    plt.subplot(4,4,12)
    plt.plot(x, y12, marker='o', markersize=5, color=cmap[11])
    for a, b in zip(x, y12):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y12)+2)
    plt.title('天然資源、食品與農業類', size=12, pad=15)

    plt.subplot(4,4,13)
    plt.plot(x, y13, marker='o', markersize=5, color=cmap[12])
    for a, b in zip(x, y13):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y13)+2)
    plt.title('司法、法律與公共安全類', size=12, pad=15)

    plt.subplot(4,4,14)
    plt.plot(x, y14, marker='o', markersize=5, color=cmap[13])
    for a, b in zip(x, y14):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y14)+2)
    plt.title('個人及社會服務類', size=12, pad=15)

    plt.subplot(4,4,15)
    plt.plot(x, y15, marker='o', markersize=5, color=cmap[14])
    for a, b in zip(x, y15):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y15)+2)
    plt.title('休閒與觀光旅遊類', size=12, pad=15)

    plt.subplot(4,4,16)
    plt.plot(x, y16, marker='o', markersize=5, color=cmap[15])
    for a, b in zip(x, y16):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    plt.xlabel('畢業後年份', size=10)
    plt.ylabel('就業人數', size=10)
    plt.xticks(range(1,6,2))
    plt.ylim(-0.5,max(y16)+2)
    plt.title('企業經營管理類', size=12, pad=15)

    fig.suptitle(str(s1)+str(s2)+"\n畢業後一、三、五年各產業就業人數", fontsize="x-large")
    plt.tight_layout()
    # plt.show()
    fig.savefig(filename)
       
        
def getGradMajorFig():
    biomedicineData1, majorN1, biomedicineData3, majorN3, biomedicineData5, majorN5 = getMajorData('生醫理工學院')
    for i in range(majorN1):
        plotMajor1('生醫理工學院', biomedicineData1, i)
    for i in range(majorN3):
        plotMajor3('生醫理工學院', biomedicineData3, i)
    for i in range(majorN5):
        plotMajor5('生醫理工學院', biomedicineData5, i)

    managementData1, majorN1, managementData3, majorN3, managementData5, majorN5 = getMajorData('管理學院')
    for i in range(majorN1):
        plotMajor1('管理學院', managementData1, i)
    for i in range(majorN3):
        plotMajor3('管理學院', managementData3, i)
    for i in range(majorN5):
        plotMajor5('管理學院', managementData5, i)

    eecsData1, majorN1, eecsData3, majorN3, eecsData5, majorN5 = getMajorData('資訊電機學院')
    for i in range(majorN1):
        plotMajor1('資訊電機學院', eecsData1, i)
    for i in range(majorN3):
        plotMajor3('資訊電機學院', eecsData3, i)
    for i in range(majorN5):
        plotMajor5('資訊電機學院', eecsData5, i)

    engineerData1, majorN1, engineerData3, majorN3, engineerData5, majorN5 = getMajorData('工學院')
    for i in range(majorN1):
        plotMajor1('工學院', engineerData1, i)
    for i in range(majorN3):
        plotMajor3('工學院', engineerData3, i)
    for i in range(majorN5):
        plotMajor5('工學院', engineerData5, i)

    liberalData1, majorN1, liberalData3, majorN3, liberalData5, majorN5 = getMajorData('文學院')
    for i in range(majorN1):
        plotMajor1('文學院', liberalData1, i)
    for i in range(majorN3):
        plotMajor3('文學院', liberalData3, i)
    for i in range(majorN5):
        plotMajor5('文學院', liberalData5, i)

    earthData1, majorN1, earthData3, majorN3, earthData5, majorN5 = getMajorData('地球科學學院')
    for i in range(majorN1):
        plotMajor1('地球科學學院', earthData1, i)
    for i in range(majorN3):
        plotMajor3('地球科學學院', earthData3, i)
    for i in range(majorN5):
        plotMajor5('地球科學學院', earthData5, i)
    
    scienceData1, majorN1, scienceData3, majorN3, scienceData5, majorN5 = getMajorData('理學院')
    for i in range(majorN1):
        plotMajor1('理學院', scienceData1, i)
    for i in range(majorN3):
        plotMajor3('理學院', scienceData3, i)
    for i in range(majorN5):
        plotMajor5('理學院', scienceData5, i)

    hakkaData1, majorN1, hakkaData3, majorN3, hakkaData5, majorN5 = getMajorData('客家學院')
    for i in range(majorN1):
        plotMajor1('客家學院', hakkaData1, i)
    for i in range(majorN3):
        plotMajor3('客家學院', hakkaData3, i)
    for i in range(majorN5):
        plotMajor5('客家學院', hakkaData5, i)

    spaceData1, majorN1, spaceData3, majorN3, spaceData5, majorN5 = getMajorData('太空及遙測研究中心')
    for i in range(majorN1):
        plotMajor1('太空及遙測研究中心', spaceData1, i)
    for i in range(majorN3):
        plotMajor3('太空及遙測研究中心', spaceData3, i)
    for i in range(majorN5):
        plotMajor5('太空及遙測研究中心', spaceData5, i)


def getGradCollegeFig():
    # biomedicineData1, biomedicineData3, biomedicineData5 = getData('生醫理工學院')
    # plot1('生醫理工學院', biomedicineData1)
    # plot3('生醫理工學院', biomedicineData3)
    # plot5('生醫理工學院', biomedicineData5)
    # plot135('各學院','生醫理工學院', biomedicineData1, biomedicineData3, biomedicineData5)
    biomedicineData1, biomedicineData3, biomedicineData5 = getCollegeInJobData('生醫理工學院')
    plotInJob('生醫理工學院', biomedicineData1, '一')
    plotInJob('生醫理工學院', biomedicineData3, '三')
    plotInJob('生醫理工學院', biomedicineData5, '五')


    # managementData1, managementData3, managementData5 = getData('管理學院')
    # plot1('管理學院', managementData1)
    # plot3('管理學院', managementData3)
    # plot5('管理學院', managementData5)
    # plot135('各學院','管理學院', managementData1, managementData3, managementData5)
    managementData1, managementData3, managementData5 = getCollegeInJobData('管理學院')
    plotInJob('管理學院', managementData1, '一')
    plotInJob('管理學院', managementData3, '三')
    plotInJob('管理學院', managementData5, '五')

    # eecsData1, eecsData3, eecsData5 = getData('資訊電機學院')
    # plot1('資訊電機學院', eecsData1)
    # plot3('資訊電機學院', eecsData3)
    # plot5('資訊電機學院', eecsData5)
    # plot135('各學院','資訊電機學院', eecsData1, eecsData3, eecsData5)
    eecsData1, eecsData3, eecsData5 = getCollegeInJobData('資訊電機學院')
    plotInJob('資訊電機學院', eecsData1, '一')
    plotInJob('資訊電機學院', eecsData3, '三')
    plotInJob('資訊電機學院', eecsData5, '五')

    # engineerData1, engineerData3, engineerData5 = getData('工學院')
    # plot1('工學院', engineerData1)
    # plot3('工學院', engineerData3)
    # plot5('工學院', engineerData5)
    # plot135('各學院','工學院', engineerData1, engineerData3, engineerData5)
    engineerData1, engineerData3, engineerData5 = getCollegeInJobData('工學院')
    plotInJob('工學院', engineerData1, '一')
    plotInJob('工學院', engineerData3, '三')
    plotInJob('工學院', engineerData5, '五')

    # liberalData1, liberalData3, liberalData5 = getData('文學院')
    # plot1('文學院', liberalData1)
    # plot3('文學院', liberalData3)
    # plot5('文學院', liberalData5)
    # plot135('各學院','文學院', liberalData1, liberalData3, liberalData5)
    liberalData1, liberalData3, liberalData5 = getCollegeInJobData('文學院')
    plotInJob('文學院', liberalData1, '一')
    plotInJob('文學院', liberalData3, '三')
    plotInJob('文學院', liberalData5, '五')

    # earthData1, earthData3, earthData5 = getData('地球科學學院')
    # plot1('地球科學學院', earthData1)
    # plot3('地球科學學院', earthData3)
    # plot5('地球科學學院', earthData5)
    # plot135('各學院','地球科學學院', earthData1, earthData3, earthData5)
    earthData1, earthData3, earthData5 = getCollegeInJobData('地球科學學院')
    plotInJob('地球科學學院', earthData1, '一')
    plotInJob('地球科學學院', earthData3, '三')
    plotInJob('地球科學學院', earthData5, '五')

    # scienceData1, scienceData3, scienceData5 = getData('理學院')
    # plot1('理學院', scienceData1)
    # plot3('理學院', scienceData3)
    # plot5('理學院', scienceData5)
    # plot135('各學院','理學院', scienceData1, scienceData3, scienceData5)
    scienceData1, scienceData3, scienceData5 = getCollegeInJobData('理學院')
    plotInJob('理學院', scienceData1, '一')
    plotInJob('理學院', scienceData3, '三')
    plotInJob('理學院', scienceData5, '五')

    # hakkaData1, hakkaData3, hakkaData5 = getData('客家學院')
    # plot1('客家學院', hakkaData1)
    # plot3('客家學院', hakkaData3)
    # plot5('客家學院', hakkaData5)
    # plot135('各學院','客家學院', hakkaData1, hakkaData3, hakkaData5)
    hakkaData1, hakkaData3, hakkaData5 = getCollegeInJobData('客家學院')
    plotInJob('客家學院', hakkaData1, '一')
    plotInJob('客家學院', hakkaData3, '三')
    plotInJob('客家學院', hakkaData5, '五')

    # spaceData1, spaceData3, spaceData5 = getData('太空及遙測研究中心')
    # plot1('太空及遙測研究中心', spaceData1)
    # plot3('太空及遙測研究中心', spaceData3)
    # plot5('太空及遙測研究中心', spaceData5)
    # plot135('各學院','太空及遙測研究中心', spaceData1, spaceData3, spaceData5)
    spaceData1, spaceData3, spaceData5 = getCollegeInJobData('太空及遙測研究中心')
    plotInJob('太空及遙測研究中心', spaceData1, '一')
    plotInJob('太空及遙測研究中心', spaceData3, '三')
    plotInJob('太空及遙測研究中心', spaceData5, '五')

    # print(biomedicineData1)

def getTotalFig():
    # totalData1, totalData3, totalData5= getTotalData()
    # plotTotal('一', totalData1)
    # plotTotal('三', totalData3)
    # plotTotal('五', totalData5)
    # plot135('全校','', totalData1, totalData3, totalData5)
    totalData1, totalData3, totalData5= getTotalInJobData()
    plotInJobTotal('一', totalData1)
    plotInJobTotal('三', totalData3)
    plotInJobTotal('五', totalData5)

if __name__ == "__main__":
    # operateJobStr()

    classifyJob()
    
    # operateJobStr()

    # getGradMajorFig()

    # getGradCollegeFig()

    getTotalFig()

    
