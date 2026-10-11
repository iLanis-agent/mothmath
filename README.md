# Moth math

The trap count, the freezer calendar and the wash-versus-dry-clean bill for a clothes moth outbreak - so the response runs on numbers instead of lavender folklore. Exact counting in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/mothmath/

## The three tools

- **Trap plan** - `trapPlan(wardrobes, lifeDays, priceDollars)`: traps out now, bought per year, yearly cost.
- **Freeze plan** - `freezePlan(items, perLoad, hoursPerLoad)`: freezer loads and days end to end.
- **Wash plan** - `washPlan(items, perLoad, loadCents, dryCleanCents)`: washer cost against dry-clean cost and the savings.

## Labeled norms (illustrative references, not guarantees)

- Trap life: 90 days, one trap per wardrobe. Freeze: 72 hours at -18 C per load, 6 items to a load. Wash: $1.50 a load against $12 an item dry-cleaned. Delicates and heavy infestations deserve a professional's call.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (12 cases, 60 checks)

Regenerate the oracle expectations: `python3 oracle.py`
