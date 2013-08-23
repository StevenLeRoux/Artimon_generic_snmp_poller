#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


scope = ['device1','device2','...']
artimonVar = 'lb.http'
labels = '{class=lb,@HOST@}'
bulk = {
  'sysHttpStatResp2xxCnt': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatResp2xxCnt.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.responses.2xx'
  },
  'sysHttpStatResp3xxCnt': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatResp3xxCnt.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.responses.3xx'
  },
  'sysHttpStatResp4xxCnt': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatResp4xxCnt.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.responses.4xx'
  },
  'sysHttpStatResp5xxCnt': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatResp5xxCnt.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.responses.5xx'
  },
  'sysHttpStatNumberReqs': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatNumberReqs.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.requests'
  },
  'sysHttpStatRespBucket1k': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatRespBucket1k.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.responses.1k'
  },
  'sysHttpStatRespBucket4k': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatRespBucket4k.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.responses.4k'
  },
  'sysHttpStatRespBucket16k': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatRespBucket16k.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.responses.16k'
  },
  'sysHttpStatRespBucket32k': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatRespBucket32k.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.responses.32k'
  },
  'sysHttpStatRespBucket64k': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatRespBucket64k.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.responses.64k'
  },
  'sysHttpStatGetReqs': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatGetReqs.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.method.get'
  },
  'sysHttpStatPostReqs': {
    'regex':'^F5-BIGIP-SYSTEM-MIB::sysHttpStatPostReqs.(0)\s=\sCounter64:\s([0-9]+)',
    'suffix':'.method.post'
  },
}
