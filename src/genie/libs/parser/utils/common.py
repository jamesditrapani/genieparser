'''Common functions to be used in parsers'''

# python
import re
import warnings

class Common():
    '''Common functions to be used in parsers.'''

    @classmethod
    def regexp(self, expression):
        def match(value):
            if re.match(expression, value):
                return value
            else:
                raise TypeError("Value '%s' doesnt match regex '%s'"
                                % (value, expression))
        return match

    @classmethod
    def convert_intf_name(self, intf):
        '''return the full interface name

            Args:
                intf (`str`): Short version of the interface name

            Returns:
                Full interface name fit the standard

            Raises:
                None

            example:

                >>> convert_intf_name(intf='Eth2/1')
        '''

        # Please add more when face other type of interface
        convert = {'Eth': 'Ethernet',
                   'Lo': 'Loopback',
                   'Fa': 'FastEthernet',
	               'Po': 'Port-channel',
                   'Null': 'Null',
                   'Gi': 'GigabitEthernet',
                   'Te': 'TenGigabitEthernet',
                   'mgmt': 'mgmt',
                   'Vl': 'Vlan'}
        m = re.search('([a-zA-Z]+)', intf) 
        m1 = re.search('([\d\/\.]+)', intf)
        if hasattr(m, 'group') and hasattr(m1, 'group'):
            int_type = m.group(0)
            int_port = m1.group(0)
            if int_type in convert.keys():
                return(convert[int_type] + int_port)
            else:
                return(intf)
        else:
            return(intf)


    @classmethod
    def retrieve_xml_child(self, root, key):
        '''return the root which contains the key from xml

            Args:

                root (`obj`): ElementTree Object, point to top of the tree
                key (`str`): Expceted tag name. ( without namespace)

            Returns:
                Element object of the given tag

            Raises:
                None

            example:

                >>> retrieve_xml_child(
                        root=<Element '{urn:ietf:params:xml:ns:netconf:base:1.0}rpc-reply' at 0xf760434c>,
                        key='TABLE_vrf')
        '''
        for item in root:
            if key in item.tag:
                return item
            else:
                root = item
                return self.retrieve_xml_child(root, key)


    @classmethod
    def compose_compare_command(self, root, namespace, expect_command):
        '''compose commmand from the xml Element object from the root,
           then compare with the command with the expect_command.
           Only work for cisco standard output.

            Args:

                root (`obj`): ElementTree Object, point to top of the tree
                namespace (`str`): Namesapce. Ex. {http://www.cisco.com/nxos:8.2.0.SK.1.:rip}
                expect_command (`str`): expected command.

            Returns:
                None

            Raises:
                AssertionError: xml tag cli and command is not matched
                Exception: No mandatory tag __readonly__ in output

            example:

                >>> compose_compare_command(
                        root=<Element '{urn:ietf:params:xml:ns:netconf:base:1.0}rpc-reply' at 0xf760434c>,
                        namespace='{http://www.cisco.com/nxos:8.2.0.SK.1.:rip}',
                        expect_command='show bgp all dampening flap-statistics')
        '''
        # get to data node
        cmd_node = root.getchildren()[0]
        # compose command from element tree
        # ex.  <nf:data>
        #        <show>
        #         <bgp>
        #          <all>
        #           <dampening>
        #            <flap-statistics>
        #             <__readonly__>
        cli = ''
        while True:
            # get next node
            try:
                cmd_node = cmd_node.getchildren()
                if len(cmd_node) == 1:

                    # when only have one child
                    cmd_node = cmd_node[0]

                    # <__XML__PARAM__vrf-name>
                    #  <__XML__value>VRF1</__XML__value>
                    # </__XML__PARAM__vrf-name>
                    if '__XML__value' in cmd_node.tag:
                        cli += ' ' + cmd_node.text

                elif len(cmd_node) > 1:

                   # <__XML__PARAM__interface>
                   #   <__XML__value>loopback100</__XML__value>
                   #   <vrf>
                   for item in cmd_node:
                       if '__XML__value' in item.tag:
                           cli += ' ' + item.text
                       else:
                           cmd_node = item
                           break
                else:
                    break
            except Exception:
                pass

            # get tag name
            tag = cmd_node.tag.replace(namespace, '')

            # __readonly__ is the end of the command
            if '__readonly__' not in tag:
                if '__XML__PARAM__' not in tag and \
                   '__XML__value' not in tag and \
                   'TABLE' not in tag:
                    cli += ' ' + tag
            else:
                break

            # if there is no __readonly__ but the command has outputs
            # should be warining
            if 'TABLE' in tag:
            	warnings.warn('Tag "__readonly__" should exsist in output when '
            		          'there are actual values in output')
            	break

        cli = cli.strip()
        # compare the commands
        assert cli == expect_command, \
            'Cli created from XML tags does not match the actual cli:\n'\
            'XML Tags cli: {c}\nCli command: {e}'.format(c=cli, e=expect_command)



    @classmethod
    def convert_xml_time(self, xml_time):
        '''Convert xml time "PT1H4M41S" to normal time "01:04:41"

            Args:
                xml_time (`str`): XML time

            Returns:
                Standard time string

            Raises:
                None

            example:

                >>> convert_xml_time(xml_time='PT1H4M41S')
                >>> "01:04:41"
        '''
        # P4DT12M38S
        # PT1H4M41S
        p = re.compile(r'^P((?P<day>\d+)D)?T((?P<hour>\d+)H)?((?P<minute>\d+)M)?((?P<second>\d+)S)?$')
        m = p.match(xml_time)
        if m:
            day = m.groupdict()['day']
            hour = m.groupdict()['hour']
            hour = 0 if not hour else int(hour)
            minute = m.groupdict()['minute']
            minute = 0 if not  minute else int(minute)
            second = m.groupdict()['second']
            second = 0 if not  second else int(second)

            if day:
                standard_time = "{d}d{h}h".format(d=day, h="%02d"% (hour))
            else:
                standard_time = ''
                standard_time += format("%02d"% (hour))
                standard_time += ' ' + format("%02d"% (minute))
                standard_time += ' ' +  format("%02d"% (second))

                standard_time = ':'.join(standard_time.strip().split())
        else:
            # P4M13DT21H21M19S
            standard_time = xml_time
        return standard_time
