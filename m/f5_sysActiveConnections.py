#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.connections.active'
labels = '{class=lb,@HOST@}'
bulk = {
  'sysStatClientCurConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatClientCurConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.client'
  },
  'sysStatServerCurConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatServerCurConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.server'
  },
  'sysStatPvaClientCurConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatPvaClientCurConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.pva.client'
  },
  'sysStatPvaServerCurConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysStatPvaServerCurConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.pva.server'
  },
  'sysClientsslStatCurConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysClientsslStatCurConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.ssl.client'
  },
  'sysServersslStatCurConns': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysServersslStatCurConns.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.ssl.server'
  },
}
