#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.mem'
labels = '{class=lb,name=Host,@HOST@}'
bulk = {
  'sysHostMemoryUsed': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHostMemoryUsed.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.used'
  },
  'sysHostMemoryTotal': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHostMemoryTotal.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.total'
  },
}
