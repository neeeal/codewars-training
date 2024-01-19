def make_readable(seconds):
    str_func = lambda x: f"0{x}" if(len(str(x))<2) else x
    sec = str_func(seconds%60)
    min = str_func((seconds//60)%60)
    hr = str_func((seconds//3600)%100)
    return "{}:{}:{}".format(hr,min,sec)