import os
import chromedriver_autoinstaller
import RequirementsInstall as rqinstall


chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'

rqinstall.requirementsinstall()

def webdriverinstall():
    # Check if chrome driver is installed or not
    if os.path.exists(driver_path):
        print(f"chrome driver is insatlled: {driver_path}")
    else:
        print(f"install the chrome driver(ver: {chrome_ver})")
        chromedriver_autoinstaller.install(True)