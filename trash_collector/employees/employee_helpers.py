def date_checker(customers_pickup_day):
    if customers_pickup_day == 0:
        customers_pickup_day = 'Monday'
        return customers_pickup_day
    elif customers_pickup_day == 1:
        customers_pickup_day = 'Tuesday'
        return customers_pickup_day
    elif customers_pickup_day == 2:
        customers_pickup_day = 'Wednesday'
        return customers_pickup_day
    elif customers_pickup_day == 3:
        customers_pickup_day = 'Thursday'
        return customers_pickup_day
    elif customers_pickup_day == 4:
        customers_pickup_day = 'Friday'
        return customers_pickup_day
    elif customers_pickup_day == 5:
        customers_pickup_day = 'Saturday'
        return customers_pickup_day
    else:
        customers_pickup_day = 'Sunday'
        return customers_pickup_day