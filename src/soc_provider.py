import json
import requests


def identify(query={}):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": "https://research.ripl.org",
    }
    response = requests.post(
        "https://research.ripl.org/api/v1/sockit",
        data=json.dumps(query),
        headers=headers,
    )

    if response.status_code == 200:
        result = response.json()

        if len(result["socs"]) > 0:
            descending_sort = sorted(
                result["socs"], key=lambda soc: soc["prob"], reverse=True
            )
            return descending_sort[0]
        else:
            return False
    else:
        return False
