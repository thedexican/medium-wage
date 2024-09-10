import argparse
import src.soc_provider as soc_provider
import src.data_provider as data_provider


parser = argparse.ArgumentParser()
parser.add_argument("--occupation", help="Your Current Occupation / Title")
parser.add_argument("--state", help="Full Name of your current state")
parser.add_argument("--sheet", help="Sheet Name", required=False)

args = parser.parse_args()
if not args.occupation or not args.state:
    parser.error("Both occupation and state are required.")

best_match = soc_provider.identify({"title": args.occupation})
if not best_match or best_match["prob"] < 0.1:
    print("Common Title not found, try using a title variant in your search")
    raise SystemExit

sheet = args.sheet or "state_M2023_dl"
percentile_array = data_provider.annual_percentiles_for_soc(
    best_match["soc"], args.state, sheet
)

if not percentile_array:
    print(
        "Salary data not found for SOC, confirm State or try using a title variant in your search"
    )
    raise SystemExit

print(percentile_array)
