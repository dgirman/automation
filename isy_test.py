import time

from isy994.controller import Controller
import isy994

url = '192.168.20.12:9080'
#url = None # use autodiscovery

zwave_my_test_switch = 'W 018 On-Off Power Switch'
zwave_my_test_switch_flag = False


def isy_event_handler(container,item,event,*args):
    #print ('Event {} from {}: {} {}'.format(event,container.container_type,item.name,*args))
    #print(event)
    #print(container.container_type)
    print(container.container_type[0:5])
    #if container.container_type == 'Device: Name' and event == 'add' and container.container_type.find('No device') ==-1:
    #    print('--->{} -- {} |||| {}'.format(event, container.container_type, item.name))
    
    '''
    if container.container_type == 'Device' and event == 'add' and item.address == zwave_my_test_switch:
        print("got zwave device")
        global dimmer
        dimmer = item
    '''

try:
    c = Controller(url,port='9080',username='dgirman',password='44544',use_https=False,event_handler=isy_event_handler)

    """
    while True:
        if zwave_my_test_switch_flag:
            zwave_my_test_switch.set_level (0)
            zwave_my_test_switch_flag = False

        time.sleep(2)

        if not zwave_my_test_switch_flag:
            zwave_my_test_switch.set_level (100)
            zwave_my_test_switch_flag = True
    """

except KeyboardInterrupt:
    print("KeyboardInterrupt has been caught.")