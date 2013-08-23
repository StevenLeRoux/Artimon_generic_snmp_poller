#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.cpu'
labels = '{class=lb,name=CPU@INDEX@,@HOST@}'
bulk = {
  'sysGlobalHostCpuUser': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysGlobalHostCpuUser.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.user'
  },
  'sysGlobalHostCpuIdle': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysGlobalHostCpuIdle.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.idle'
  },
  'sysGlobalHostCpuNice': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysGlobalHostCpuNice.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.nice'
  },
  'sysGlobalHostCpuSystem': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysGlobalHostCpuSystem.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.system'
  },
  'sysGlobalHostCpuIrq': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysGlobalHostCpuIrq.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.irq'
  },
  'sysGlobalHostCpuSoftIrq': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysGlobalHostCpuSoftirq5m.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.softirq'
  },
  'sysGlobalHostCpuIowait': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysGlobalHostCpuIowait.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.iowait'
  },
}
