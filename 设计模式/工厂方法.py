# -*- coding: utf-8 -*- 
# @Time : 2019/11/18 11:33 
# @Author : 赵金林
# @Site :  
# @File : 工厂方法.py

class ChinaGetter:
    def __init__(self):
        self.trans = dict(dog="小狗", cat="小猫")

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter:
    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    languages = dict(English=EnglishGetter, China=ChinaGetter)
    return languages[language]()


e, g = get_localizer("English"), get_localizer("China")
for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))
