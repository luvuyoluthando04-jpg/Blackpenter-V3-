# Blackpenter V3
# Demo-only analyzer — no real trades

def analyze_market(price):
    if price > 100:
        return "DEMO SIGNAL: BUY"
    elif price < 100:
        return "DEMO SIGNAL: SELL"
    else:
        return "DEMO SIGNAL: WAIT"


def main():
    demo_price = 100
    signal = analyze_market(demo_price)

    print("Blackpenter Analyzer V3")
    print("-----------------------")
    print("Demo price:", demo_price)
    print(signal)


if __name__ == "__main__":
    main()
