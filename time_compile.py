"""_summary_

    Returns:
        _type_: _description_
    """
import re
import datetime


def time_compile(time):
    """_summary_

    Args:
        time (_type_): _description_

    Returns:
        _type_: _description_
    """
    if time != "Featured":
        p = re.compile(r"\d*[-]\d{2}[-]\d{2}")
        strs = re.compile(r"\d*\s*[a-zA-Z]*")
        g = p.search(time)
        query = g.group()
        sp = query.split("-")
        list = []
        for x in sp:
            list.append(int(x))
        wwr_date = datetime.datetime(list[0], list[1], list[2])
        now = datetime.datetime.today()
        target = now - wwr_date
        result = str(target)
        ti = strs.search(result)
        result_time = ti.group()
    else:
        result_time = "Featured"
    return result_time


def emo_compile(i):
    """_summary_

    Args:
        i (_type_): _description_

    Returns:
        _type_: _description_
    """
    li = i["time"]
    if li != "Featured":
        text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', li)
        a = text.encode('ascii', 'ignore').decode('ascii')
        result = a.replace("\t", "").replace(" ", "").replace("days", "d")
    else:
        result = "Featured"
    return result
