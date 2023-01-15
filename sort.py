from time_compile import emo_compile


def sorted_list(wwr, sof, rem):
    list = []
    try:
        for i in wwr:
            list.append(i)
        for i in sof:
            list.append(i)
        for i in rem:
            list.append(i)
        for i in list:
            result = emo_compile(i)
            i["time"] = result.replace("days", "d")
            # i["time"] = result.replace(" day", "d")
            if "Featured" == i["time"]:
                i["time"] = 0
            elif "s" in i["time"]:
                i["time"] = int(i["time"].replace("s", ""))
            elif "h" in i["time"]:
                i["time"] = int(i["time"].replace("h", ""))*100
            elif "d" in i["time"]:
                i["time"] = int(i["time"].replace("d", ""))*10000
            elif "mo" in i["time"]:
                i["time"] = int(i["time"].replace("mo", ""))*1000000
        sort_list = sorted(list, key=lambda li: li["time"])
        for i in sort_list:
            if i["time"] == 0:
                i["time"] = "Featured"
            elif i["time"] < 61:
                i["time"] = f"{i['time']} seconds"
            elif i["time"] < 2500:
                if i["time"] != 100:
                    i["time"] = f"{int(i['time']/100)} hours"
                else:
                    i["time"] = f"{int(i['time']/100)} hour"
            elif i["time"] < 320000:
                if i["time"] != 10000:
                    i["time"] = f"{int(i['time']/10000)} days"
                else:
                    i["time"] = f"{int(i['time']/10000)} day"
            elif i["time"] < 11000000:
                i["time"] = f"{int(i['time']/1000000)} month"
    except:
        sort_list = []
    return sort_list
