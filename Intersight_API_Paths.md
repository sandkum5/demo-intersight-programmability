# Intersight API Paths

**Format**  Object Name : `Intersight API Path`
**Complete Path Creation**
* `https://intersight.com/api/v1/<path>`
* E.g. For UCS Server Profiles, the complete URL for SAAS would be:
  * `https://intersight.com/api/v1/server/Profiles`
  * For PVA/CVA, replace `intersight.com` with the `FQDN/IP` of the Intersight Private/Connected Virtual Appliance

## Profiles
* UCS Server Profiles       `server/Profiles`
* UCS Domain Profiles       `fabric/SwitchClusterProfiles`
* UCS Chassis Profiles      `chassis/Profiles`
* HX Cluster Profiles       `hyperflex/ClusterProfiles`


## Templates
* Templates	                `server/ProfileTemplates`

## Policies
### Server Policies
* Adapter Configuration	    `adapter/ConfigPolicies`
* BIOS	                    `bios/Policies`
* Boot Order	            `boot/PrecisionPolicies`
* Certificate Management	`certificatemanagement/Policies`
* Device Connector	        `deviceconnector/Policies`
* Drive Security	        `storage/DriveSecurityPolicies`
* Ethernet Adapter	        `vnic/EthAdapterPolicies`
* Ethernet Network	        `vnic/EthNetworkPolicies`
* Ethernet Network Control	`fabric/EthNetworkControlPolicies`
* Ethernet Network Group  	`fabric/EthNetworkGroupPolicies`
* Ethernet QoS	            `vnic/EthQosPolicies`
* FC Zone	                `fabric/FcZonePolicies`
* Fibre Channel Adapter	    `vnic/FcAdapterPolicies`
* Fibre Channel Network	    `vnic/FcNetworkPolicies`
* Fibre Channel QoS	        `vnic/FcQosPolicies`
* Firmware	                `firmware/Policies`
* IMC Access	            `access/Policies`
* IPMI Over LAN	            `ipmioverlan/Policies`
* iSCSI Adapter	            `vnic/IscsiAdapterPolicies`
* iSCSI Boot	            `vnic/IscsiBootPolicies`
* iSCSI Static Target	    `vnic/IscsiStaticTargetPolicies`
* LAN Connectivity	        `vnic/LanConnectivityPolicies`
  * VNICs	                `vnic/EthIfs`
* LDAP	                    `iam/LdapPolicies`
* Local User	            `iam/EndPointUserPolicies`
* Network Connectivity      `networkconfig/Policies`
* NTP                       `ntp/Policies`
* Persistent Memory	        `memory/PersistentMemoryPolicies`
* Power	                    `power/Policies`
* SAN Connectivity	        `vnic/SanConnectivityPolicies`
  * VHBAs	                `vnic/FcIfs`
* SD Card	                `sdcard/Policies`
* Serial Over LAN	        `sol/Policies`
* SMTP	                    `smtp/Policies`
* SNMP	                    `snmp/Policies`
* SSH	                    `ssh/Policies`
* Storage	                `storage/StoragePolicies`
* Syslog	                `syslog/Policies`
* Thermal	                `thermal/Policies`
* Virtual KVM	            `kvm/Policies`
* Virtual Media	            `vmedia/Policies`


### Domain Policies
* Ethernet Network Control	`fabric/EthNetworkControlPolicies`
* Ethernet Network Group	`fabric/EthNetworkGroupPolicies`
* Flow Control	            `fabric/FlowControlPolicies`
* Link Aggregation	        `fabric/LinkAggregationPolicies`
* Link Control	            `fabric/LinkControlPolicies`
* Multicast Policy	        `fabric/MulticastPolicies`
* Network Connectivity	    `networkconfig/Policies`
* NTP	                    `ntp/Policies`
* Port	                    `fabric/PortPolicies`
* SNMP	                    `snmp/Policies`
* Switch Control	        `fabric/SwitchControlPolicies`
* Syslog	                `syslog/Policies`
* System QoS	            `fabric/SystemQosPolicies`
* VLAN                    	`fabric/Vlans`
* VSAN                    	`fabric/Vsans`

### Chassis Policies
* IMC Access	            `access/Policies`
* Power     	            `power/Policies`
* SNMP	                    `snmp/Policies`
* Thermal   	            `thermal/Policies`

### HyperFlex Policies
* Auto Support                     	`hyperflex/AutoSupportPolicies`
* Backup                           	`hyperflex/ClusterBackupPolicies`
* DNS,NTP and Timezone             	`hyperflex/SysConfigPolicies`
* External FC Storage              	`hyperflex/ExtFcStoragePolicies`
* External iSCSI Storage           	`hyperflex/ExtIscsiStoragePolicies`
* HTTP Proxy                       	`hyperflex/ProxySettingPolicies`
* Network Configuration            	`hyperflex/ClusterNetworkPolicies`
* Node IP Ranges                   	`hyperflex/NodeConfigPolicies`
* Replication Network Configuration	`hyperflex/ClusterReplicationNetworkPolicies`
* Security                         	`hyperflex/LocalCredentialPolicies`
* Storage Configuration            	`hyperflex/ClusterStoragePolicies`
* vCenter                          	`hyperflex/VcenterConfigPolicies`

### Pools
* IP Pool	    `ippool/Pools`
* IQN	        `iqnpool/Pools`
* MAC	        `macpool/Pools`
* Resource	    `resourcepool/Pools`
* UUID	        `uuidpool/Pools`
* WWNN	        `fcpool/Pools`
* WWPN

## ADDITIONAL APIS
* Requests  	   `workflow/WorkflowInfos`
* Alarms    	   `cond/Alarms`
* Advisories
	* `tam/SecurityAdvisories`
	* `tam/AdvisoryInfos`
	* `tam/AdvisoryDefinitions`
	* `tam/AdvisoryInstances`

## Admin
* API                 	`iam/ApiKeys`
* Webhooks            	`notification/AccountSubscriptions`
* Resource Groups     	`resource/Groups`
* Organization        	`organization/Organizations`
* IP Access Management	`iam/IpAccessManagements`
* Security & Privacy
	* `kvm/TunneledKvmPolicies`
	* `techsupportmanagement/CollectionControlPolicies`
* Notifications  	    `notification/AccountSubscriptions`
* Domain Names   	    `iam/DomainNameInfos`
* Account Details	    `iam/Accounts`
* Targets             	`asset/Targets`
* Tech Support Bundles	`techsupportmanagement/TechSupportBundles`
* Audit Logs          	`aaa/AuditRecords`
* Licensing           	`license/LicenseInfos`
* UCS Director        	`iaas/UcsdInfos`

## Software Repository
* Firmware Links        	`firmware/Distributables`
* OS Image Links        	`softwarerepository/OperatingSystemFiles`
* SCU Links             	`firmware/ServerConfigurationUtilityDistributables`
* OS Configuration Files	`os/ConfigurationFiles`

## Operate
* All Servers	                    `compute/PhysicalSummaries`
    * C-series                      `compute/RackUnits`
    * B-series                      `compute/Blades`
* Chassis	                        `equipment/Chasses`
* Fabric Interconnects	            `fabric/ElementIdentities`
* Networking	                    `network/ElementSummaries`
* HyperFlex Clusters	            `hyperflex/Clusters`
* Storage	                        `search/SearchItems?$filter=(IndexMotypes eq storage.BaseArray)`
* Virtualization	                `search/SearchItems?$filter=(IndexMotypes eq virtualization.BaseCluster) and (ObjectType ne hyperflex.Cluster)&$expand=Datacenter($select=Name)`
