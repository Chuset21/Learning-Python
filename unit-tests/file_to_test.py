def do_stuff(num=0):
    try:
        return int(num) + 5
    except (ValueError, TypeError) as err:
        return err
