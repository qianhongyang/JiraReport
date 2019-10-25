from functools import reduce
from CtrolJira.GetJiraData import readconfig,GetJiraData
from CtrolJira.BinPicture import draw
from CtrolJira.SendMail import SendMali


def total():
    total=[]
    for i in bugdic:
        total.append(i[1])
    return reduce(lambda x, y: x+y, total)

jurl = readconfig(option="JURL")
juser = readconfig(option="JUSER")
jpasswd = readconfig(option="JPASSWD")
jproject = readconfig(option="JPROJECT")
jversion = readconfig(option="JVERSION")

myjira = GetJiraData(jurl,juser,jpasswd)
myjira.ExistProject(jproject)

bugdic = myjira.get_bugtypes(jproject,jversion)
peopledic = myjira.get_assignes(jproject, jversion)
modeldic = myjira.get_components(jproject, jversion)




draw("Bug类型", bugdic)
draw("经办人", peopledic)
draw("模块类型", modeldic)


Do = SendMali()
Do.main(total())