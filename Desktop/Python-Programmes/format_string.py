def make_bold(orginal_func):
    def inner_func():
        return "<b>" + orginal_func() + "</b>"
    return inner_func

def make_italic(orginal_func):
    def inner_func():
        return "<i>" + orginal_func() + "</i>"
    return inner_func

def make_underline(orginal_func):
    def inner_func():
        return "<u>" + orginal_func() + "</u>"
    return inner_func


@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello())