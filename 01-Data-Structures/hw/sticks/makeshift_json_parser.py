class SimpleJsonParser:
    json_str = ""
    keys = []

    def get_keys(self):
        # get first json object returned by split and extract keys
        jks = self.json_str[0]
        index = 0
        while index < len(jks):
            while jks[index] != '"':
                index += 1
            index += 1
            key = ""
            while jks[index] != '"':
                key += jks[index]
                index += 1
            self.keys.append(key)
            index += 3
            if jks[index] == '"':
                index += 1
                while jks[index] != '"':
                    index += 1
                    if jks[index] == '"' and jks[index - 1] != '\\':
                        break
                index += 1

    def extract_values(self, json_obj):
        # getting values using keys generated by the get_keys function
        obj = {}
        for key_index, key_string in enumerate(self.keys):
            left_key = key_string
            left_pos = json_obj.find('"' + left_key + '":') + len(left_key) + 4
            if key_index == len(self.keys) - 1:
                right_pos = len(json_obj)
            else:
                right_key = self.keys[key_index + 1]
                right_pos = json_obj.find('"' + right_key + '":') - 2
            val = json_obj[left_pos:right_pos]
            # print(key_string, left_pos, right_pos, val)
            if val[0] == '"':
                val = val[1:-1]
            elif val == "null":
                val = None
            obj[key_string] = val

        return obj

    def parse(self, json_file_path):
        with open(json_file_path, encoding="unicode-escape") as json_file:
            self.json_str = json_file.read()[2:-2]
        json_parsed = []
        self.json_str = self.json_str.split("}, {")
        # hoping nobody used this sequence describing wine
        self.get_keys()
        for json_obj in self.json_str:
            json_parsed.append(self.extract_values(json_obj))
        return json_parsed


sjp = SimpleJsonParser()
winedata_1 = sjp.parse("files/winedata_1.json")
winedata_2 = sjp.parse("files/winedata_2.json")
winedata_full = []

# merging while getting rid of dupes
for wine in winedata_1:
    if wine not in winedata_2:
        winedata_full.append(wine)
winedata_full += winedata_2

# first we sort by wine name, then by price in reverse to
# fulfill the collision requirement
winedata_full = sorted(winedata_full, key=lambda x: x["title"])
winedata_full = sorted(winedata_full,
                       key=lambda x: int(x["price"])
                       if x["price"] is not None else 0,
                       reverse=True)


def save_formatted_json(json_arr, filename):
    with open(filename + ".json", "w", encoding="utf-8") as wff:
        wff.write("[\n")
        for index, i in enumerate(json_arr):
            wff.write("   {\n")
            for key_index, key in enumerate(i.keys()):
                wff.write(" " * 6 + '"' + key + '": ')
                val = i[key]
                if val is None:
                    val = "null"
                else:
                    # I dunno how to format these so here we go
                    val = val.replace('\\"', '"')
                    val = val.replace("\r", "\\r")
                    val = val.replace("\t", "\\t")
                    val = val.replace("\\T", "T")
                    val = val.replace("\n", "\\n")
                    val = val.replace('"', '\\"')
                    val = '"' + val + '"'
                wff.write(val)
                if key_index < len(list(i.keys())) - 1:
                    wff.write(",\n")
            wff.write("\n   }")
            if index < len(json_arr) - 1:
                wff.write(",")
            wff.write('\n')
        wff.write("]\n")


save_formatted_json(winedata_full, "winedata_full")


def get_avg_arr(arr):
    # returning average value of list with string values and None's
    arr = [int(x) for x in arr if x is not None]
    avg = 0
    if arr:
        avg = round(sum(arr) / len(arr), 1)
    return avg


statistics = {"wine": {}}
wines_explored = "Gewürztraminer, Riesling, " \
                 "Merlot, Madera, " \
                 "Tempranillo, Red Blend".split(", ")
wine_stats_1 = "min_price,max_price".split(",")
wine_stats_2 = "most_common_region,most_common_country".split(",")
for wine in wines_explored:
    statistics["wine"][wine] = {}

stats_short = {}
# collecting all values to count averages etc. and store them in
# statistics dict; all stats calculated for the whole set will be
# represented as lists to satisfy the collision requirement
for wine in wines_explored:
    stats_short[wine] = {
        "prices": [],
        "regions": [],
        "countries": [],
        "scores": []
    }

stats_common = {
    "winescores": {},
    "countries": {},
    "commentators": {}
}

for i in winedata_full:
    # calculating all stats in one pass over the dict
    name = i["variety"]
    if name in wines_explored:
        stats_short[name]["prices"].append(i["price"])
        stats_short[name]["regions"].append(i["region_1"])
        stats_short[name]["regions"].append(i["region_2"])
        stats_short[name]["countries"].append(i["country"])
        stats_short[name]["scores"].append(i["points"])
    if i["points"]:
        if name in stats_common["winescores"]:
            stats_common["winescores"][name].append(i["points"])
        else:
            stats_common["winescores"][name] = [i["points"]]
    if i["country"]:
        if i["country"] in stats_common["countries"]:
            stats_common["countries"][i["country"]]["scores"]. \
                append(i["points"])
            stats_common["countries"][i["country"]]["prices"]. \
                append(i["price"])
        else:
            stats_common["countries"][i["country"]] = {}
            stats_common["countries"][i["country"]]["scores"] = [i["points"]]
            stats_common["countries"][i["country"]]["prices"] = [i["price"]]
    if i["taster_name"]:
        if i["taster_name"] in stats_common["commentators"]:
            stats_common["commentators"][i["taster_name"]] += 1
        else:
            stats_common["commentators"][i["taster_name"]] = 1

