class City(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name', 'csvname'):
            setattr(self, field, kwargs.get(field, None))


city_names = [
    'Aotizhongxin',
    'Changping',
    'Dingling',
    'Dongsi',
    'Guanyuan',
    'Gucheng',
    'Huairou',
    'Nongzhanguan',
    'Shunyi',
    'Tiantan',
    'Wanliu',
    'Wanshouxigong'
]

CSV_FILE_FORMAT = 'city/csv/PRSA_Data_{}_20130301-20170228.csv'
cities = {}
for index in range(len(city_names)):
    cities[str(index + 1)] = City(id=index + 1,
                                  name=city_names[index],
                                  csvname=CSV_FILE_FORMAT.format(city_names[index]))
