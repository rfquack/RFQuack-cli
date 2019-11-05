# RFQuack Command Line Interface Client
Command line interface client to [RFQuack](https://github.com/trendmicro/RFQuack) dongles.

# Install
```bash
$ git clone https://github.com/rfquack/RFQuack-cli
$ cd RFQuack-cli
$ python setup.py install
```
If you use [pipenv](https://pipenv.org) you can just `pipenv install -e .`.

# Usage
```bash
$ rfquack --help                      
Usage: rfq.py [OPTIONS] COMMAND [ARGS]...                                
                                                                         
Options:                                                                 
  -l, --loglevel [CRITICAL|ERROR|WARNING|INFO|DEBUG|NOTSET]              
  --help                          Show this message and exit.            
                                                                         
Commands:                                                                
  mqtt  RFQuack client with MQTT transport.                              
  tty   RFQuack client with serial transport.                            

$ rfquack mqtt --help                 
Usage: rfq.py mqtt [OPTIONS]                                             
                                                                         
  RFQuack client with MQTT transport. Assumes one dongle per MQTT broker.
                                                                         
Options:                                                                 
  -i, --client_id TEXT                                                   
  -H, --host TEXT                                                        
  -P, --port INTEGER                                                     
  -u, --username TEXT                                                    
  -p, --password TEXT                                                    
  --help                Show this message and exit.                      

$ rfquack tty --help                  
Usage: rfq.py tty [OPTIONS]                                              
                                                                         
  RFQuack client with serial transport.                                  
                                                                         
Options:                                                                 
  -b, --baudrate INTEGER                                                 
  -s, --bytesize INTEGER                                                 
  -p, --parity [M|S|E|O|N]                                               
  -S, --stopbits [1|1.5|2]                                               
  -t, --timeout INTEGER                                                  
  -P, --port TEXT           [required]                                   
  --help                    Show this message and exit.                  
```

# Example

```
$ rfquack mqtt -H localhost -P 1884
2019-04-10 18:04:31 local RFQuack[20877] INFO Transport initialized
2019-04-10 18:04:31 local RFQuack[20877] DEBUG Setting mode to IDLE
2019-04-10 18:04:31 local RFQuack[20877] DEBUG rfquack/in/set/status (2 bytes)
2019-04-10 18:04:31 local RFQuack[20877] INFO Transport pipe initialized (QoS = 2): mid = 2

...

In [1]: q.rx()
2019-04-10 18:04:45 local RFQuack[20877] DEBUG Setting mode to RX
2019-04-10 18:04:45 local RFQuack[20877] DEBUG rfquack/in/set/status (2 bytes)

In [2]: q.set_modem_config(modemConfigChoiceIndex=0, txPower=14, syncWords='', carrierFreq=433)
2019-04-10 18:04:58 local RFQuack[20877] INFO txPower = 14
2019-04-10 18:04:58 local RFQuack[20877] INFO modemConfigChoiceIndex = 0
2019-04-10 18:04:58 local RFQuack[20877] INFO syncWords =
2019-04-10 18:04:58 local RFQuack[20877] INFO carrierFreq = 433
2019-04-10 18:04:58 local RFQuack[20877] DEBUG rfquack/in/set/modem_config (11 bytes)

...

In [73]: 2019-04-10 18:24:16 local RFQuack[20877] DEBUG Message on topic rfquack/out/status
2019-04-10 18:24:16 local RFQuack[20877] DEBUG rfquack/out/status -> <class 'rfquack_pb2.Status'>: stats {
  rx_packets: 0
  tx_packets: 0
  rx_failures: 0
  tx_failures: 0
  tx_queue: 0
  rx_queue: 0
}
mode: IDLE
modemConfig {
  carrierFreq: 433.0
  txPower: 14
  isHighPowerModule: true
  preambleLen: 4
  syncWords: "CB"
}
```

The last message (i.e., on the `rfquack/out/status` topic) is automatically sent by the RFQuack dongle at first boot, and shows that the dongle is up and running, with some basic info about its status.

At this point you're good to go from here!

# License
Copyright (C) 2019 Trend Micro Incorporated.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

# Disclaimer
RFQuack is a research tool intended to analyze radio-frequency (RF) signals via
software, with native hardware support. It is not intended for malicious or
offensive purposes.
