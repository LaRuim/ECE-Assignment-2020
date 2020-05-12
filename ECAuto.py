import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
from datetime import datetime

#laruim

def load(tag, options='xpath'):
    if options == 'xpath':
        return waiter.until(EC.presence_of_element_located((By.XPATH, tag)))

#laruim

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")

#laruim

chrome = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
waiter = WebDriverWait(chrome, 30)
with open('log.txt', 'w+') as logfile:

    def log(message):
        log_output = datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + ': ' + message
        print(log_output)
        logfile.write(log_output+'\n')

#laruim

    def initWebsite1(root, part):
        site = root.format(part)
        chrome.get(site)
        log(r'Initialised website: {}'.format(site))
        time.sleep(0.5)
        base_slider = load(r'//*[@id="base_r"]')
        log(r'Found Base Slider')
        var_slider = load(r'//*[@id="collector_r"]')
        log(r'Found Other Slider')
        reading = load(r'//*[@id="add"]')
        log(r'Found Reading Button')
        plotgraph = load(r'//*[@id="plt"]')
        log(r'Found Plot Button')
        return base_slider, var_slider, reading, plotgraph

    def initWebsite2(site):
        chrome.get(site)
        log(r'Initialised website: {}'.format(site))
        time.sleep(0.5)
        dcvolt = load(r'//*[@id="vdc"]')
        log(r'Found DC Voltage Slider')
        zvolt = load(r'//*[@id="znrvlt"]')
        log(r'Found Zener Voltage Slider')
        res_s = load(r'//*[@id="res1"]')
        log(r'Found Series Resistance Slider')
        res_l = load(r'//*[@id="res2"]')
        log(r'Found Load Resistance Slider')
        reading = load(r'//*[@id="add"]')
        log(r'Found Reading Button')
        plotgraph = load(r'//*[@id="plt"]')
        log(r'Found Plot Button')
        return dcvolt, zvolt, res_s, res_l, reading, plotgraph


    def execute1(base_slider, var_slider, reading, plotgraph, part, step, var_slider_val):
        for _ in range(var_slider_val-1):
            var_slider.send_keys(Keys.RIGHT)
        log(r'Set Variable Slider value')
        for _ in range(step-1):
            base_slider.send_keys(Keys.RIGHT)
        reading.click()
        log(r'Reading 1 taken')
        for r in range(10):
            for _ in range(step):
                base_slider.send_keys(Keys.RIGHT)
            reading.click()
            log(r'Reading {} taken'.format(r+2))
        
        plotgraph.click()

        log(r'Graph Plotted')
        chrome.execute_script("document.body.style.zoom='90%'")
        chrome.save_screenshot(r'./Screenshots/{}.png'.format(part))

        log(r'Screenshot taken')



    def execute2(dcvolt, zvolt, res_s, res_l, reading, plotgraph, val_zvolt):
        load(r'//*[@id="check-button"]').click()
        try:
            chrome.switch_to.alert.accept()
        except:
            pass
        for _ in range(18):
            dcvolt.send_keys(Keys.LEFT)
            zvolt.send_keys(Keys.LEFT)
            res_s.send_keys(Keys.LEFT)
            res_l.send_keys(Keys.LEFT)
            res_l.send_keys(Keys.LEFT)
            res_s.send_keys(Keys.LEFT)
            zvolt.send_keys(Keys.LEFT)
            dcvolt.send_keys(Keys.LEFT)
            
        for _ in range(15):
            res_l.send_keys(Keys.LEFT)
            dcvolt.send_keys(Keys.LEFT)
        
        for _ in range(30):
            dcvolt.send_keys(Keys.LEFT)

        log(r'Reset Slider Values')

        for _ in range(int((val_zvolt-3.3)*10 - 1)):
            zvolt.send_keys(Keys.RIGHT)
        
        log(r'Set Zener Voltage Slider value')

        for _ in range(random.randint(20, 30)):
            res_s.send_keys(Keys.RIGHT)

        log(r'Set Series Resistance Slider value')

        for _ in range(random.randint(30, 40)):
            res_l.send_keys(Keys.RIGHT)

        log(r'Set Load Resistance Slider value')

        reading.click()
        log(r'Reading 1 taken')

        for r in range(10):
            for _ in range(15):
                dcvolt.send_keys(Keys.RIGHT)
            reading.click()
            log(r'Reading {} taken'.format(r+2))

        plotgraph.click()
        log(r'Graph Plotted')

        chrome.execute_script("document.body.style.zoom='90%'")
        chrome.save_screenshot(r'./Screenshots/{}.png'.format('3'))
        log(r'Screenshot taken')


    ROOT = r'http://vlabs.iitkgp.ernet.in/be/exp11/bjtce{}_ver1.html'
    base_slider, var_slider, reading, plotgraph = initWebsite1(ROOT, 'in')
    step = random.randint(1,10)
    log(r'Chosen step: {}'.format(step))
    execute1(base_slider, var_slider, reading, plotgraph, '1in', step, 10)
    var_slider, base_slider, reading, plotgraph = initWebsite1(ROOT, 'op')
    step = random.randint(1,5)
    log(r'Chosen step: {}'.format(step))
    execute1(base_slider, var_slider, reading, plotgraph, '1op', step, 15)

    ROOT = r'http://vlabs.iitkgp.ernet.in/be/exp12/bjtcb{}_ver1.html'
    base_slider, var_slider, reading, plotgraph = initWebsite1(ROOT, 'in')
    step = random.randint(1,10)
    log(r'Chosen step: {}'.format(step))
    execute1(base_slider, var_slider, reading, plotgraph, '2in', step, 10)
    var_slider, base_slider, reading, plotgraph = initWebsite1(ROOT, 'op')
    step = random.randint(1,5)
    log(r'Chosen step: {}'.format(step))
    execute1(base_slider, var_slider, reading, plotgraph, '2op', step, 12)

    ROOT = r'https://eceassignment-pesu-btech-2020.netlify.app/'
    dcvolt, zvolt, res_s, res_l, reading, plotgraph = initWebsite2(ROOT)
    zvolt_value = random.randint(60,70)/10
    log(r'Chosen Zener Voltage Value: {}'.format(zvolt_value))
    execute2(dcvolt, zvolt, res_s, res_l, reading, plotgraph, zvolt_value)