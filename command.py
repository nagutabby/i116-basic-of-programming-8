from cname import CName

class Command():
    def __init__(self, cname, x) -> None:
        self.cname = cname
        if cname == CName.PUSH:
            self.num = x
    def __str__(self) -> str:
        if self.cname == CName.PUSH:
            return str(self.cname) + '(' + str(self.num) + ')'
        else:
            return str(self.cname)

