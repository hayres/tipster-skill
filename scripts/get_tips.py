import sys
import json

def get_day_1_tips():
    return [
        {"time": "13:20", "race": "Supreme Novices’ Hurdle", "selection": "Old Park Star", "type": "Win"},
        {"time": "14:00", "race": "Arkle Novices’ Chase", "selection": "Lulamba", "type": "Win"},
        {"time": "14:40", "race": "Ultima Handicap Chase", "selection": "Jagwar", "type": "Each Way"},
        {"time": "16:00", "race": "Champion Hurdle", "selection": "Lossiemouth", "type": "NAP (Win)"},
        {"time": "16:40", "race": "Boodles (Fred Winter)", "selection": "Saratoga", "type": "Win"},
        {"time": "17:20", "race": "National Hunt Chase", "selection": "Backmersackme", "type": "Win"}
    ]

def main():
    # Simple CLI for Day 1
    tips = get_day_1_tips()
    print(f"{'Time':<8} {'Race':<30} {'Selection':<25} {'Type'}")
    print("-" * 75)
    for t in tips:
        print(f"{t['time']:<8} {t['race']:<30} {t['selection']:<25} {t['type']}")

if __name__ == "__main__":
    main()
