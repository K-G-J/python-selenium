from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go('New York')
        bot.select_dates(check_in_date='2023-04-17',
                         check_out_date='2023-04-24')
        bot.select_adults(1)
        bot.click_search()
        bot.apply_filterations()
        bot.refresh()  # A workaround to let our bot grab the data properly
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print('\n You are trying to run the bot from command line \n Please make sure you have installed the Google Chrome WebDriver \n')
    else:
        raise
