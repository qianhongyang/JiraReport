#coding = utf-8
from collections import Counter
from JiraReport.JiraInit import JiraInit



# 获取具体数据
assignee_li = []
components_li = []
bugtypes_li = []

class GetJiraData(JiraInit):


    def setup(self,project,version):
        jql = GetJiraData.JqlProjrct(project) + GetJiraData.JqlText(version)
        issues_counts = self.JqlContent(jql)
        return issues_counts

    # list转dict
    @staticmethod
    def all_dict(li):
        count = Counter(li)
        count_dict = dict(count)  # 类型：<type 'dict'>
        count_tuple = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
        return count_tuple

    # 获取jql对象
    def JqlContent(self,jqlcontent):
        jql = self.jr.search_issues(("%s"%jqlcontent), maxResults=300)
        return jql

    # 反射处理无自定义字段情况
    def get_isss(self,project, version, text):
        isss = self.setup(project, version)
        for i in isss:
            fie = self.jr.issue(i, fields="components,assignee,customfield_10301")
            try:
                eval(text)
            except AttributeError:
                continue

    # 获取模块
    def get_components(self,project,version):
        self.get_isss(project, version,
                      "components_li.append(fie.fields.components[0].name)")

        return self.all_dict(components_li)

    # 获取经办人
    def get_assignes(self,project,version):
        self.get_isss(project, version,
                      "assignee_li.append(fie.fields.assignee.displayName)")

        return self.all_dict(assignee_li)

    # 获取bug类型
    def get_bugtypes(self,project, version):
        self.get_isss(project, version,
                      "bugtypes_li.append(fie.fields.customfield_10301.value)")

        return self.all_dict(bugtypes_li)





