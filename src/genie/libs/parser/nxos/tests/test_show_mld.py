# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.nxos.show_mld import ShowIpv6MldInterface, \
                                  ShowIpv6MldGroups, \
                                  ShowIpv6MldLocalGroups


# ==============================================
# Unit test for 'show ipv6 mld interface vrf all'
# Unit test for 'show ipv6 mld interface'
# Unit test for 'show ipv6 mld interface vrf <WORD>'
# ==============================================
class test_show_ipv6_mld_interface(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrfs": {
            "VRF1": {
                 "interface": {
                      "Ethernet2/2": {
                           "query_max_response_time": 16,
                           "querier": "fe80::5054:ff:fed7:c01f",
                           "group_policy": "test",
                           "group_timeout": 2578,
                           "enable_refcount": 4,
                           "version": 2,
                           "link_status": "up",
                           "immediate_leave": True,
                           "startup_query": {
                                "interval": 91,
                                "configured_interval": 31,
                                "count": 7
                           },
                           "last_member": {
                                "query_count": 7,
                                "mrt": 1
                           },
                           "robustness_variable": 7,
                           "oper_status": "up",
                           "host_version": 2,
                           "available_groups": 6400,
                           "membership_count": 2,
                           "query_interval": 366,
                           "configured_robustness_variable": 7,
                           "statistics": {
                                "sent": {
                                     "v1_queries": 0,
                                     "v2_reports": 102,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 82
                                },
                                "received": {
                                     "v1_queries": 0,
                                     "v2_reports": 416,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 82
                                }
                           },
                           "configured_querier_timeout": 255,
                           "link_local_groups_reporting": False,
                           "max_groups": 6400,
                           "enable": True,
                           "next_query_sent_in": "00:05:18",
                           "querier_timeout": 2570,
                           "ipv6": {
                                "2001:db1:1::1/64": {
                                     "ip": "2001:db1:1::1",
                                     "prefix_length": "64",
                                     "status": "valid"
                                }
                           },
                           "configured_query_max_response_time": 16,
                           "link_local": {
                                "ipv6_address": "fe80::5054:ff:fed7:c01f",
                                "address": "fe80::5054:ff:fed7:c01f",
                                "status": "valid"
                           },
                           "unsolicited_report_interval": 1,
                           "querier_version": 2,
                           "configured_query_interval": 366,
                           "configured_group_timeout": 260
                      }
                 }
            },
            "default": {
                 "interface": {
                      "Ethernet2/1": {
                           "query_max_response_time": 16,
                           "querier": "fe80::5054:ff:fed7:c01f",
                           "group_policy": "test",
                           "group_timeout": 2578,
                           "enable_refcount": 5,
                           "version": 2,
                           "link_status": "up",
                           "immediate_leave": True,
                           "startup_query": {
                                "interval": 91,
                                "configured_interval": 31,
                                "count": 7
                           },
                           "last_member": {
                                "query_count": 7,
                                "mrt": 1
                           },
                           "robustness_variable": 7,
                           "oper_status": "up",
                           "host_version": 2,
                           "available_groups": 6400,
                           "membership_count": 2,
                           "query_interval": 366,
                           "configured_robustness_variable": 7,
                           "statistics": {
                                "sent": {
                                     "v1_queries": 0,
                                     "v2_reports": 191,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 792
                                },
                                "received": {
                                     "v1_queries": 0,
                                     "v2_reports": 1775,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 792
                                }
                           },
                           "configured_querier_timeout": 255,
                           "link_local_groups_reporting": False,
                           "max_groups": 6400,
                           "enable": True,
                           "next_query_sent_in": "00:03:01",
                           "querier_timeout": 2570,
                           "ipv6": {
                                "2001:db1:1:1::1/64": {
                                     "ip": "2001:db1:1:1::1",
                                     "prefix_length": "64",
                                     "status": "valid"
                                }
                           },
                           "configured_query_max_response_time": 16,
                           "link_local": {
                                "ipv6_address": "fe80::5054:ff:fed7:c01f",
                                "address": "fe80::5054:ff:fed7:c01f",
                                "status": "valid"
                           },
                           "unsolicited_report_interval": 1,
                           "querier_version": 2,
                           "configured_query_interval": 366,
                           "configured_group_timeout": 260
                      }
                 }
            }
       }
    }

    golden_output = {'execute.return_value': '''\
        ICMPv6 MLD Interfaces for VRF "VRF1"
        Ethernet2/2, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:db1:1::1/64 [VALID]
          Link Local Address : fe80::5054:ff:fed7:c01f(VALID)
          IPv6 Link-local Address: fe80::5054:ff:fed7:c01f
          ICMPv6 MLD parameters:
              Active Querier: fe80::5054:ff:fed7:c01f
              Querier version: 2, next query sent in: 00:05:18
              MLD Membership count: 2
              MLD version: 2, host version: 2
              MLD query interval: 366 secs, configured value: 366 secs
              MLD max response time: 16 secs, configured value: 16 secs
              MLD startup query interval: 91 secs, configured value: 31 secs
              MLD startup query count: 7
              MLD last member mrt: 1 secs
              MLD last member query count: 7
              MLD group timeout: 2578 secs, configured value: 260 secs
              MLD querier timeout: 2570 secs, configured value: 255 secs
              MLD unsolicited report interval: 1 secs
              MLD robustness variable: 7, configured value: 7
              MLD reporting for link-local groups: disabled
              MLD immediate leave: enabled
              MLD interface enable refcount: 4
              MLD Report Policy: test
              MLD State Limit: 6400,  Available States: 6400
          ICMPv6 MLD Statistics (sent/received):
          V1 Queries:          0/0         
          V2 Queries:         82/82        
          V1 Reports:          0/0         
          V2 Reports:        102/416       
          V1 Leaves :          0/0         
        ICMPv6 MLD Interfaces for VRF "default"
        Ethernet2/1, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:db1:1:1::1/64 [VALID]
          Link Local Address : fe80::5054:ff:fed7:c01f(VALID)
          IPv6 Link-local Address: fe80::5054:ff:fed7:c01f
          ICMPv6 MLD parameters:
              Active Querier: fe80::5054:ff:fed7:c01f
              Querier version: 2, next query sent in: 00:03:01
              MLD Membership count: 2
              MLD version: 2, host version: 2
              MLD query interval: 366 secs, configured value: 366 secs
              MLD max response time: 16 secs, configured value: 16 secs
              MLD startup query interval: 91 secs, configured value: 31 secs
              MLD startup query count: 7
              MLD last member mrt: 1 secs
              MLD last member query count: 7
              MLD group timeout: 2578 secs, configured value: 260 secs
              MLD querier timeout: 2570 secs, configured value: 255 secs
              MLD unsolicited report interval: 1 secs
              MLD robustness variable: 7, configured value: 7
              MLD reporting for link-local groups: disabled
              MLD immediate leave: enabled
              MLD interface enable refcount: 5
              MLD Report Policy: test
              MLD State Limit: 6400,  Available States: 6400
          ICMPv6 MLD Statistics (sent/received):
          V1 Queries:          0/0         
          V2 Queries:        792/792       
          V1 Reports:          0/0         
          V2 Reports:        191/1775      
          V1 Leaves :          0/0         
        ICMPv6 MLD Interfaces for VRF "management"

    '''}

    golden_parsed_output_1 = {
        "vrfs": {
            "default": {
                 "interface": {
                      "Ethernet2/1": {
                           "query_max_response_time": 16,
                           "querier": "fe80::5054:ff:fed7:c01f",
                           "group_policy": "test",
                           "group_timeout": 2578,
                           "enable_refcount": 5,
                           "version": 2,
                           "link_status": "up",
                           "immediate_leave": True,
                           "startup_query": {
                                "interval": 91,
                                "configured_interval": 31,
                                "count": 7
                           },
                           "last_member": {
                                "query_count": 7,
                                "mrt": 1
                           },
                           "robustness_variable": 7,
                           "oper_status": "up",
                           "host_version": 2,
                           "available_groups": 6400,
                           "membership_count": 2,
                           "query_interval": 366,
                           "configured_robustness_variable": 7,
                           "statistics": {
                                "sent": {
                                     "v1_queries": 0,
                                     "v2_reports": 191,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 792
                                },
                                "received": {
                                     "v1_queries": 0,
                                     "v2_reports": 1775,
                                     "v1_leaves": 0,
                                     "v1_reports": 0,
                                     "v2_queries": 792
                                }
                           },
                           "configured_querier_timeout": 255,
                           "link_local_groups_reporting": False,
                           "max_groups": 6400,
                           "enable": True,
                           "next_query_sent_in": "00:03:01",
                           "querier_timeout": 2570,
                           "ipv6": {
                                "2001:db1:1:1::1/64": {
                                     "ip": "2001:db1:1:1::1",
                                     "prefix_length": "64",
                                     "status": "valid"
                                }
                           },
                           "configured_query_max_response_time": 16,
                           "link_local": {
                                "ipv6_address": "fe80::5054:ff:fed7:c01f",
                                "address": "fe80::5054:ff:fed7:c01f",
                                "status": "valid"
                           },
                           "unsolicited_report_interval": 1,
                           "querier_version": 2,
                           "configured_query_interval": 366,
                           "configured_group_timeout": 260
                      }
                 }
            }
       }
    }

    golden_output_1 = {'execute.return_value': '''\
        ICMPv6 MLD Interfaces for VRF "default"
        Ethernet2/1, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:db1:1:1::1/64 [VALID]
          Link Local Address : fe80::5054:ff:fed7:c01f(VALID)
          IPv6 Link-local Address: fe80::5054:ff:fed7:c01f
          ICMPv6 MLD parameters:
              Active Querier: fe80::5054:ff:fed7:c01f
              Querier version: 2, next query sent in: 00:03:01
              MLD Membership count: 2
              MLD version: 2, host version: 2
              MLD query interval: 366 secs, configured value: 366 secs
              MLD max response time: 16 secs, configured value: 16 secs
              MLD startup query interval: 91 secs, configured value: 31 secs
              MLD startup query count: 7
              MLD last member mrt: 1 secs
              MLD last member query count: 7
              MLD group timeout: 2578 secs, configured value: 260 secs
              MLD querier timeout: 2570 secs, configured value: 255 secs
              MLD unsolicited report interval: 1 secs
              MLD robustness variable: 7, configured value: 7
              MLD reporting for link-local groups: disabled
              MLD immediate leave: enabled
              MLD interface enable refcount: 5
              MLD Report Policy: test
              MLD State Limit: 6400,  Available States: 6400
          ICMPv6 MLD Statistics (sent/received):
          V1 Queries:          0/0         
          V2 Queries:        792/792       
          V1 Reports:          0/0         
          V2 Reports:        191/1775      
          V1 Leaves :          0/0
    '''}
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldInterface(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


# ==============================================
# Unit test for 'show ipv6 mld groups'
# Unit test for 'show ipv6 mld groups vrf all'
# Unit test for 'show ipv6 mld groups vrf <WORD>'
# ==============================================
class test_show_ip_igmp_groups(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrfs": {
            "default": {
                 "groups_count": 2,
                 "interface": {
                      "Ethernet2/1": {
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reporter": "2001:db1:1:1::1",
                                               "expire": "never",
                                               "type": "static",
                                               "up_time": "00:26:28"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reporter": "2001:db1:1:1::1",
                                     "expire": "never",
                                     "type": "static",
                                     "up_time": "00:26:05"
                                }
                           }
                      }
                 }
            },
            "VRF1": {
                 "groups_count": 2,
                 "interface": {
                      "Ethernet2/2": {
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reporter": "2001:db1:1::1",
                                               "expire": "never",
                                               "type": "static",
                                               "up_time": "00:25:49"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reporter": "2001:db1:1::1",
                                     "expire": "never",
                                     "type": "static",
                                     "up_time": "00:25:49"
                                }
                           }
                      }
                 }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        MLD Connected Group Membership for VRF "default" - 2 total entries
        (2001:db8:0:abcd::2, ff30::2)
          Type: Static, Interface: Ethernet2/1
          Uptime/Expires: 00:26:28/never, Last Reporter: 2001:db1:1:1::1

        (*, fffe::2)
          Type: Static, Interface: Ethernet2/1
          Uptime/Expires: 00:26:05/never, Last Reporter: 2001:db1:1:1::1

        MLD Connected Group Membership for VRF "VRF1" - 2 total entries
        (2001:db8:0:abcd::2, ff30::2)
          Type: Static, Interface: Ethernet2/2
          Uptime/Expires: 00:25:49/never, Last Reporter: 2001:db1:1::1

        (*, fffe::2)
          Type: Static, Interface: Ethernet2/2
          Uptime/Expires: 00:25:49/never, Last Reporter: 2001:db1:1::1
    '''}

    golden_parsed_output_1 = {
        "vrfs": {
            "default": {
                 "groups_count": 2,
                 "interface": {
                      "Ethernet2/1": {
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reporter": "2001:db1:1:1::1",
                                               "expire": "never",
                                               "type": "static",
                                               "up_time": "00:26:28"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reporter": "2001:db1:1:1::1",
                                     "expire": "never",
                                     "type": "static",
                                     "up_time": "00:26:05"
                                }
                           }
                      }
                 }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        MLD Connected Group Membership for VRF "default" - 2 total entries
        (2001:db8:0:abcd::2, ff30::2)
          Type: Static, Interface: Ethernet2/1
          Uptime/Expires: 00:26:28/never, Last Reporter: 2001:db1:1:1::1

        (*, fffe::2)
          Type: Static, Interface: Ethernet2/1
          Uptime/Expires: 00:26:05/never, Last Reporter: 2001:db1:1:1::1
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldGroups(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldGroups(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldGroups(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# ==============================================
# Unit test for 'show ipv6 mld local-groups'
# Unit test for 'show ipv6 mld local-groups vrf all'
# Unit test for 'show ipv6 mld local-groups vrf <WORD>'
# ==============================================
class test_show_ipv6_mld_local_groups(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrfs": {
            "VRF1": {
                 "interface": {
                      "Ethernet2/2": {
                           "static_group": {
                                "fffe::2 *": {
                                     "group": "fffe::2",
                                     "source": "*"
                                },
                                "ff30::2 2001:db8:0:abcd::2": {
                                     "group": "ff30::2",
                                     "source": "2001:db8:0:abcd::2"
                                }
                           },
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reported": "1d07h",
                                               "type": "static"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reported": "1d07h",
                                     "type": "static"
                                },
                                "fffe::1": {
                                     "last_reported": "00:01:04",
                                     "type": "local"
                                },
                                "ff30::1": {
                                     "source": {
                                          "2001:db8:0:abcd::1": {
                                               "last_reported": "00:01:01",
                                               "type": "local"
                                          }
                                     }
                                }
                           },
                           "join_group": {
                                "ff30::1 2001:db8:0:abcd::1": {
                                     "group": "ff30::1",
                                     "source": "2001:db8:0:abcd::1"
                                },
                                "fffe::1 *": {
                                     "group": "fffe::1",
                                     "source": "*"
                                }
                           }
                      }
                 }
            },
            "default": {
                 "interface": {
                      "Ethernet2/1": {
                           "static_group": {
                                "fffe::2 *": {
                                     "group": "fffe::2",
                                     "source": "*"
                                },
                                "ff30::2 2001:db8:0:abcd::2": {
                                     "group": "ff30::2",
                                     "source": "2001:db8:0:abcd::2"
                                }
                           },
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reported": "1d07h",
                                               "type": "static"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reported": "1d07h",
                                     "type": "static"
                                },
                                "fffe::1": {
                                     "last_reported": "00:03:07",
                                     "type": "local"
                                },
                                "ff30::1": {
                                     "source": {
                                          "2001:db8:0:abcd::1": {
                                               "last_reported": "00:03:19",
                                               "type": "local"
                                          }
                                     }
                                }
                           },
                           "join_group": {
                                "ff30::1 2001:db8:0:abcd::1": {
                                     "group": "ff30::1",
                                     "source": "2001:db8:0:abcd::1"
                                },
                                "fffe::1 *": {
                                     "group": "fffe::1",
                                     "source": "*"
                                }
                           }
                      }
                 }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        MLD Locally Joined Group Membership for VRF "default"
        Group   Type     Interface   Last Reported 
        (*, fffe::1)
                Local    Eth2/1      00:03:07  
        (2001:db8:0:abcd::1, ff30::1)
                Local    Eth2/1      00:03:19  
        (2001:db8:0:abcd::2, ff30::2)
                Static   Eth2/1      1d07h     
        (*, fffe::2)
                Static   Eth2/1      1d07h     
        MLD Locally Joined Group Membership for VRF "VRF1"
        Group   Type     Interface   Last Reported 
        (*, fffe::1)
                Local    Eth2/2      00:01:04  
        (2001:db8:0:abcd::1, ff30::1)
                Local    Eth2/2      00:01:01  
        (2001:db8:0:abcd::2, ff30::2)
                Static   Eth2/2      1d07h     
        (*, fffe::2)
                Static   Eth2/2      1d07h  
    '''}

    golden_parsed_output_1 = {
        "vrfs": {
            "VRF1": {
                 "interface": {
                      "Ethernet2/2": {
                           "static_group": {
                                "fffe::2 *": {
                                     "group": "fffe::2",
                                     "source": "*"
                                },
                                "ff30::2 2001:db8:0:abcd::2": {
                                     "group": "ff30::2",
                                     "source": "2001:db8:0:abcd::2"
                                }
                           },
                           "group": {
                                "ff30::2": {
                                     "source": {
                                          "2001:db8:0:abcd::2": {
                                               "last_reported": "1d07h",
                                               "type": "static"
                                          }
                                     }
                                },
                                "fffe::2": {
                                     "last_reported": "1d07h",
                                     "type": "static"
                                },
                                "fffe::1": {
                                     "last_reported": "00:01:04",
                                     "type": "local"
                                },
                                "ff30::1": {
                                     "source": {
                                          "2001:db8:0:abcd::1": {
                                               "last_reported": "00:01:01",
                                               "type": "local"
                                          }
                                     }
                                }
                           },
                           "join_group": {
                                "ff30::1 2001:db8:0:abcd::1": {
                                     "group": "ff30::1",
                                     "source": "2001:db8:0:abcd::1"
                                },
                                "fffe::1 *": {
                                     "group": "fffe::1",
                                     "source": "*"
                                }
                           }
                      }
                 }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        MLD Locally Joined Group Membership for VRF "VRF1"
        Group   Type     Interface   Last Reported 
        (*, fffe::1)
                Local    Eth2/2      00:01:04  
        (2001:db8:0:abcd::1, ff30::1)
                Local    Eth2/2      00:01:01  
        (2001:db8:0:abcd::2, ff30::2)
                Static   Eth2/2      1d07h     
        (*, fffe::2)
                Static   Eth2/2      1d07h  
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6MldLocalGroups(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6MldLocalGroups(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6MldLocalGroups(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()