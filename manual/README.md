# Prerequisites
- Python 3
- Python Selenium
- Chrome Driver

On Debian-based distribution:
```bash
sudo apt-get install chromium-chromedriver python3-selenium
```

# Usage
To run all tests in parallel:
```bash
python3 manual/run.py
```
To run tests only for some countries:
```bash
python3 manual/run.py country1 country2 ...
```
For example:
```bash
python3 manual/run.py australia canada
```

After invocation results will be stored in file "list\_data.txt".
