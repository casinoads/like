from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

class UserAgents:
    def __init__(self):
        pass

    def get_user_agent(self, driver):
        return driver.execute_script("return navigator.userAgent")

    def change_user_agent(self, driver):
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"python 3.10", "platform":"Windows"})

    def random_user_agent(self):
        software_names = [SoftwareName.CHROME.value]
        #operating_systems = [OperatingSystem.IOS.value, OperatingSystem.WINDOWS.value]
        operating_systems = [OperatingSystem.WINDOWS.value,OperatingSystem.MAC.value,OperatingSystem.LINUX.value]
        #[OperatingSystem.IOS.value, OperatingSystem.ANDROID.value,OperatingSystem.MAC.value,OperatingSystem.LINUX.value]
        #OperatingSystem.IOS.value, OperatingSystem.ANDROID.value,
        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
        #list of all user agents
        #user_agents = user_agent_rotator.get_user_agents()
        user_agent = user_agent_rotator.get_random_user_agent()
        #print(user_agent)
        return user_agent