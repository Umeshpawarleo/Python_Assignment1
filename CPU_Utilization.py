import psutil
import time

th=80
print("Monitoring CPU usage...")
try:
    while True:
        cpu_use=psutil.cpu_percent(interval=1)

        if cpu_use>th:
            print("Alert! CPU usage exceeds threshold: ",cpu_use,"%")
        else:
            print("CPU utilization is Normal ",cpu_use,"%")

except KeyboardInterrupt:
    print("Monitoring stopped by user actions")

except Exception as e:
    print(f"An error occurred : {str(e)}")