import pychrome

url = "https://www.guildfordgolf.com/teetimes/"

browser = pychrome.Browser(url=url)
tab = browser.new_tab()

tab.debug = True 

tab.start()
tab.Network.enable()
#res = tab.Network.getResponseBody()
#print(res)
#tab.call_method("Network.enable")
#tab.call_method("Page.navigate", url="https://github.com/fate0/pychrome", _timeout=5)
tab.stop()

browser.close_tab(tab)

#import json
#from pychrome import Tab
#
#def network_data(url):
#    # Start a new Chrome instance
#    tab = Tab()
#    tab.start()
#
#    # Enable Network domain
#    tab.Network.enable()
#
#    # Enable Page domain
#    tab.Page.enable()
#
#    # Open the URL
#    tab.Page.navigate(url=url, _timeout=5)
#
#    # Wait for the page to load
#    tab.wait(5)
#
#    # Get the network data
#    response = tab.Network.getResponseBody(url=url)
#
#    # Close the tab
#    tab.stop()
#
#    # Parse the response
#    if 'body' in response:
#        return response['body']
#
#    return None
#
#if __name__ == "__main__":
#    url = input("Enter the URL: ")
#    data = network_data(url)
#    if data:
#        print(json.loads(data))
#    else:
#        print("No network data found.")
#