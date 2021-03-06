#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

class Rule:
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

class HeadingRule(Rule):
    type = 'heading'
    def condition(self,block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
    type = 'title'
    first = True

    def condition(self,block):
        if not self.first:
            return False
if __name__ == "__main__":
    pass