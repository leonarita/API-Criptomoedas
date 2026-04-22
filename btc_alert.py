import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import requests

BASE = "https://api.binance.com"
SYMBOL = os.getenv("BTC_SYMBOL", "BTCUSDT")
WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")
TZ = os.getenv("TIMEZONE", "America/Sao_Paulo")
THRESHOLD = float(os.getenv("DAILY_DROP_THRESHOLD", "-3"))


def ms(dt):
    return int(dt.astimezone(ZoneInfo("UTC")).timestamp() * 1000)


def get(url, params=None):
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()


def price():
    return float(get(f"{BASE}/api/v3/ticker/price", {"symbol": SYMBOL})["price"])


def open_at(dt, interval):
    data = get(f"{BASE}/api/v3/klines", {"symbol": SYMBOL, "interval": interval, "startTime": ms(dt), "limit": 1})
    return float(data[0][1])


def pct(cur, ref):
    return ((cur / ref) - 1) * 100


def main():
    if not WEBHOOK:
        raise RuntimeError("Missing DISCORD_WEBHOOK_URL")

    tz = ZoneInfo(TZ)
    now = datetime.now(tz)
    cur = price()

    day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week = day - timedelta(days=day.weekday())
    month = day.replace(day=1)
    year = day.replace(month=1, day=1)
    m3 = month.replace(month=month.month-3 if month.month > 3 else 12 + (month.month-3))

    refs = [
        ("Dia", day, "1m"),
        ("Semana", week, "1h"),
        ("Mês", month, "1h"),
        ("3 meses", m3, "1h"),
        ("Ano", year, "1h"),
    ]

    vals = []
    for name, dt, itv in refs:
        ref = open_at(dt, itv)
        vals.append((name, ref, pct(cur, ref)))

    if vals[0][2] > THRESHOLD:
        return

    lines = ["🚨 BTC Alert", f"Preço: {cur:,.2f}", ""]
    for n, r, p in vals:
        lines.append(f"{n}: {p:+.2f}% | {r:,.2f} -> {cur:,.2f}")

    requests.post(WEBHOOK, json={"content": "\n".join(lines)})


if __name__ == "__main__":
    main()
