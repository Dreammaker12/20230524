class Programmer:
    def __init__(self, OS, language, work):
        self.OS = OS 
        self.language = language
        self.work = work
    def programming(self):
        print(f"{self.language}개발자로 코딩을 합니다.")
class security(Programmer):
    def programming(self):
        print(f"{self.language}개발자로 보안을 담당합니다.")
class developer(Programmer):
    def programming(self):
        print(f"{self.language}개발자로 소프트웨어 설계를 담당합니다.")

pro = Programmer("리눅스","C언어","자바개발자")

pro.programming()

security.programming(pro)

secu = security("윈도우","JAVA","자바보안설계자")
secu.programming()