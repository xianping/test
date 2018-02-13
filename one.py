import calendar
from datetime import datetime, timedelta

def get_lastmonth_ds(ds_nodash):
    '''
    ds_nodash: the str, '20170501'
    return: last month days ['20150401'...'20150430']
    '''
    DS_NODASH_FORMAT = '%Y%m%d'
    date = datetime.strptime(ds_nodash, DS_NODASH_FORMAT)
    # we need the input data is first day of next month, to make sure partition by ds (20170501)
    if date.day != 1:
        print('error:input ds_nodash should be first day of month, like(20170501)')
        return ''
    end_date = date - timedelta(days=1)
    return end_date

print get_lastmonth_ds('20170501')
print get_lastmonth_ds('20170301')
print get_lastmonth_ds('20170101')
print get_lastmonth_ds('20170102')
#before revert ci
#after revert
