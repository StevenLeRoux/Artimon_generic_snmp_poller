#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.mem'
labels = '{class=lb,name=TMM,@HOST@}'
bulk = {
  'sysStatMemoryUsed': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatMemoryUsed.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.used'
  },
  'sysStatMemoryTotal': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatMemoryTotal.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.total'
  },
}
