import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(n) + " " + (word if n == 1 else (form or word + "s"))
def money(c): return "$" + str(c // 100) + "." + str(c % 100).zfill(2)
def fmt(x): return str(jsnum(x))

def trap_plan(wardrobes, lifeDays, priceDollars):
    if not (wardrobes > 0) or not (lifeDays > 0) or not (priceDollars > 0):
        return {"error": "wardrobes, life and price must be positive"}
    traps = wardrobes
    bought = traps * math.ceil(365 / lifeDays)
    return {"traps": traps, "bought": bought, "costCents": bought * priceDollars * 100}

def freeze_plan(items, perLoad, hoursPerLoad):
    if not (items > 0) or not (perLoad > 0) or not (hoursPerLoad > 0):
        return {"error": "items, load and hours must be positive"}
    loads = math.ceil(items / perLoad)
    return {"loads": loads, "days": jsnum(loads * hoursPerLoad / 24)}

def wash_plan(items, perLoad, loadCents, dryCleanCents):
    if not (items > 0) or not (perLoad > 0) or not (loadCents > 0) or not (dryCleanCents > 0):
        return {"error": "items, load, wash and dry-clean must be positive"}
    loads = math.ceil(items / perLoad)
    wash = loads * loadCents
    dry = items * dryCleanCents
    return {"loads": loads, "washCents": wash, "dryCents": dry, "savedCents": dry - wash}

def render_trap(r, wardrobes, lifeDays, priceDollars):
    return ("A labeled trap in each of " + plural(wardrobes, "wardrobe") + ", a " + fmt(lifeDays)
            + "-day trap life and $" + fmt(priceDollars) + " a trap: " + plural(r["traps"], "trap")
            + " out now, " + fmt(r["bought"]) + " bought across the year - " + money(r["costCents"]) + " a year in traps.")

def render_freeze(r, items, perLoad, hoursPerLoad):
    return (plural(items, "woolen") + " at a labeled " + fmt(perLoad) + " to a load and " + fmt(hoursPerLoad)
            + " hours a load: " + plural(r["loads"], "freezer load") + ", " + plural(r["days"], "day") + " end to end.")

def render_wash(r, items, perLoad, loadCents, dryCleanCents):
    return (plural(items, "item") + ", a labeled " + fmt(perLoad) + " to a load and " + money(loadCents)
            + " a load against " + money(dryCleanCents) + " an item at the cleaners: " + plural(r["loads"], "washer load")
            + " for " + money(r["washCents"]) + " against " + money(r["dryCents"]) + " dry-cleaned - "
            + money(r["savedCents"]) + " stays with you.")

cases = []
for a in [(3, 90, 6), (2, 60, 8), (5, 120, 4), (0, 90, 6)]:
    r = trap_plan(*a)
    cases.append({"fn": "trapPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_trap(r, *a)})
for a in [(34, 6, 72), (12, 6, 72), (5, 6, 48), (0, 6, 72)]:
    r = freeze_plan(*a)
    cases.append({"fn": "freezePlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_freeze(r, *a)})
for a in [(34, 6, 150, 1200), (20, 8, 200, 900), (10, 10, 100, 500), (0, 6, 150, 1200)]:
    r = wash_plan(*a)
    cases.append({"fn": "washPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_wash(r, *a)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
