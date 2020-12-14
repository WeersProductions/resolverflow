from datetime import datetime


def feature_user_age_in_days(user_date, post_date):
    user_date_datetime = datetime.strptime(user_date, "%m/%d/%Y %H:%M:%S")
    post_date_datetime = datetime.strptime(post_date, "%m/%d/%Y %H:%M:%S")
    return (post_date_datetime - user_date_datetime).days
