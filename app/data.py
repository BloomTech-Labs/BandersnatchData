from os import getenv
from typing import Dict, Iterable

import pandas as pd
import altair as alt
from MonsterLab import Monster
from dotenv import load_dotenv
from pymongo import MongoClient


class Data:
    load_dotenv()
    db_url = getenv("DB_URL")
    db_name = getenv("DB_NAME")
    db_table = getenv("DB_TABLE")

    def connect(self):
        ...

    def find(self, query_obj: Dict, limit=0) -> pd.DataFrame:
        ...

    def insert(self, insert_obj: Iterable[Dict]):
        ...

    def update(self, query: Dict, data_update: Dict):
        ...

    def delete(self, query_obj: Dict):
        ...

    def seed(self, n_monsters):
        ...

    @property
    def count(self):
        ...

    def visualize(self, x_axis, y_axis, target, rarity):
        ...
