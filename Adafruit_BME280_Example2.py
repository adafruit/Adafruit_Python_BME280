from Adafruit_BME280 import *
import curses

def main(stdscr):
    sensor = BME280(p_mode=BME280_OSAMPLE_8, t_mode=BME280_OSAMPLE_2, h_mode=BME280_OSAMPLE_1, filter=BME280_FILTER_16)
    stdscr.nodelay(1)
    tstart = time.time()
    while (stdscr.getch() == -1) :
        degrees = sensor.read_temperature()
        pascals = sensor.read_pressure()
        hectopascals = pascals / 100
        humidity = sensor.read_humidity()

        stdscr.addstr(0, 0, 'Timestamp = %0.3f sec' % (time.time() - tstart))
        stdscr.addstr(1, 0, 'Temp      = %0.3f deg C (%0.3f deg F)' % (degrees, ((degrees*9/5)+32)))
        stdscr.addstr(2, 0, 'Pressure  = %0.2f hPa' % hectopascals)
        stdscr.addstr(3, 0, 'Humidity  = %0.2f %%' % humidity)
        stdscr.addstr(5, 0, 'Press any key to exit...')
        stdscr.refresh()

        time.sleep(3)

        stdscr.erase()


curses.wrapper(main)

