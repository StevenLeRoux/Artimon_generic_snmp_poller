#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.cpu.tmm'
labels = '{class=lb,name=TMM@INDEX@,@HOST@}'
bulk = {
  'sysStatTmTotalCycles': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatTmTotalCycles.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.total'
  },
  'sysStatTmIdleCycles': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatTmIdleCycles.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.idle'
  },
  'sysStatTmSleepCycles': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatTmSleepCycles.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.sleep'
  },
}
