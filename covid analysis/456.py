from datetime import date
from datetime import timedelta
today = date.today()
yesterday = today - timedelta(days=1)
new_format = yesterday.strftime('%m-%d-%Y')
path = []
path.append('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + new_format +'.csv')
print(path)