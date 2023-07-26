# time module
import time
import locale

locale.setlocale(locale.LC_ALL, 'uk_UA.utf8')

seconds = time.time()
print(seconds)  # 1690191544.724622

print(time.ctime(seconds))  # Mon Jul 24 12:39:04 2023
# time.clock()
# print(time.clock())


print(time.localtime(seconds))  # time.struct_time(tm_year=2023, tm_mon=7, tm_mday=24, tm_hour=12,
# tm_min=44, tm_sec=45, tm_wday=0, tm_yday=205, tm_isdst=1)
res = time.localtime(seconds)
print(res.tm_isdst)  # 1

print(time.strftime("%d.%m.%Y %H:%m:%S", time.localtime(1690192416.154508)))

pause = 2
print("program started")
time.sleep(pause)
print(pause, " seconds")

print("task")
t = 0.6
time.sleep(t)
print()
print("task completed")

start = time.monotonic()
time.sleep(5)
finish = time.monotonic()
res = finish - start
print(res)

print(time.strftime("Зараз: %B %d %Y", time.localtime(23456789089))) # Зараз: липень 25 2023 time.struct_time(
# tm_year=2023, tm_mon=7, tm_mday=25, tm_hour=17, tm_min=7, tm_sec=22, tm_wday=1, tm_yday=206, tm_isdst=1)
# додав import locale
# додав locale.setlocale(locale.LC_ALL, 'uk_UA.utf8')


