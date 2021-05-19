from typing import List, Tuple
import numpy
import pandas as pd
from data_extractor import get_data
from data_extractor import User


class Dataset:
    def __init__(self, data: List[User]):
        d = sorted(data, key=lambda item: item['date'].timestamp())
        self.dataset = pd.DataFrame(d)

    def get_data_by_user_id(self, user_id: int) -> pd.DataFrame:
        return self.dataset.loc[self.dataset['id'] == user_id]

    def get_add_del_diff_by_user_id(self, user_id: int) -> Tuple[int]:
        dataframe = self.get_data_by_user_id(user_id)[['additions', 'deletions']]
        return tuple(dataframe['additions'].sub(dataframe['deletions']))

    def get_commits_by_user_id(self, user_id: int) -> Tuple[int]:
        return tuple(self.get_data_by_user_id(user_id)['commits'])

    def get_adc_coefficient_by_user_id(self, user_id: int) -> Tuple[float]:
        return tuple(
            numpy.array(self.get_add_del_diff_by_user_id(user_id)) / numpy.array(self.get_commits_by_user_id(user_id))
        )

    def get_date_by_user_id(self, user_id: int) -> Tuple[int]:
        return tuple(self.get_data_by_user_id(user_id)['date'])


if __name__ == "__main__":
    d = Dataset(get_data())
    print(d.dataset)


