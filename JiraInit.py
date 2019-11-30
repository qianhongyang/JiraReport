#coding=utf-8

__auth__="hongyang"

import datetime
from jira import JIRA
from JiraReport.LogAndExcept import logger,except_decorate




#获取jira原始数据
class JiraInit(object):



    @except_decorate("获取jira服务器错误,请确认能在网页中正确登录JIRA服务")
    def __init__(self,jurl,juser,jpasswd):
        self.jurl = jurl
        self.juser = juser
        self.jpasswd = jpasswd
        self.nowtime = datetime.datetime.now().strftime('%Y年%m月%d日')
        self.jr = JIRA(self.jurl,basic_auth=(self.juser,self.jpasswd))



    @except_decorate("用户错误")
    def authuser(self):
        name = self.jr.current_user()
        logger().info(u"当前登录用户:%s" % name)

    # 查询项目是否存在
    @except_decorate("未查询到项目")
    def ExistProject(self, jproject):

        projects = str(self.jr.projects())
        if jproject in projects:
            logger().info("存在项目%s" % jproject)
        else:
            logger().error("不存在项目%s" % jproject)
            exit(2)

    @staticmethod
    def JqlProjrct(jproject):
        jproject_ql = "project = %s "%jproject
        return jproject_ql

    @staticmethod
    def JqlText(jversion):
        jtext_ql = "AND text ~ %s "%jversion
        return jtext_ql

    @staticmethod
    def JqlBugType(jbugtype):
        jbugtype_ql = "AND bug类型 = %s "%jbugtype
        return jbugtype_ql

    @staticmethod
    def JqlModel(jmodel):
        jmodel_ql = "AND component = %s "%jmodel
        return jmodel_ql

    #获取全部模块类型
    def GetComponents(self,project):
        components = self.jr.project_components(project)
        return components

