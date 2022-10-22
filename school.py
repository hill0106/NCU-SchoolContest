import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib import cm


dataset = pd.read_csv('./dataset/first.csv')
biomedicineData = []
managementData = []
eecsData = []
engineerData = []
liberalData = []
earthData = []
scienceData = []
hakkaData = []
spaceData = []

# print(dataset['leave_school_name'].unique())
# print(dataset['leave_dept_name'].unique())

def operateJobStr(): 
    dataset["第一題"] = dataset["第一題"].str.replace("(以接案維生，或個人服務，如幫忙排隊…)","")
    dataset["第一題"] = dataset["第一題"].str.replace("(以接案維生或個人服務，例如撰稿人…)","")
    dataset["第一題"] = dataset["第一題"].str.replace("\（請跳答第13題）","")
    dataset["第一題"] = dataset["第一題"].str.replace("(請跳答第13題)","")
    dataset["第一題"] = dataset["第一題"].str.replace("\（包括公立及私立大學、高中、高職、國中小…等）","")
    dataset["第一題"] = dataset["第一題"].str.replace("(以接案維生，或個人服務，如幫忙排隊…)","")
    dataset["第一題"] = dataset["第一題"].str.replace("\（請跳答第6題、第13題）","")
    dataset["第一題"] = dataset["第一題"].str.replace("\（含職業軍人）","")
    dataset["第一題"] = dataset["第一題"].str.replace("\（包括民營企業或國營企業…等）","")
    dataset["第一題"] = dataset["第一題"].str.replace("\（請跳答第6題後，再跳答第13題）","")
    dataset["第一題"] = dataset["第一題"].str.replace("部分工時_請問您1週工作時數約_小時","")
    dataset["第一題"] = dataset["第一題"].str.replace("(建議以每週平均時數填報)*:*","")
    dataset["第一題"] = dataset["第一題"].str.replace("部分工時_請問您1週工作時數約_小時*:*","")
    dataset["第一題"] = dataset["第一題"].str.replace("\**","")
    dataset["第一題"] = dataset["第一題"].str.replace("\(\)","")


class job: 
    def __init__(self, workType, num): 
        self.workType = workType 
        self.num = num

class majorJob: 
    def __init__(self, workType, num, major): 
        self.major = major
        self.workType = workType 
        self.num = num

def getData(s):
    data = []
    for k in dataset['第二題'].unique():
        data.append(job(workType = k, num = 0))
        for obj in data:
            condition = np.logical_and(dataset['leave_school_name'] == s, dataset['第二題']== obj.workType) 
            obj.num = dataset[condition].size
    return data

def getInJobData(s):
    data = []
    for k in dataset['第一題'].unique():
        data.append(job(workType = k, num = 0))
        for obj in data:
            condition = np.logical_and(dataset['leave_school_name'] == s, dataset['第一題']== obj.workType) 
            obj.num = dataset[condition].size
    return data

def getMajorData(s):
    data = []
    major = dataset['leave_school_name']== s
    dd = dataset[major]
    majorNum = dd['leave_dept_name'].unique().size
    for j in dd['leave_dept_name'].unique():
        for k in dd['第二題'].unique():
            data.append(majorJob(workType = k, num = 0, major=j))
    for obj in data:
        condition = np.logical_and(dd['leave_dept_name'] == obj.major, dd['第二題']== obj.workType) 
        obj.num = dd[condition].size
    return data, majorNum

def getMajorInJobData(s):
    data = []
    major = dataset['leave_school_name']== s
    dd = dataset[major]
    majorNum = dd['leave_dept_name'].unique().size
    for j in dd['leave_dept_name'].unique():
        for k in dd['第一題'].unique():
            data.append(majorJob(workType = k, num = 0, major=j))
    for obj in data:
        condition = np.logical_and(dd['leave_dept_name'] == obj.major, dd['第一題']== obj.workType) 
        obj.num = dd[condition].size
    return data, majorNum

