Artimon_generic_snmp_poller
===========================

This is a generic metric poller using SNMP which produces variables to be used with the Artimon time series framework.

## Dynamic Modules

Modules are a very small python file which describes the scope of a set of metric to be retrieved and the equivalence between SNMP OIDs and the Artimon Variable.

Given this example : 
```
scope = ['device1','device2']
artimonVar = 'lb.ltm.node'
labels = '{class=lb,name=@INDEX@,@HOST@}'
bulk = {
  'ltmNodeAddrStatTotRequests': {
    'regex':'^F5-BIGIP-LOCAL-MIB::ltmNodeAddrStatTotRequests."([^\s]+)"\s=\sCounter64:\s([0-9]+)',
    'suffix':'.requests'
  },
}

```
We retrieve the specific OID ```ltmNodeAddrStatTotRequests``` (see you specific MIB) on each device from the scope list and we parse the result using the provided regex. We get the index from the snmp response and the value which are catch in the regex.

The index value is mapped through ```@INDEX@``` as the name label and we suffix the provided suffix at the end of the ```artimonVar``` key.

The produced variables look like this : 

```
1377269041486 lb.ltm.node.requests{class=lb,name=/env/node_name,host=device1} 42
1377269041486 lb.ltm.node.requests{class=lb,name=/env/node_name,host=device2} 42
```

This example is done with a load balancer metric collect, but can fit with any other SNMP which use ```LongDisplayString``` type as index key.
