import argparse
import src.soc_provider as soc_provider
import src.data_provider as data_provider
import bisect

parser = argparse.ArgumentParser()
parser.add_argument("--occupation", help="Your Current Occupation / Title")
parser.add_argument("--state", help="Full Name of your current state")
parser.add_argument("--salary", help="Add your current salary as integer, e.g. 150000")
parser.add_argument("--sheet", help="Sheet Name", required=False)

args = parser.parse_args()
if not args.occupation or not args.state or not args.salary:
    parser.error("Both occupation, salary and state are required.")

best_match = soc_provider.identify({"title": args.occupation})
if not best_match or best_match["prob"] < 0.1:
    print("Common Title not found, try using a title variant in your search")
    raise SystemExit

sheet = args.sheet or "state_M2023_dl"
salary = int(args.salary)

percentile_array = data_provider.annual_percentiles_for_soc(
    best_match["soc"], args.state, sheet
)

if not percentile_array:
    print(
        "Salary data not found for SOC, confirm State or try using a title variant in your search"
    )
    raise SystemExit

#  bisect returns the position of the first element greater than or equal to value
idx_position = bisect.bisect_left(percentile_array, salary)

if idx_position == 0 or idx_position == len(percentile_array):
    print("Your salary is NOT within upper and lower range bounds")
    raise SystemExit

upper = idx_position
lower = idx_position - 1

percentiles = [
    "10th",
    "25th",
    "50th",
    "75th",
    "90th",
]

print(
    f"Your salary falls between the {percentiles[lower]} and {percentiles[upper]} percentiles of reported salaries"
)
