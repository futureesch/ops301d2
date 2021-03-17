ops301d2 - reading 08

https://www.nakivo.com/blog/virtualbox-network-setting-guide/ 

VirtualBox VMs have up to eight virtual network adapters, called network interface controllers (NIC). All virtual network adapters (up to 8) can be configured with the VBoxManage modifyvm command. 

Industry standard: Paravirtualized Network Adapter (virtio-net). “instead of virtualizing networking hardware that is supported by most operating systems, a guest operating system must provide a special software interface for virtualized environments.” This obviates the need to correctly set up an emulated hardware network.

Network Modes:
Not attached - simulates the act of physically plugging and unplugging the ethernet cable from the switch/router
NAT - default, isolated networks with default DHCP set to 10.0.2.2. Default IP for VM would be set 10.0.2.15
NAT Network - allows VMs to share the level so as to be able to communicate without strange port-forwarding rules
“The default address of the NatNetwork is 10.0.2.0/24.
The default gateway IP is 10.0.2.1 (the x.x.x.1 template is used to assign the default gateway IP).”
Bridged Adapter - “can be used to run servers on VMs that must be fully accessible from a physical local area network. When using the bridged network mode in VirtualBox, you can access a host machine, hosts of the physical network and external networks, including internet from a VM. The VM can be accessed from the host machine and from other hosts (and VMs) connected to the physical network.
the IP address of a VM virtual network adapter can belong to the same network as the IP address of the physical network adapter of the host machine when the bridged mode is used.”
Promiscuous mode “makes it possible for a physical network adapter to have multiple MAC addresses, allowing all incoming traffic to pass the physical network adapter of the host machine and reach the virtual network adapter of the VM which has its own MAC address that is represented on the host adapter, even if that traffic is not addressed to the virtual network adapter of that particular VM.”
Internal Network - Might be better thought of as an isolated network, ideal for simulating a network at large. 
“Network configuration used in this example:
VM1. IP address – 192.168.23.1 (internal network mode); 10.0.2.15 (NAT mode), gateway 10.0.2.2 (the IP address of the built-in VirtualBox NAT device).
VM2. IP address – 192.168.23.2 (internal network), gateway – 192.168.23.1
VM3. IP address – 192.168.23.3 (internal network), gateway – 192.168.23.1
VirtualBox internal network subnet: 192.168.23.0/24”
Host-only adapter - been using this all class.
Generic Driver
Port Forwarding
