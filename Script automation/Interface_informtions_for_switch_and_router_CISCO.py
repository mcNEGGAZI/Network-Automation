from netmiko import ConnectHandler
import re 
import numpy as np
import pandas as pd

# here is list of cisco routers ip addresses



#here is list of cisco routers ip addresses
device_type_input='cisco_ios'
ip_input=input('Input SSH IP @ : ')
username_input=input('Input SSH Username :  ')
password_input=input('Input SSH Password :  ')
enable_secret_password_input=input('Input Enable password :  ')


def get_interface_info_router_CISCO(device_type_input, ip_input, username_input, password_input, enable_secret_password_input):
    

    devices = {
        'device_type': device_type_input,
        'ip': ip_input,
        'username': username_input,
        'password': password_input, 
        'secret': enable_secret_password_input
    }

    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_command('show interfaces | include (bia|Ethernet)')

    print(output)

    rech_name_number_interface='(Ethernet|FastEthernet)(\d+/\d+)'
    pattern_name_number_int=re.findall(rech_name_number_interface, output)
    rech_status_interface = 'is (up|down|administratively down),'
    pattern_status_int = re.findall(rech_status_interface, output)
    rech_line_protocol = 'line protocol is (up|down)'
    pattern_line_protocol = re.findall(rech_line_protocol, output)
    rech_hardware = 'Hardware is (\S+),'
    pattern_hardware = re.findall(rech_hardware, output)
    rech_mac_address = 'address is (\S+)'
    pattern_mac_address = re.findall(rech_mac_address, output)
    rech_biaddress = 'bia (\S+)'
    pattern_biaddress = re.findall(rech_biaddress, output)

    #diviser pattern_name_number_int en deux listes
    pattern_name = []
    pattern_number = []
    for i in range(len(pattern_name_number_int)):
        pattern_name.append(pattern_name_number_int[i][0])
        pattern_number.append(pattern_name_number_int[i][1])

    # Now you can create the NumPy array
    tableau = np.array([pattern_name,pattern_number, pattern_status_int, pattern_line_protocol, pattern_hardware, pattern_mac_address, pattern_biaddress])

    df = pd.DataFrame(tableau).T
    df.columns = ['Interface','Numero interface ', 'Status', 'Line Protocol', 'Hardware', 'MAC Address', 'BI Address']
    print(df)

    net_connect.disconnect()

