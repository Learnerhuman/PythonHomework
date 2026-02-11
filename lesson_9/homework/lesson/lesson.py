class CustomException(Exception):
    pass


#raise CustomException("xwxw")

class appplication(Exception):
    pass

class aa(appplication):
    pass

class netw(appplication):
    pass

try:
    raise aa("swswsws")
except appplication as e:
    print("caught")
