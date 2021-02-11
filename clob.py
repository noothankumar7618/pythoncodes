class Computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("Configure is",self.cpu,self.ram)

com1=Computer("i5",'8gb')
com2=Computer("Ryzen 5",'16gb')

com1.config()
com2.config()