def get_interface_info_switch_CISCO(device_type_input, ip_input, username_input, password_input, enable_secret_password_input):
    

    devices = {
        'device_type': device_type_input,
        'ip': ip_input,
        'username': username_input,
        'password': password_input, 
        'secret': enable_secret_password_input
    }

    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    show_interfaces_output = net_connect.send_command('show interfaces ')
    
    # Regular expressions to extract information
    interface_regex = r'(\S+) is (up|down|administratively down), line protocol is (up|down) (\((\S+)\))?'
    hardware_regex = r'\s+Hardware is (.+), address is (.+) \(bia (.+)\)'
    mtu_regex = r'\s+MTU (\d+) bytes, BW (\d+) Kbit/sec, DLY (\d+) usec,'
    reliability_regex = r'\s+reliability (\d+)/(\d+), txload (\d+)/(\d+), rxload (\d+)/(\d+)'
    encapsulation_regex = r'\s+Encapsulation (\S+), loopback (\S+) set'
    auto_settings_regex = r'\s+Auto-duplex, Auto-speed, media type is (\S+)'
    arp_regex = r'\s+ARP type: (\S+), ARP Timeout (\S+)'

    
    

    #creat a list of interfaces 
    interface_list = re.findall(interface_regex, show_interfaces_output)
    #separer interface_list  en quatre listes
    interface_name = []
    status_up_down = []
    line_protocol = []
    status = []
    for i in range(len(interface_list)):
        interface_name.append(interface_list[i][0])
        status_up_down.append(interface_list[i][1])
        line_protocol.append(interface_list[i][2])
        status.append(interface_list[i][3])

    
    
    #creat a list of hardware
    hardware_list = re.findall(hardware_regex, show_interfaces_output)
    #separer hardware_list  en trois listes
    hardware = []
    mac_address = []
    bi_address = []
    for i in range(len(hardware_list)):
        hardware.append(hardware_list[i][0])
        mac_address.append(hardware_list[i][1])
        bi_address.append(hardware_list[i][2])

    

    #creat a list of mtu
    mtu_list = re.findall(mtu_regex, show_interfaces_output)
    #separer mtu_list  en trois listes
    mtu = []
    bw = []
    dly = []
    for i in range(len(mtu_list)):
        mtu.append(mtu_list[i][0])
        bw.append(mtu_list[i][1])
        dly.append(mtu_list[i][2])
    
    
    #creat a list of reliability
    reliability_list = re.findall(reliability_regex, show_interfaces_output)
    #separer reliability_list  en trois listes
    reliability = []
    txload = []
    rxload = []
    for i in range(len(reliability_list)):
        reliability.append(reliability_list[i][0])
        txload.append(reliability_list[i][1])
        rxload.append(reliability_list[i][2])
    
    

    #creat a list of encapsulation
    encapsulation_list = re.findall(encapsulation_regex, show_interfaces_output)
    #separer encapsulation_list  en deux listes
    encapsulation = []
    loopback = []
    for i in range(len(encapsulation_list)):
        encapsulation.append(encapsulation_list[i][0])
        loopback.append(encapsulation_list[i][1])
    
    

    #creat a list of auto_settings
    auto_settings_list = re.findall(auto_settings_regex, show_interfaces_output)
    #separer auto_settings_list  en une listes
    auto_settings = []
    for i in range(len(auto_settings_list)):
        auto_settings.append(auto_settings_list[i][0])
    
    

    
    #creat a list of arp
    arp_list = re.findall(arp_regex, show_interfaces_output)
    #separer arp_list  en deux listes
    arp_type = []
    arp_timeout = []
    for i in range(len(arp_list)):
        arp_type.append(arp_list[i][0])
        arp_timeout.append(arp_list[i][1])
    
    

    #Regrouper les listes en un seul tableau
    listes=[interface_name, status_up_down, line_protocol, status, hardware, 
            mac_address, bi_address, mtu, bw, dly, reliability, txload, 
            rxload, encapsulation, loopback, auto_settings, arp_type, arp_timeout
            ]
    
    
    #derterminer la longueur de la liste la plus longue
    max_length = max(len(l) for l in listes)
    print(max_length)

    #determiner la longueur de chaque liste
    for liste in listes:
        while len(liste) < max_length:
            liste.append(None)
    
    # Now you can create the NumPy array
    tableau = np.array(listes).T
    df = pd.DataFrame(tableau)
    df.columns = ['Interface','Status', 'Line Protocol', 'Status', 'Hardware', 'MAC Address', 'BI Address', 'MTU', 'BW', 'DLY', 'Reliability', 'TXload', 'RXload', 'Encapsulation', 'Loopback', 'Auto Settings', 'ARP Type', 'ARP Timeout']
    #print(df)


    total_outpu_drop_regex=r'; Total output drops: (\S+)'
    total_outpu_drop=re.findall(total_outpu_drop_regex, show_interfaces_output)

    input_rate_regex=r'5 minute input rate (\d+) bits/sec, (\d+) packets/sec'
    input_rate_list=re.findall(input_rate_regex, show_interfaces_output)

    output_rate_regex=r'5 minute output rate (\d+) bits/sec, (\d+) packets/sec'
    output_rate_list=re.findall(output_rate_regex, show_interfaces_output)


    input_rate_bps=[]
    input_rate_pps=[]
    output_rate_bps=[]
    output_rate_pps=[]

    for i in range(len(input_rate_list)):
        input_rate_bps.append(input_rate_list[i][0])
        input_rate_pps.append(input_rate_list[i][1])


    for g in range(len(output_rate_list)):
        output_rate_bps.append(output_rate_list[i][0])
        output_rate_pps.append(output_rate_list[i][1])

    packet_output_regex=r'(\d+) packets output, (\d+) bytes, (\d+) underruns'
    packet_output_list=re.findall(packet_output_regex,show_interfaces_output)

    packet_out=[]
    packet_out_bytes=[]
    packet_out_underruns=[]
    for i in range(len(packet_output_list)):
        packet_out.append(packet_output_list[i][0])
        packet_out_bytes.append(packet_output_list[i][1])
        packet_out_underruns.append(packet_output_list[i][2])



    alpha_regex=r'(\d+) packets input, (\d+) bytes, (\d+) no buffer' 
    alpha=re.findall(alpha_regex, show_interfaces_output) #RETURN 3 VALUES 
    packet_input_ipt=[]
    bytess_ipt=[]
    no_buffer_ipt=[]
    for i in range(len(alpha)):
        packet_input_ipt.append(alpha[i][0])
        bytess_ipt.append(alpha[i][1])
        no_buffer_ipt.append(alpha[i][2])   



    fel_regex=r'(\d+) runts, (\d+) giants, (\d+) throttles'
    fel=re.findall(fel_regex, show_interfaces_output) #RETURN 3 VALUES
    runts_ipt=[]
    gigants_ipt=[]
    throttles_ipt=[]
    for i in range(len(fel)):
        runts_ipt.append(fel[i][0])
        gigants_ipt.append(fel[i][1])
        throttles_ipt.append(fel[i][2])


    bel_regex=r'(\d+) input errors, (\d+) CRC, (\d+) frame, (\d+) overrun, (\d+) ignored'
    bel=re.findall(bel_regex, show_interfaces_output) #RETURN 5 VALUES 
    input_errors_ipt=[]
    CRC_ipt=[]
    frame_ipt=[]
    overrun_ipt=[]
    ignored_input_ipt=[]
    for i in range(len(bel)):
        input_errors_ipt.append(bel[i][0])
        CRC_ipt.append(bel[i][1])
        frame_ipt.append(bel[i][2])
        overrun_ipt.append(bel[i][3])
        ignored_input_ipt.append(bel[i][4])


    gam_regex=r'(\d+) output buffer failures, (\d+) output buffers swapped out'
    otp_buffer_failures_otp=[]
    otp_buffer_swapped_otp=[]
    gam=re.findall(gam_regex, show_interfaces_output) #RETURN 2 VALUES
    for i in range(len(gam)):
        otp_buffer_failures_otp.append(gam[i][0])
        otp_buffer_swapped_otp.append(gam[i][1])


    sama=r'(\d+) unknown protocol drops'
    unknown_protocol_drops=re.findall(sama, show_interfaces_output) #RETURN 1 VALUE


    #CECI EST POUR LE INTERFACE PHYSIQUE 
    output_errors_collision_int_reset_intphy_regex=r'(\d+) output errors, (\d+) collisions, (\d+) interface resets'
    output_errors_collision_int_reset_intphy=re.findall(output_errors_collision_int_reset_intphy_regex, show_interfaces_output)
    output_errors_intphy=[]
    output_collision_intphy=[]
    interface_reste=[]
    for i in range(len(output_errors_collision_int_reset_intphy)):
        output_errors_intphy.append(output_errors_collision_int_reset_intphy[i][0])
        output_collision_intphy.append(output_errors_collision_int_reset_intphy[i][1])
        interface_reste.append(output_errors_collision_int_reset_intphy[i][2])



    #CECI EST POUR LES INTERFACE VLAN ILS N'ONT PAS LE MEME SORTIE 
    #QUE DANS LES INTERFACE PHYISUQE LIKE FastEthernet
    output_errors_int_reset__vlan_regex=r'(\d+) output errors, (\d+) interface resets'
    output_errors_int_reset_list_vlan=re.findall(output_errors_int_reset__vlan_regex,show_interfaces_output)
    ####HERE WE HAVE A PROBLEME 
    output_errors_vlan=[]
    int_reset_vlan=[]
    for i in range(len(output_errors_int_reset_list_vlan)):
        output_errors_vlan.append(output_errors_int_reset_list_vlan[i][0])
        int_reset_vlan.append(output_errors_int_reset_list_vlan[i][1])



    beta_vlan_regex=r' Received (\d+) broadcasts \((\d+) IP multicasts\)'
    beta_vlan=re.findall(beta_vlan_regex, show_interfaces_output) #RETURN 2 VALUES 
    #HERE WE HAVEEEE A PROBLEEEMMMME 
    Recevied_Brodacast_ipt_vlan=[]
    IPmulticasts_ipt_vlan=[]
    for i in range(len(beta_vlan)):          
        Recevied_Brodacast_ipt_vlan.append(beta_vlan[i][0])
        IPmulticasts_ipt_vlan.append(beta_vlan[i][1])


    beta_intphy_regex=r' Received (\d+) broadcasts \((\d+) IP multicasts\)'
    beta_intphy=re.findall(beta_intphy_regex, show_interfaces_output) #RETURN 2 VALUES 
    #HERE WE HAVEEEE A PROBLEEEMMMME 
    Recevied_Brodacast_ipt_intphy=[]
    IPmulticasts_ipt_intphy=[]
    for i in range(len(beta_vlan)):
        Recevied_Brodacast_ipt_intphy.append(beta_intphy[i][0])
        IPmulticasts_ipt_intphy.append(beta_intphy[i][1])


    #Regrouper dans une seule liste 
        
    listes_2=[interface_name,
              input_rate_bps,input_rate_pps,
              output_rate_bps,output_rate_pps,
              packet_out,packet_out_bytes,packet_out_underruns,
              packet_input_ipt,bytess_ipt,no_buffer_ipt,
              runts_ipt,gigants_ipt,throttles_ipt,
              input_errors_ipt,CRC_ipt,frame_ipt,overrun_ipt,ignored_input_ipt,
              otp_buffer_failures_otp,otp_buffer_swapped_otp,
              unknown_protocol_drops,
              output_errors_intphy,output_collision_intphy,interface_reste,
              output_errors_vlan,int_reset_vlan,
              Recevied_Brodacast_ipt_vlan,IPmulticasts_ipt_vlan,
              Recevied_Brodacast_ipt_intphy,IPmulticasts_ipt_intphy
              ]
    
    
    #derterminer la longueur de la liste la plus longue
    max_length_2 = max(len(l) for l in listes_2)

    for liste in listes_2:
        while len(liste) < max_length:
            liste.append(None)
    
    # Now you can create the NumPy array
    tableau_2 = np.array(listes_2).T
    df_2 = pd.DataFrame(tableau_2)
    df_2.columns = ['Interface',
                    'Input Rate bps','Input Rate pps',
                    'Output Rate bps','Output Rate pps',
                    'Packet Output','Packet Output Bytes','Packet Output Underruns',
                    'Packet Input','Packet Input Bytes','Packet Input No Buffer',
                    'Runts','Giants','Throttles',
                    'Input Errors','CRC','Frame','Overrun','Ignored Input',
                    'Output Buffer Failures','Output Buffers Swapped Out',
                    'Unknown Protocol Drops',
                    'Output Errors','Collisions','Interface Resets',
                    'Output Errors','Interface Resets',
                    'Received Brodcast Vlan Interface ','IP Multicasts Vlan Interface ',
                    'Received Brodcast Physical Interface','IP Multicasts Physical Interface'
                    ]
    
    print(df_2)
   


    #put the df_2 in ods ubuntu file
    df_2.to_csv('Interface_info.csv', index=False)
    

    net_connect.disconnect()
    return df_2


#get_interface_info_router_CISCO(device_type_input, ip_input, username_input, password_input, enable_secret_password_input)

#get_interface_info_switch_CISCO(device_type_input, ip_input, username_input, password_input, enable_secret_password_input)
