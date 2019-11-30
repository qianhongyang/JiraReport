from functools import reduce
from JiraReport.GetJiraData import GetJiraData
from JiraReport.ReadConfig import readconfig
from JiraReport.BinPicture import draw
from JiraReport.SendMail import SendMali

#tips：改进
#1，增加界面
#2，增加多项目统计
#3，增加多人邮件


class client:

    def __init__(self):
        self.jurl = readconfig(option="JURL")
        self.juser = readconfig(option="JUSER")
        self.jpasswd = readconfig(option="JPASSWD")
        self.jproject = readconfig(option="JPROJECT")
        self.jversions = readconfig(option="JVERSION").split(",")
        self.myjira = GetJiraData(self.jurl, self.juser, self.jpasswd)
        self.myjira.ExistProject(self.jproject)

    #获取bug总数
    @staticmethod
    def total(dict):
        """传入：字典
           返回：字符串
        """
        return sum(dict.values())


    #两个字典相同的key相加
    @staticmethod
    def add_dict(dict_a, dict_b):
        """传入：字典
           返回：字典
        """
        for k, v in dict_b.items():
            dict_a[k] = dict_a.get(k, 0) + v
        return dict_a

    #把得出的字典放入列表中等待处理
    def chuli(self,doname):
        """传入：函数名"""
        dict_li = []

        for i in self.jversions:
            func = getattr(self.myjira, doname)
            dic = func(self.jproject, i)
            dict_li.append(dic)

        return reduce(self.add_dict,dict_li)



if __name__ == '__main__':
    Do = client()

    bug_types = Do.chuli("get_bugtypes")
    bug_assignes = Do.chuli("get_assignes")
    bug_components = Do.chuli("get_components")

    draw("Bug类型", bug_types)
    draw("经办人", bug_assignes)
    draw("模块类型", bug_components)

    Send = SendMali()
    Send.main(Do.total(bug_types))