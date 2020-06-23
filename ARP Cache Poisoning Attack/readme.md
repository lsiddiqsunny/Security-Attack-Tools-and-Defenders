# ARP Cache Poisoning Attack

**Address Resolution Protocol (ARP) poisoning** is when an attacker sends falsified ARP messages over a local area network (LAN) to link an attacker’s MAC address with the IP address of a legitimate computer or server on the network.

Once the attacker’s MAC address is linked to an authentic IP address, the attacker can receive any messages directed to the legitimate MAC address. As a result, the attacker can intercept, modify or block communicates to the legitimate MAC address.

## What is ARP

**Address Resolution Protocol (ARP)** is a protocol that enables network communications to reach a specific device on the network. ARP translates Internet Protocol (IP) addresses to a Media Access Control (MAC) address, and vice versa. Most commonly, devices use ARP to contact the router or gateway that enables them to connect to the Internet.

Hosts maintain an ARP cache, a mapping table between IP addresses and MAC addresses, and use it to connect to destinations on the network. If the host doesn’t know the MAC address for a certain IP address, it sends out an ARP request packet, asking other machines on the network for the matching MAC address.

The ARP protocol was not designed for security, so it does not verify that a response to an ARP request really comes from an authorized party. It also lets hosts accept ARP responses even if they never sent out a request. This is a weak point in the ARP protocol, which opens the door to ARP spoofing attacks.

![ARP Working](.\assests\d8f138_9e82523f8ff044e6ace39eb0e2e0079e.webp)

## Attack Plan

An ARP spoofing, also known as ARP poisoning, is a **Man in the Middle (MitM) attack** that allows attackers to intercept communication between network devices. The attack works as follows:

1. The attacker must have access to the network. They scan the network to determine the IP addresses of at least two devices⁠—let’s say these are a workstation and a router.
2. The attacker uses a spoofing tool, such as Arpspoof or Driftnet, to send out forged ARP responses.
3. The forged responses advertise that the correct MAC address for both IP addresses, belonging to the router and workstation, is the attacker’s MAC address. This fools both router and workstation to connect to the attacker’s machine, instead of to each other.
4. The two devices update their ARP cache entries and from that point onwards, communicate with the attacker instead of directly with each other.
5. The attacker is now secretly in the middle of all communications.

![ARP Cache Poisoning](.\assests\attack_image.webp)

## Attack Result

- **Continue routing the communications** as-is⁠—the attacker can sniff the packets and steal data, except if it is transferred over an encrypted channel like HTTPS.
- **Perform session hijacking⁠**—if the attacker obtains a session ID, they can gain access to accounts the user is currently logged into.
- **Alter communication**⁠—for example pushing a malicious file or website to the workstation.
- **Distributed Denial of Service (DDoS)**⁠—the attackers can provide the MAC address of a server they wish to attack with DDoS, instead of their own machine. If they do this for a large number of IPs, the target server will be bombarded with traffic.

## Attack Detection

Here is a simple way to detect that a specific device’s ARP cache has been poisoned, using the command line. Start an operating system shell as an administrator. Use the following command to display the ARP table, on both Windows and Linux:

```cpp
arp -a
```

Output should be something like this:

```cpp
Internet Address    Physical Address

192.168.5.1        00-14-22-01-23-45
192.168.5.201      40-d4-48-cr-55-b8
192.168.5.202      00-14-22-01-23-45
```

If the table contains two different IP addresses that have the same MAC address, this indicates an ARP attack is taking place. Because the IP address 192.168.5.1 can be recognized as the router, the attacker’s IP is probably 192.168.5.202.

To discover ARP spoofing in a large network and get more information about the type of communication the attacker is carrying out, you can use the open source **Wireshark** protocol.

## Prevention

- **Use a Virtual Private Network (VPN)⁠**—a VPN allows devices to connect to the Internet through an encrypted tunnel. This makes all communication encrypted, and worthless for an ARP spoofing attacker.
- **Use static ARP⁠**—the ARP protocol lets you define a static ARP entry for an IP address, and prevent devices from listening on ARP responses for that address. For example, if a workstation always connects to the same router, you can define a static ARP entry for that router, preventing an attack.
- **Use packet filtering⁠**—packet filtering solutions can identify poisoned ARP packets by seeing that they contain conflicting source information, and stop them before they reach devices on your network.
- **Run a spoofing attack⁠**—check if your existing defenses are working by mounting a spoofing attack, in coordination with IT and security teams. If the attack succeeds, identify weak points in your defensive measures and remediate them.

## Example

Here is an example of ARP Cache Poisoning: [ARP Cache Poisoning](https://medium.com/datadriveninvestor/arp-cache-poisoning-using-scapy-d6711ecbe112)

## Resources

- [imperva](https://www.imperva.com/learn/application-security/arp-spoofing/)
- [comparitech](https://www.comparitech.com/blog/vpn-privacy/arp-poisoning-spoofing-detect-prevent/)
- [wixsite](https://paragtailor.wixsite.com/infosec/single-post/2015/05/08/ARP-Cache-Poisoning-Attack-with-IP-Forwarding)
  