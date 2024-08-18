rules = {}
err_log = set()  # error log set

def prepare_dict(rules_raw):
    for key in rules_raw:
        str = rules_raw.get(key).replace(" ", "").split("|")
        for i in str:
            if i.isupper():
                for j in i:
                    if j.isupper() and not j in rules_raw:
                        err_log.add(f"{i} key doesn't exist, wrong input")
                        return 1
            rules[key] = str
    for i in rules:
        for j in rules.get(i):
            print(f"{i} -> {j}")