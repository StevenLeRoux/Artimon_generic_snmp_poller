#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.bytes'
labels = '{class=lb,@HOST@}'
bulk = {
  'sysStatClientBytesIn': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatClientBytesIn.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.client.in'
  },
  'sysStatClientBytesOut': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatClientBytesOut.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.client.out'
  },
  'sysStatServerBytesIn': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatServerBytesIn.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.server.in'
  },
  'sysStatServerBytesOut': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatServerBytesOut.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.server.out'
  },
}
