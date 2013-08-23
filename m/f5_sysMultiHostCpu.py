#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.cpu'
labels = '{class=lb,name=CPU@INDEX@,@HOST@}'
bulk = {
  'sysMultiHostCpuUser': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysMultiHostCpuUser."0".([0-9])\s=\sCounter64:\s([0-9]+)',
    'suffix':'.user'
  },
  'sysMultiHostCpuIdle': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysMultiHostCpuIdle."0".([0-9])\s=\sCounter64:\s([0-9]+)',
    'suffix':'.idle'
  },
  'sysMultiHostCpuNice': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysMultiHostCpuNice."0".([0-9])\s=\sCounter64:\s([0-9]+)',
    'suffix':'.nice'
  },
  'sysMultiHostCpuSystem': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysMultiHostCpuSystem."0".([0-9])\s=\sCounter64:\s([0-9]+)',
    'suffix':'.system'
  },
  'sysMultiHostCpuIrq': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysMultiHostCpuIrq."0".([0-9])\s=\sCounter64:\s([0-9]+)',
    'suffix':'.irq'
  },
  'sysMultiHostCpuSoftIrq': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysMultiHostCpuSoftirq5m."0".([0-9])\s=\sCounter64:\s([0-9]+)',
    'suffix':'.softirq'
  },
  'sysMultiHostCpuIowait': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysMultiHostCpuIowait."0".([0-9])\s=\sCounter64:\s([0-9]+)',
    'suffix':'.iowait'
  },
}
