#!/usr/bin/python3
#Automating nmap with hackersploit..
import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<---------------------------------------------->")

ip_address = input("Please enter the IP adress you want to scan: ")
print("The IP adress is: ",ip_address)

option=input(""" \n Please enter the type of scan you want to run
             1)SYN ACK Scan
             2)UDP Scan
             3)Comprehensive Scan\n""")
print("You have selected option: ",option)

if option == '1':
    print("Nmap version:",scanner.nmap_version())
    scanner.scan(ip_address, '1-100','-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ",scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open ports:",scanner[ip_address]['tcp'].keys())