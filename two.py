import calendar
from datetime import datetime, timedelta

def get_lastmonth_ds(ds_nodash,isdash = False):
    '''
    ds_nodash: the str, '20170501'
    return: last month days ['20150401'...'20150430']
    '''
    DS_NODASH_FORMAT = '%Y%m%d'
    DS_FORMAT = '%Y-%m-%d'
    date = datetime.strptime(ds_nodash, DS_NODASH_FORMAT)
    # we need the input data is first day of next month, to make sure partition by ds (20170501)
    if date.day != 1:
        print('error:input ds_nodash should be first day of month, like(20170501)')
        return []
    target_date = date - timedelta(days=1)
    dt = target_date.replace(day=1)
    if isdash:
        s = dt.strftime(DS_FORMAT)
    else:
        s = dt.strftime(DS_NODASH_FORMAT)
    return s

print get_lastmonth_ds('20170501')
print get_lastmonth_ds('20170301',True)
