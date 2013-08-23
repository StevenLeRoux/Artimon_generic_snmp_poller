#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.connections'
labels = '{class=lb,@HOST@}'
bulk = {
  'sysTcpStatAccepts': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysTcpStatAccepts.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.tcp.accepts'
  },
  'sysTcpStatConnects': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysTcpStatConnects.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.tcp.connects'
  },
  'sysStatClientTotConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatClientTotConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.client'
  },
  'sysStatServerTotConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatServerTotConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.server'
  },
  'sysStatPvaClientTotConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatPvaClientTotConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.pva.client'
  },
  'sysStatPvaServerTotConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatPvaServerTotConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.pva.server'
  },
  'sysClientsslStatTotNativeConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysClientsslStatTotNativeConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.ssl.client'
  },
  'sysServersslStatTotCompatConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysServersslStatTotCompatConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.ssl.server'
  },
}
