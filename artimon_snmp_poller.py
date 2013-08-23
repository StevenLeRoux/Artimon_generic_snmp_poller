#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


import sys
from multiprocessing import Pool
import re
import os
import time
import glob

atom = str(int(time.time() * 1000.0))

currentpath = 'PATH'


absolutemodules = glob.glob(currentpath + '/m/*.py')


def foobar(module):
  try:
    reg = {}
    _mod=os.getpid()
    module_exec = 'import m.' + module  +' as _module'
    exec module_exec
    for cmd in _module.bulk.keys():
      reg[cmd] = re.compile(_module.bulk[cmd]['regex'])
    currentfile = '/var/run/artimon/' + module + '.snmp.' + atom
    os.system('touch %s' % currentfile)
    os.system('touch %s' % currentfile)
    artimonfiletemp = '/var/run/artimon/' + module + '.artimon.' + atom
    artimonfile = '/var/run/artimon/' + module + '.artimon'
    art = open(artimonfiletemp,'w')
    for host in _module.scope:
      for cmd in _module.bulk.keys():
        os.system('snmpbulkwalk -v2c -c public %s %s >> %s' % (host,cmd,currentfile))
      currentopen = open(currentfile, 'r')
      lines = currentopen.readlines()
      for line in lines:
        line = line.strip()
        for oid in reg.keys():
          m = reg[oid].search(line)
          if m:
            index = m.group(1)
            value = m.group(2)
            art.write(atom + ' ' + _module.artimonVar + _module.bulk[oid]['suffix'] + _module.labels.replace('@INDEX@',index).replace('@HOST@','host=' + host) + ' ' + value + '\n')
            continue
      currentopen.close()
      os.unlink(currentfile)
    art.close()
    try:
      os.unlink(artimonfile)
      os.rename(artimonfiletemp,artimonfile)
    except:
      os.rename(artimonfiletemp,artimonfile)
  except ImportError:
    print "Can't import : " + module
  except Exception,e:
    print 'Error : ' + str(e)

if __name__ == '__main__':
  modules = []
  for module in absolutemodules:
    modulename = os.path.basename(module).replace('.py','')
    if not modulename == "__init__":
      modules.append(modulename)
  p = Pool(16)
  p.map(foobar, modules)
