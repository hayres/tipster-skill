---
name: tipster
description: Cheltenham 2026 Race Card & Tipster. Fetches tomorrow's race cards and suggests winners based on current market sentiment and historical trends.
---

# Tipster Skill

This skill helps you navigate the 2026 Cheltenham Festival by providing up-to-date race cards and consensus-based winner predictions.

## Usage

### 1. View Race Card
Fetches the card for a specific day of the festival. See [references/schedule_trends.md](references/schedule_trends.md) for full times and trends.

**Example:**
```bash
python3 scripts/get_card.py --day 1
```

### 2. Get Tips
Analyzes the runners and provides a list of recommended winners (NAPs, each-way value, etc.).

**Example:**
```bash
python3 scripts/get_tips.py --day 1
```

## Security & Ethics
This skill provides information and predictions for entertainment and competition purposes only. It does not facilitate real-money gambling.

---

**Steer for the win.**
