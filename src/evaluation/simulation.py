import random

OPEN_PROB = {
    1: 0.45,
    2: 0.4,
    3: 0.38,
    4: 0.3,
    5: 0.35
}

CLICK_PROB = {
    1: 0.15,
    2: 0.12,
    3: 0.1,
    4: 0.08,
    5: 0.1
}

def simulate_campaign(df):
    opened, clicked = 0, 0

    for _, row in df.iterrows():
        barrier = row["predicted_barrier"]

        if random.random() < OPEN_PROB[barrier]:
            opened += 1
            if random.random() < CLICK_PROB[barrier]:
                clicked += 1

    total = len(df)

    return {
        "open_rate": opened / total,
        "click_rate": clicked / total
    }