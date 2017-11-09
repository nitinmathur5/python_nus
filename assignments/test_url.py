import re
def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)


print( remove_urls("this is a test https://sdfs.sdfsdf.com/sdfsdf/sdfsdf/sd/sdfsdfs?bob=%20tree&jef=man lets see this too https://sdfsdf.fdf.com/sdf/f end"))
