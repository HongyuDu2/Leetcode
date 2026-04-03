class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))

        sum1 = 0
        for i in range(1,y1):
            if (i%4==0 and i%100 !=0) or (i%400==0):
                sum1 += 366
            else:
                sum1 += 365
        sum2 = 0
        for i in range(1,y2):
            if (i%4==0 and i%100 !=0) or (i%400==0):
                sum2 += 366
            else:
                sum2 += 365
        
        for i in range(1, m1):
            if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
                sum1 += 31
            elif i==4 or i==6 or i==9 or i==11:
                sum1 += 30
            else:
                if (y1%4==0 and y1%100 !=0) or (y1%400==0):
                    sum1 += 29
                else:
                    sum1 += 28
        for i in range(1, m2):
            if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
                sum2 += 31
            elif i==4 or i==6 or i==9 or i==11:
                sum2 += 30
            else:
                if (y2%4==0 and y2%100 !=0) or (y2%400==0):
                    sum2 += 29
                else:
                    sum2 += 28
        return abs(sum1-sum2+d1-d2)

        