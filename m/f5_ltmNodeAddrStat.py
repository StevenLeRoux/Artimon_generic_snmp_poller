#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.ltm.node'
labels = '{class=lb,name=@INDEX@,@HOST@}'
bulk = {
  'ltmNodeAddrStatTotRequests': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmNodeAddrStatTotRequests."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.requests'
  },
  'ltmNodeAddrStatServerTotConns': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmNodeAddrStatServerTotConns."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.connections'
  },
  'ltmNodeAddrStatServerPktsIn': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmNodeAddrStatServerPktsIn."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.packets.in'
  },
  'ltmNodeAddrStatServerPktsOut': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmNodeAddrStatServerPktsOut."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.packets.out'
  },
  'ltmNodeAddrStatServerBytesIn': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmNodeAddrStatServerBytesIn."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.bytes.in'
  },
  'ltmNodeAddrStatServerBytesOut': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmNodeAddrStatServerBytesOut."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.bytes.out'
  },
}
