#coding=utf8
from com.youmogan.spider.url_generater import out_text_dir
from glob import glob

__author__ = "jun.yanj"
__date__ = "$2008-11-24 19:37:39$"

class DataLoader(object):
    """数据加载器基类"""
    resource_dir_ = ''
    def __init__(self, resource_dir_):
        self.__class__.resource_dir_ = resource_dir_
    def parse_data(self):
        """以list的list返回解析完毕的数据，内层list数据是tuple"""
        return []

class HumorDataLoader(DataLoader):
    """负责解析数据文件到符合表单的post数据"""
    def __init__(self, resource_dir_):
        super(HumorDataLoader, self).__init__(resource_dir_)
        #DataLoader.__init__(self, resource_dir)
    def parse_data(self):
        data = []
        for file in glob(self.__class__.resource_dir_ + '*.txt'):
            humor_file = open(file, 'r')
            humor_sepline = humor_file.readline().strip()
            while humor_sepline == '--ymg-humor--':
                subject = humor_file.readline().strip()
                content = humor_file.readline().strip()
                data.append([('subject', subject), ('content', content), ('type', '1'), ('status', '1')])
                humor_sepline = humor_file.readline().strip()
        return data

class IqDataLoader(DataLoader):
    """负责解析数据文件到符合表单的post数据"""
    def __init__(self, resource_dir_):
        super(IqDataLoader, self).__init__(resource_dir_)
    def parse_data(self):
        data = []
        for file in glob(self.__class__.resource_dir_ + '*.txt'):
            iq_file = open(file, 'r')
            iq_sepline = iq_file.readline().strip()
            while iq_sepline == '--ymg-iq--':
                subject = iq_file.readline().strip()
                answer = iq_file.readline().strip()
                data.append([('subject', subject), ('content', answer), ('type', '20000'), ('status', '1')])
                iq_sepline = iq_file.readline().strip()
        return data


class RiddleDataLoader(DataLoader):
    """负责解析数据文件到符合表单的post数据"""
    def __init__(self, resource_dir_):
        super(RiddleDataLoader, self).__init__(resource_dir_)
    def parse_data(self):
        data = []
        for file in glob(self.__class__.resource_dir_ + '*.txt'):
            riddle_file = open(file, 'r')
            start = True
            line = riddle_file.readline()
            while line != '':
                if line == '\n':
                    line = riddle_file.readline()
                    continue
                if start:
                    subject = '<p>' + line.strip() + ' [字谜]</p>'
                    start = False
                else:
                    content = '<p>' + line.strip() + '</p>'
                    start = True
                    data.append([('subject', subject), ('content', content), ('type', '30500'), ('status', '1')])
                line = riddle_file.readline()
        return data

if __name__ == "__main__":
    rdl = RiddleDataLoader(out_text_dir)
    print rdl.parse_data()
