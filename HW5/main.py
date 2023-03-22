class PercentCalculator:
    # Attribute
    welcome_message = 'สวัสดีฉันคือโปรแกรมคำนวนร้อยละเปอร์เซ็นต์ คุณต้องการให้ฉันคำนวนอะไร ?'
    # Constructor

    def __init__(self, digit1=None, digit2=None, result=None):
        #print('Show this message when Instance was built')
        self.digit1 = digit1
        self.digit2 = digit2
        self.result = result

    # Method
    def get_output(self):
        print('Mode 1: ใช้สำหรับหาผลลัพธ์เปอร์เซนต์ที่ต้องการ')
        self.digit1 = float(input('Enter the number of percentages :'))
        self.digit2 = float(input('Enter the values :'))
        self.result = (self.digit1*self.digit2)/100
        return print('%.2f %% ของ %.2f คือ : %.2f' % (self.digit1, self.digit2, self.result))

    def get_percents(self):
        print('Mode 2: ใช้สำหรับหาเปอร์เซนต์ โดยตัวตั้ง และ ตัวหารที่ต้องการทราบ')
        self.digit1 = float(input('Enter the number of Dividend :'))
        self.digit2 = float(input('Enter the number of Divider :'))
        self.result = (self.digit1/self.digit2)*100
        return print('จำนวน %.2f คิดเป็น %.2f %% ของ %.2f' % (self.digit1, self.result, self.digit2))

    def get_input(self):
        print('Mode 3: ใช้สำหรับหาจำนวนตั้งต้น จากผลลัพธ์ และ เปอร์เซนต์')
        self.digit1 = float(input('Enter the number of outputs :'))
        self.digit2 = float(input('Enter the number of percents :'))
        self.result = (self.digit1*100)/self.digit2
        return print('จำนวน %.2f เป็น %.2f %% ของ %.2f' % (self.digit1, self.digit2, self.result))


class AppliedPercentsCalculator(PercentCalculator):
    def __init__(self, digit1=None, digit2=None, result=None):
        super().__init__(digit1, digit2, result)
        #print('Inheritance test result')
        print('Mode 4: ใช้สำหรับคำนวนค่าที่เพิ่มขึ้น หรือลดลงเป็นเปอร์เซนต์')
        self.digit1 = float(input('Enter 1st digits :'))
        self.digit2 = float(input('Enter 2nd digits :'))

        if self.digit1 > self.digit2:
            AppliedPercentsCalculator.get_decrease(self)
        elif self.digit1 < self.digit2:
            AppliedPercentsCalculator.get_increase(self)
        else:
            print('Please Try Again')

    def get_increase(self):
        self.result = ((self.digit2-self.digit1)/self.digit1)*100
        return print('จำนวน %.2f ถึง จำนวน %.2f เพิ่มขึ้น %.2f %%' % (self.digit1, self.digit2, self.result))

    def get_decrease(self):
        self.result = ((self.digit2-self.digit1)/self.digit2)*100
        return print('จำนวน %.2f ถึง จำนวน %.2f ลดลง %.2f %%' % (self.digit2, self.digit1, self.result))


print('================================================================')


if __name__ == '__main__':

    # test01 = PercentCalculator()
    # print(test01.welcome_message)
    # test01.get_output()
    # test01.get_percents()
    # test01.get_input()
    test02 = AppliedPercentsCalculator()
    # test02.get_increase()
    # test02.get_decrease()
