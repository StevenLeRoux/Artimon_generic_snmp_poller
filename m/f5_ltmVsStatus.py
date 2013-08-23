#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.ltm.virtualserver.status'
labels = '{class=lb,name=@INDEX@,@HOST@}'
bulk = {
  'ltmVsStatusAvailState': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmVsStatusAvailState."([^\s]+)"\s=\sINTEGER:\s.*\(([0-9]+)\)',
    'suffix':'.availability'
  },
  'ltmVsStatusEnabledState': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmVsStatusEnabledState."([^\s]+)"\s=\sINTEGER:\s.*\(([0-9]+)\)',
    'suffix':'.enable'
  },
}
