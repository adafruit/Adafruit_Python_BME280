# Adafruit_Python_BME280

This Python driver allows you to read data from the [Adafruit BME280 Breakout](https://www.adafruit.com/products/2652) on a Raspberry Pi, Pi2 or similar device.

## Requirements

This driver requires that you have previously installed the
[Adafruit_Python_GPIO](https://github.com/adafruit/Adafruit_Python_GPIO) package.

On Raspbian, you can install this package with the following commands:

```
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
```

## Usage

To read a single set of data points from the BME, connect your Pi or Pi2
to the BME280 breakout using I2C (connect SCL0/1 to the SCK pin and SCL0/1
to the SDI pin), and run the following command from this folder:

```
python Adafruit_BME280_Example.py
```

## Credits

This driver is based on the [Adafruit_BMP](https://github.com/adafruit/Adafruit_Python_BMP)
driver by Tony DiCola (Adafruit Industries), with BME280 additions kindly provided by
David J. Taylor (www.satsignal.eu).

# MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
