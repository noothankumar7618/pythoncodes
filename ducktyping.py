class PyCharm:   #editor

    def execute(self):
        print('Compiling')
        print('Running')

class MyEditor:   #another ide

    def execute(self):
        print("spellcheck")
        print("Covention check")
        print('Compiling')
        print('Running')

class Laptop:

    def code(self,ide):
        ide.execute()

ide=PyCharm()
ide=MyEditor()

lap1=Laptop()
lap1.code(ide)