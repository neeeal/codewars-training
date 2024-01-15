def ips_between(start, end):
    start_list, end_list = start.split('.'), end.split('.')
    diff = [int(end_list[i])-int(start_list[i]) for i in range(4)]
    return sum([diff[i]*(256**(-i+3)) for i in range(4)])