def plot(s, data):
    title = str(s)
    t = []
    n = []
    for obj in data:
        n.append(obj.num)
    maxNum = max(n)
    for i in dataset['第二題'].unique():
        strr = str(i).split('*')[0]
        if(len(strr)>10):
            s1 = ""
            for s in range(len(strr)):
                if s != 7:
                    s1 += strr[s]
                else:
                    s1 += (strr[s]+'\n')
            t.append(s1)
        else:
            t.append(str(i).split('*')[0])
    n.remove(0)
    t.remove('nan')
    x = np.arange(len(t))
    y = np.array(n)
    cmap = cm.jet(np.linspace(0, 1, len(t)))
    fig = plt.figure(figsize=(15, 8))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    plt.rc('ytick', labelsize=8) 
    plt.barh(x, n, color=cmap)
    plt.yticks(x, t)
    plt.ylabel('工作類型')
    plt.xlabel('就業人數')
    plt.title(title)
    for a,b in zip(y,x):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=10)
    plt.xlim(0,maxNum+500)
    plt.show()

def plotInJob(s, data):
    title = str(s)
    filename1 = '/Users/alex87/Documents/AI導論/competition/各學院就職情況' + '各類別＿'+ title + '.png'
    filename2 = '/Users/alex87/Documents/AI導論/competition/各學院就職情況' + '3類別＿'+ title + '.png'
    t = []
    n = []
    fulltime  = 0
    parttime = 0
    nojob = 0
    for obj in data:
        n.append(obj.num)
        if(obj.workType.__contains__('全職工作')):
            fulltime+=(obj.num)
        elif(obj.workType.__contains__('部分工時')):
            parttime+=(obj.num)
        else:
            nojob+=(obj.num)
    print(fulltime)
    print(parttime)
    print(nojob)
    # '''plot all job type'''
    maxNum = max(n)
    for i in dataset['第一題'].unique():
        strr = str(i).split('(')[0]
        if(len(strr)>10):
            s1 = ""
            for s in range(len(strr)):
                if s != 7:
                    s1 += strr[s]
                else:
                    s1 += (strr[s]+'\n')
            t.append(s1)
        else:
            t.append(str(i).split('(')[0])
    x = np.arange(len(t))
    y = np.array(n)
    cmap = cm.jet(np.linspace(0, 1, len(t)))
    fig = plt.figure(figsize=(15, 8))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    plt.rc('xtick', labelsize=12) 
    plt.barh(x, n, color=cmap)
    plt.yticks(x, t)
    plt.ylabel('工作狀況', fontsize = 14)
    plt.xlabel('人數', fontsize = 14)
    plt.title(title, fontsize = 18)
    for a,b in zip(y,x):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum+500)
    fig.savefig(filename1)
    # plt.show()
    
    '''plot partime, fulltime, nojob'''
    fpnNum = [fulltime, parttime, nojob] #y
    FPN = ['全職工作', '部分工時', '目前非就業中 & 家管/料理家務者'] #x
    x = np.arange(len(FPN))
    y = np.array(fpnNum)
    cmap = cm.jet(np.linspace(0, 1, len(FPN)))
    fig1 = plt.figure(figsize=(10, 8))
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
    plt.ylim(0,max(fpnNum)+500)
    fig1.savefig(filename2)
    # plt.show()

def plotMajor(s, data, idx):
    t = []
    n = []
    m = dataset['leave_school_name']== s
    dd = dataset[m]
    title = str(s) + ' ' + str(dd['leave_dept_name'].unique()[int(idx)])
    filename = '/Users/alex87/Documents/AI導論/competition/各系畢業就業/'+str(dd['leave_dept_name'].unique()[int(idx)])+'.png'
    for obj in data:
        if obj.major == dd['leave_dept_name'].unique()[idx]:
            n.append(obj.num)
    maxNum = max(n)
    for i in dd['第二題'].unique():
        strr = str(i).split('*')[0]
        if(len(strr)>10):
            s1 = ""
            for s in range(len(strr)):
                if s != 7:
                    s1 += strr[s]
                else:
                    s1 += (strr[s]+'\n')
            t.append(s1)
        else:
            t.append(str(i).split('*')[0])
    n.remove(0)
    t.remove('nan')
    x = np.arange(len(t))
    y = np.array(n)
    cmap = cm.jet(np.linspace(0, 1, len(t)))
    fig = plt.figure(figsize=(15, 8))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    plt.rc('ytick', labelsize=12) 
    plt.barh(x, n, color=cmap)
    plt.yticks(x, t)
    plt.ylabel('工作類型', fontsize = 14)
    plt.xlabel('就業人數', fontsize = 14)
    plt.title(title, fontsize = 18)
    for a,b in zip(y,x):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum+500)
    # plt.show()
    fig.savefig(filename)

