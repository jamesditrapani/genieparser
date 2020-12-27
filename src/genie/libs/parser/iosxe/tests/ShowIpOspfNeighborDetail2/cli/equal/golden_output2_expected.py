expected_output = \
        {
           "address-family":{
              "ipv4":{
                 "areas":{
                    "0.0.0.0":{
                       "virtual_links":{
                          "OSPF_VL1":{
                             "neighbors":{
                                "10.36.3.3":{
                                   "neighbor_router_id":"10.36.3.3",
                                   "interface":"OSPF_VL1",
                                   "address":"10.229.3.3",
                                   "priority":0,
                                   "state":"full",
                                   "statistics":{
                                      "nbr_event_count":12,
                                      "nbr_retrans_qlen":0,
                                      "total_retransmission":3,
                                      "last_retrans_scan_length":1,
                                      "last_retrans_max_scan_length":1,
                                      "last_retrans_scan_time_msec":0,
                                      "last_retrans_max_scan_time_msec":0
                                   },
                                   "dr_ip_addr":"0.0.0.0",
                                   "bdr_ip_addr":"0.0.0.0",
                                   "hello_options":"0x2",
                                   "dbd_options":"0x42",
                                   "dead_timer":"00:00:41",
                                   "uptime":"05:07:21",
                                   "index":"1/3,",
                                   "first":"0x0(0)/0x0(0)",
                                   "next":"0x0(0)/0x0(0)"
                                }
                             }
                          }
                       }
                    },
                    "0.0.0.1":{
                       "interfaces":{
                          "GigabitEthernet0/1":{
                             "neighbors":{
                                "10.36.3.3":{
                                   "neighbor_router_id":"10.36.3.3",
                                   "interface":"GigabitEthernet0/1",
                                   "address":"10.19.4.3",
                                   "priority":1,
                                   "state":"full",
                                   "statistics":{
                                      "nbr_event_count":6,
                                      "nbr_retrans_qlen":0,
                                      "total_retransmission":2,
                                      "last_retrans_scan_length":1,
                                      "last_retrans_max_scan_length":1,
                                      "last_retrans_scan_time_msec":0,
                                      "last_retrans_max_scan_time_msec":0
                                   },
                                   "dr_ip_addr":"10.19.4.4",
                                   "bdr_ip_addr":"10.19.4.3",
                                   "hello_options":"0x2",
                                   "dbd_options":"0x42",
                                   "dead_timer":"00:00:33",
                                   "uptime":"16:31:06",
                                   "index":"2/2,",
                                   "first":"0x0(0)/0x0(0)",
                                   "next":"0x0(0)/0x0(0)"
                                }
                             }
                          },
                          "GigabitEthernet0/0":{
                             "neighbors":{
                                "10.16.2.2":{
                                   "neighbor_router_id":"10.16.2.2",
                                   "interface":"GigabitEthernet0/0",
                                   "address":"10.229.4.2",
                                   "priority":1,
                                   "state":"full",
                                   "statistics":{
                                      "nbr_event_count":6,
                                      "nbr_retrans_qlen":0,
                                      "total_retransmission":1,
                                      "last_retrans_scan_length":1,
                                      "last_retrans_max_scan_length":1,
                                      "last_retrans_scan_time_msec":0,
                                      "last_retrans_max_scan_time_msec":0
                                   },
                                   "dr_ip_addr":"10.229.4.4",
                                   "bdr_ip_addr":"10.229.4.2",
                                   "dead_timer":"00:00:34",
                                   "uptime":"05:07:40",
                                   "index":"1/1,",
                                   "first":"0x0(0)/0x0(0)",
                                   "next":"0x0(0)/0x0(0)"
                                }
                             }
                          }
                       }
                    }
                 }
              }
           }
        }