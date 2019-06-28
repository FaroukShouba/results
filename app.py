from database import Database
from result import Result


Database.initialise(user='postgres', password='0000', host='localhost', database='elections')
url = 'https://gist.githubusercontent.com/ifeslibya/a7f5b434d722348bdc354c1706f4d0ac/raw/' \
      '4e365e4e80b715a31b80b7175089affbc07f1841/results.json'
results = Result.load_results_from_url(url)
for result in results:
    result.save_to_db()