class vscode:
    def execute(self):
        print("compiling")
        print("running")

class Myeditor:
    def execute(self):
        print("spell checking")
        print("convention check")
        print("compliling")
        print("running")


class Laptops:
    def code(self,ide):
        ide.execute()

ide=Myeditor()

lap1=Laptops()
lap1.code(ide)

