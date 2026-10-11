(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function money(c) { return "$" + Math.floor(c / 100) + "." + ("0" + (c % 100)).slice(-2); }

  function trapPlan(wardrobes, lifeDays, priceDollars) {
    if (!(wardrobes > 0) || !(lifeDays > 0) || !(priceDollars > 0)) return { error: "wardrobes, life and price must be positive" };
    var traps = wardrobes;
    var bought = traps * Math.ceil(365 / lifeDays);
    var costCents = bought * priceDollars * 100;
    return { traps: traps, bought: bought, costCents: costCents };
  }

  function freezePlan(items, perLoad, hoursPerLoad) {
    if (!(items > 0) || !(perLoad > 0) || !(hoursPerLoad > 0)) return { error: "items, load and hours must be positive" };
    var loads = Math.ceil(items / perLoad);
    var days = loads * hoursPerLoad / 24;
    return { loads: loads, days: days };
  }

  function washPlan(items, perLoad, loadCents, dryCleanCents) {
    if (!(items > 0) || !(perLoad > 0) || !(loadCents > 0) || !(dryCleanCents > 0)) return { error: "items, load, wash and dry-clean must be positive" };
    var loads = Math.ceil(items / perLoad);
    var washCents = loads * loadCents;
    var dryCents = items * dryCleanCents;
    return { loads: loads, washCents: washCents, dryCents: dryCents, savedCents: dryCents - washCents };
  }

  function renderTrap(r, wardrobes, lifeDays, priceDollars) {
    return "A labeled trap in each of " + plural(wardrobes, "wardrobe") + ", a " + lifeDays + "-day trap life and $" + priceDollars + " a trap: " + plural(r.traps, "trap") + " out now, " + r.bought + " bought across the year - " + money(r.costCents) + " a year in traps.";
  }

  function renderFreeze(r, items, perLoad, hoursPerLoad) {
    return plural(items, "woolen") + " at a labeled " + perLoad + " to a load and " + hoursPerLoad + " hours a load: " + plural(r.loads, "freezer load") + ", " + plural(r.days, "day") + " end to end.";
  }

  function renderWash(r, items, perLoad, loadCents, dryCleanCents) {
    return plural(items, "item") + ", a labeled " + perLoad + " to a load and " + money(loadCents) + " a load against " + money(dryCleanCents) + " an item at the cleaners: " + plural(r.loads, "washer load") + " for " + money(r.washCents) + " against " + money(r.dryCents) + " dry-cleaned - " + money(r.savedCents) + " stays with you.";
  }

  var api = { trapPlan: trapPlan, freezePlan: freezePlan, washPlan: washPlan, renderTrap: renderTrap, renderFreeze: renderFreeze, renderWash: renderWash };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.MothMath = api;
})(this);