for wine in stats_short:
    # counting averages for the particular wine varieties
    prices = [int(x) for x in stats_short[wine]["prices"] if x is not None]
    if prices:
        statistics["wine"][wine]["average_price"] = \
            round(sum(prices) / len(prices), 1)
        statistics["wine"][wine]["min_price"] = min(prices)
        statistics["wine"][wine]["max_price"] = max(prices)
    else:
        statistics["wine"][wine]["average_price"] = 0
        statistics["wine"][wine]["min_price"] = 0
        statistics["wine"][wine]["max_price"] = 0

    regions = [x for x in stats_short[wine]["regions"] if x is not None]
    if regions:
        statistics["wine"][wine]["most_common_region"] =\
            max(set(regions), key=regions.count)
    else:
        statistics["wine"][wine]["most_common_region"] = 0

    countries = [x for x in stats_short[wine]["countries"] if x is not None]
    if countries:
        statistics["wine"][wine]["most_common_country"] =\
            max(set(countries), key=countries.count)
    else:
        statistics["wine"][wine]["most_common_country"] = 0

    scores = [int(x) for x in stats_short[wine]["scores"] if x is not None]
    if scores:
        statistics["wine"][wine]["average_score"] = \
            round(sum(scores) / len(scores), 1)
    else:
        statistics["wine"][wine]["average_score"] = 0

# it is possible to count max and min price by just iterating from start/end
# of sorted winedata
max_prices = []
max_price = winedata_full[0]["price"]
min_prices = []
min_price = -1

for i in winedata_full:
    if i["price"] == max_price:
        max_prices.append(i["title"])
    else:
        break
for i in winedata_full[::-1]:
    if i["price"] is None:
        continue
    elif min_price == -1 or min_price == i["price"]:
        min_price = i["price"]
        min_prices.append(i["title"])
    else:
        break

statistics["most expensive wine"] = max_prices
statistics["cheapest wine"] = min_prices

for wine in stats_common["winescores"]:
    stats_common["winescores"][wine] =\
        get_avg_arr(stats_common["winescores"][wine])
for country in stats_common["countries"]:
    stats_common["countries"][country]["prices"] = \
        get_avg_arr(stats_common["countries"][country]["prices"])
    stats_common["countries"][country]["scores"] = \
        get_avg_arr(stats_common["countries"][country]["scores"])


def max_min_from_dict(data):
    result = []
    for i in data:
        result.append([i, data[i]])
    result_max = max(result, key=lambda x: x[1])
    result_max_all = [x for x in result if x[1] == result_max[1]]
    result_min = min(result, key=lambda x: x[1] if x[1] > 0 else 9999)
    result_min_all = [x for x in result if x[1] == result_min[1]]
    return [result_max_all, result_min_all]


best_wine, worst_wine = max_min_from_dict(stats_common["winescores"])
m_e_country, cheapest_country = max_min_from_dict(stats_common["winescores"])

# I had interpreted the task as finding wines with
# best and worst average scores
statistics["best wine"] = best_wine
statistics["worst wine"] = worst_wine

cp_dict = {c: stats_common["countries"][c]["prices"]
           for c in stats_common["countries"]}
cs_dict = {c: stats_common["countries"][c]["scores"]
           for c in stats_common["countries"]}

statistics["most expensive country"], statistics["cheapest country"] =\
    max_min_from_dict(cp_dict)
statistics["best country"], statistics["worst country"] =\
    max_min_from_dict(cs_dict)

statistics["most active reviewer"] =\
    max_min_from_dict(stats_common["commentators"])[0]

statistics = {"statistics": statistics}


def pp_dict(of, mydict, indent=0):
    # does its best to pretty print a dict into json file
    commas = len(mydict.items())
    for key, val in mydict.items():
        commas -= 1
        of.write("\t" * indent + '"' + key + '": ')
        if isinstance(val, dict):
            of.write("{\n")
            pp_dict(of, val, indent + 1)
            of.write("\t" * indent + "}")
        else:
            if isinstance(val, str):
                val = '"' + val + '"'
            elif isinstance(val, list):
                if isinstance(val[0], str):
                    val = "[" + ",".join([f'"{x}"' for x in val]) + "]"
                else:
                    val = "[" +\
                          ",".join([f'["{x[0]}", {x[1]}]' for x in val])\
                          + "]"
            of.write("\t" * (indent) + str(val))
        if commas:
            of.write(",\n")
        else:
            of.write("\n")


with open("stats.json", "w", encoding="utf-8") as of:
    of.write("{")
    pp_dict(of, statistics)
    of.write("}\n")

with open("stats.md", "w", encoding="utf-8") as f:
    # making a markdown file from stats
    f.write("##Wine Stats!\n\n")
    f.write("####Stats for selected varieties:\n\n")
    for wine in statistics["statistics"]["wine"]:
        f.write("#"*6 + wine + "\n\n")
        for key in statistics["statistics"]["wine"][wine]:
            f.write(" * **" + key + "**: *" +
                    str(statistics["statistics"]["wine"][wine][key]) +
                    "*\n")
    f.write("---\n")
    f.write("####General Stats:\n")
    for key in statistics["statistics"]:
        if key != "wine":
            f.write("#"*6 + "**" + key + "**: *" +
                    str(statistics["statistics"][key]) +
                    "*\n")
