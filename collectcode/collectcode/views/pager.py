#-*-coding:utf8-*-

class Pager():    
    #总记录
    total = 0
    #当前页
    current_num = 1
    #每页记录
    page_size = 10
    #是否有前一页
    has_previous = False
    #前一页
    previous_page_num = 1
    #是否有后一页
    has_next = False
    #后一页
    next_page_num = 1
    #总页数
    total_page = 1
    
    def __init__(self,total,current_num,page_size):
        self.total = total
        self.current_num = current_num
        self.page_size = page_size
    
    def show(self):
        self.total_page = (self.total+self.page_size -1)/self.page_size
        if self.total_page == 1:
            return self
        if self.current_num == 1:
            self.has_next = True
            self.next_page_num = self.current_num + 1
        elif self.current_num > 1 and self.current_num < self.total_page:
            self.has_next = True
            self.has_previous = True
            self.next_page_num = self.current_num + 1
            self.previous_page_num = self.current_num - 1
        else:
            self.has_previous = True
            self.previous_page_num = self.current_num - 1
        return self