def plotMajorInJob(s, data, idx):
    t = []
    n = []
    m = dataset['leave_school_name']== s
    dd = dataset[m]
    title = str(s) + ' ' + str(dd['leave_dept_name'].unique()[int(idx)])
    filename1 = '/Users/alex87/Documents/AI導論/competition/各系就職情況/'+'各類別'+str(dd['leave_dept_name'].unique()[int(idx)])+'.png'
    filename2 = '/Users/alex87/Documents/AI導論/competition/各系就職情況/'+'3類別'+str(dd['leave_dept_name'].unique()[int(idx)])+'.png'
    fulltime  = 0
    parttime = 0
    nojob = 0
        
    for obj in data:
        if obj.major == dd['leave_dept_name'].unique()[idx]:
            n.append(obj.num)
            if(obj.workType.__contains__('全職工作')):
                fulltime+=(obj.num)
            elif(obj.workType.__contains__('部分工時')):
                parttime+=(obj.num)
            else:
                nojob+=(obj.num)
    maxNum = max(n)
    # print(sorted(list(dd['第一題'].unique())))
    for i in dd['第一題'].unique():
        strr = str(i).split('*')[0]
        if(len(strr)>10):
            s1 = ""
            for s in range(len(strr)):
                if s != 7:
                    s1 += strr[s]
                else:
                    s1 += (strr[s]+'\n')
            t.append(s1)
        else:
            t.append(str(i).split('*')[0])

    # plot all
    x = np.arange(len(t))
    y = np.array(n)
    cmap = cm.jet(np.linspace(0, 1, len(t)))
    fig = plt.figure(figsize=(15, 8))
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    plt.rc('ytick', labelsize=11) 
    plt.barh(x, n, color=cmap)
    plt.yticks(x, t)
    plt.ylabel('工作狀況', fontsize = 14)
    plt.xlabel('人數', fontsize = 14)
    plt.title(title, fontsize = 18)
    for a,b in zip(y,x):
        plt.text(a, b, '%.0f' % a, ha='left', va= 'center',fontsize=12)
    plt.xlim(0,maxNum+500)
    # plt.show()
    fig.savefig(filename1)

    #plot three types
    fpnNum = [fulltime, parttime, nojob] #y
    FPN = ['全職工作', '部分工時', '目前非就業中 & 家管/料理家務者'] #x
    x = np.arange(len(FPN))
    y = np.array(fpnNum)
    cmap = cm.jet(np.linspace(0, 1, len(FPN)))
    fig1 = plt.figure(figsize=(10, 8))
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
    plt.ylim(0,max(fpnNum)+500)
    # plt.show()
    fig1.savefig(filename2)


def getFig():
    # biomedicineData, majorN = getMajorInJobData('生醫理工學院')
    # managementData, majorN = getMajorInJobData('管理學院')
    # eecsData, majorN = getMajorInJobData('資訊電機學院')
    # engineerData, majorN = getMajorInJobData('工學院')
    # liberalData, majorN = getMajorInJobData('文學院')
    # earthData, majorN = getMajorInJobData('地球科學學院')
    # scienceData, majorN = getMajorInJobData('理學院')
    # hakkaData, majorN = getMajorInJobData('客家學院')
    spaceData, majorN = getMajorInJobData('太空及遙測研究中心')

    for i in range(majorN):
        plotMajorInJob('太空及遙測研究中心', spaceData, i)


if __name__ == "__main__":
    operateJobStr()
    # getFig()
    # biomedicineData = getInJobData('生醫理工學院')
    # managementData = getInJobData('管理學院')
    # eecsData = getInJobData('資訊電機學院')
    # engineerData = getInJobData('工學院')
    # liberalData = getInJobData('文學院')
    # earthData = getInJobData('地球科學學院')
    # scienceData = getInJobData('理學院')
    # hakkaData = getInJobData('客家學院')
    spaceData = getInJobData('太空及遙測研究中心')

    # plotInJob('生醫理工學院', biomedicineData)
    # plotInJob('管理學院', managementData)
    # plotInJob('資訊電機學院', eecsData)
    # plotInJob('工學院', engineerData)
    # plotInJob('文學院', liberalData)
    # plotInJob('地球科學學院', earthData)
    # plotInJob('理學院', scienceData)
    # plotInJob('客家學院', hakkaData)
    plotInJob('太空及遙測研究中心', spaceData)
