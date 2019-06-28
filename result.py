import requests
from database import CursorFromConnectionFromPool


class Center:
    def __init__(self, center_number, center_name):
        self.center_number = center_number
        self.center_name = center_name


class Result(Center):
    def __init__(self, center_number, center_name, result_id, valid_votes):
        super().__init__(center_number, center_name)
        self.result_id = result_id
        self.valid_votes = valid_votes

    def __repr__(self):
        return "<Result {} and valid votes {}".format(self.center_name, self.valid_votes)

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO results (id, center_number, center_name, valid_votes) VALUES (%s, %s, %s, %s)',
                           (self.result_id, self.center_number, self.center_name, self.valid_votes))

    @classmethod
    def load_results_from_url(cls, url):
        resp = requests.get(url)
        results = resp.json()
        return [cls(result['Center Number'], result['Center Name'], result['id'], result['Valid Votes'])
                for result in results]
