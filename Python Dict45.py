def mergdicts(dects):
    Dicts = { }; names = ""; res = [ ]
    for k in range(len(dects)-1, -1, -1):
        names += dects[k]["books"]
        res.append(dects[k].get("price"))
    Dicts.update({"books": names, "price": sum(res)})
    return Dicts
print(mergdicts([{"books": "python", "price": 480}, {"books": "java", "price": 350}]))
