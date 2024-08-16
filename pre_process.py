
rules = {}
err_log = set()  # error log set



def prepare_dict(rules_raw):
    for key in rules_raw:
        str=rules_raw.get(key).replace(" ", "").split("|")
        for i in str:
            if i.isupper():
                for j in i:
                    if j.isupper() and not j in rules_raw:
                        err_log.add(f"{i} key doesn't exist, excluded from rules")
                        str.remove(i)
            else:
                rules[key] = str
