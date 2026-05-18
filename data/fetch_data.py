import fastf1
import pandas as pd
import os

cache_path = os.path.join(os.path.dirname(__file__), '..', 'cache')
fastf1.Cache.enable_cache(cache_path)

seasons = [2022, 2023, 2024]

rounds = range(1, 25)

all_laps = []

for year in seasons:
    for round_num in rounds:
        try:
            session = fastf1.get_session(year, round_num, 'Q')
            session.load(telemetry=False, weather=False, messages=False)
            laps = session.laps.copy()
            laps['Year'] = year
            laps['Round'] = round_num
            laps['Circuit'] = session.event['Location']
            all_laps.append(laps)
            print(f"✅ {year} Round {round_num} - {session.event['Location']}")
        except Exception as e:
            print(f"⛔ {year} Round {round_num} - {e}")

df = pd.concat(all_laps, ignore_index=True)
print(f'\nTotal laps: {len(df)}')