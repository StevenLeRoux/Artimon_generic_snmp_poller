#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.ltm.virtualserver'
labels = '{class=lb,name=@INDEX@,@HOST@}'
bulk = {
  'ltmVirtualServStatTotRequests': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmVirtualServStatTotRequests."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.requests'
  },
  'ltmVirtualServStatClientTotConns': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmVirtualServStatClientTotConns."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.connections'
  },
  'ltmVirtualServStatClientPktsIn': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmVirtualServStatClientPktsIn."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.packets.in'
  },
  'ltmVirtualServStatClientPktsOut': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmVirtualServStatClientPktsOut."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.packets.out'
  },
  'ltmVirtualServStatClientBytesIn': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmVirtualServStatClientBytesIn."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.bytes.in'
  },
  'ltmVirtualServStatClientBytesOut': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmVirtualServStatClientBytesOut."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.bytes.out'
  },
}
