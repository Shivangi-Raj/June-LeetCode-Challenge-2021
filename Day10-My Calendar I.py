#https://leetcode.com/problems/my-calendar-i/

class MyCalendar:

    def __init__(self):
        self.se=[]
        

    def book(self, start: int, end: int) -> bool:
        if len(self.se)==0:
            t=(start,end)
            self.se.append(t)
            return True
        else:
            ln=len(self.se)
            for i in range(ln):
                if start>self.se[i][0] and start<self.se[i][1]: 
                    return False
                elif end >self.se[i][0] and end<self.se[i][1]:
                    return False
                elif start<= self.se[i][0] and end>=self.se[i][1]:
                    return False
            t=(start,end)
            self.se.append(t)
            return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
