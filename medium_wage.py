import argparse
import src.soc_provider as soc_provider


parser = argparse.ArgumentParser()
parser.add_argument("--occupation", help="Your Current Occupation / Title")
parser.add_argument("--state", help="Full Name of your current state")

args = parser.parse_args()
if not args.occupation or not args.state:
    parser.error("Both occupation and state are required.")

best_match = soc_provider.identify({"title": args.occupation})
if not best_match or best_match["prob"] < 0.1:
    print("Match not found, try using a title variant in your search")
    raise SystemExit

print(best_match["soc"])
