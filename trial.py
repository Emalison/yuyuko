import schedule
import time
#from mon9 import job_function
def job_function():
    print("DONE WELL")


#schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job_function)
#schedule.every().hour.do(job)
#schedule.every().day.at("11:55").do(job_function)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job_function)


while True:
    schedule.run_pending()
    time.sleep(1)
