from pandevice.objects import AddressGroup

from lib.actions import BaseAction


class ApplyAddressGroup(BaseAction):
    """
    Add/update address group to a firewall
    """
    def run(self, device_group, firewall, **kwargs):

        device = self.get_panorama(firewall, device_group)
        obj = AddressGroup(**kwargs)
        device.add(obj)
        obj.apply()

        device_value = device_group or firewall
        return True, "AddressGroup {} successfully applied to {}".format(obj.name, device_value)
