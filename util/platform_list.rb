result = []
DATA.each_line do |line|
  if line[0] == '*' && line.include?('[[')
    candidate = line[line.index('[[') + 2..line.index(']]') - 1].gsub(/[\s,\/]/, '-').gsub(/"/, '')
    if candidate.include? '|'
      candidate = candidate.split('|')[1]
    end
    result.push candidate.downcase unless candidate.nil?
  end
end

p result.uniq

__END__
source: https://en.wikipedia.org/wiki/List_of_operating_systems, retrieved on 17-12-2020


{{short description|Wikipedia list article}}
This is a '''list of operating systems'''. Computer [[operating system]]s can be categorized by technology, ownership, licensing, working state, usage, and by many other characteristics. In practice, many of these groupings may overlap. Criteria for inclusion is notability, as shown either through an existing Wikipedia article or citation to a reliable source.

==Proprietary==

===Acorn Computers===
* [[Arthur (operating system)|Arthur]]
* [[ARX (operating system)|ARX]]
* [[Acorn MOS|MOS]]
* [[RISC iX]]
* [[RISC OS]]

===Amiga Inc.===
* [[AmigaOS]]
**[[AmigaOS versions|AmigaOS 1.0-3.9]] (Motorola 68000)
** [[AmigaOS 4]] (PowerPC)
* [[Amiga Unix]] (a.k.a. Amix)

===Amstrad===
* [[AMSDOS]]
* [[Contiki]]
* [[CP/M 2.2]]
* [[CP/M Plus]]
* [[SymbOS]]

===Apple Inc.===
* [[Apple II]] family
** [[Apple DOS]]
** [[Apple Pascal]]
** [[ProDOS]]
** [[Apple GS/OS|GS/OS]]
** [[GNO/ME]]
**[[Contiki]]
* [[Apple III]]
** [[Apple SOS]]
* [[Apple Lisa]]
* [[Macintosh|Apple Macintosh]]
** [[Classic Mac OS]]
** [[A/UX]] ([[UNIX System V]] with [[BSD]] extensions)
** [[Copland (operating system)|Copland]]
** [[MkLinux]]
** [[Taligent|Pink]]
** [[Rhapsody (operating system)|Rhapsody]]
** [[macOS]] (formerly Mac OS X and OS X)
*** [[macOS Server]] (formerly Mac OS X Server and OS X Server)
* [[Apple Network Server]]
** [[IBM AIX]] (Apple-customized)
* [[Apple MessagePad]]
** [[Newton OS]]
* [[iPhone]] and [[Ipod touch|iPod Touch]]
**[[iOS]] (formerly iPhone OS)
*[[iPad]]
**[[iPadOS]]
* [[Apple Watch]]
** [[watchOS]]
* [[Apple TV]]
** [[tvOS]]
* Embedded operating systems
** [[A/ROSE]]
** [[iPod software]] (unnamed embedded OS for [[iPod]])
** Unnamed [[NetBSD]] variant for [[Airport Extreme]] and [[Time Capsule (Apple)|Time Capsule]]

===Apollo Computer===
* [[Domain/OS]] – One of the first network-based systems. Run on [[Apollo/Domain]] hardware. Later bought by [[Hewlett-Packard]].

===Atari===
* [[Atari DOS]] (for 8-bit computers)
* [[Atari TOS]]
* [[MultiTOS|Atari MultiTOS]]
*[[Contiki]] (for 8-bit, ST, Portfolio)

===BAE Systems===
* [[XTS-400]]

===Be Inc.===
* [[BeOS]]
** [[BeIA]]
** [[Dano (BeOS)|BeOS r5.1d0]]
*** [[magnussoft ZETA]] (based on [[Dano (BeOS)|BeOS r5.1d0]] source code, developed by [[yellowTAB]])

===Bell Labs===
* [[Unix]] ("Ken's new system," for its creator ([[Ken Thompson]]), officially Unics and then Unix, the prototypic operating system created in Bell Labs in 1969 that formed the basis for the [[List of Unix systems|Unix family]] of operating systems)
** UNIX Time-Sharing System v1
** UNIX Time-Sharing System v2
** UNIX Time-Sharing System v3
** UNIX Time-Sharing System v4
** UNIX Time-Sharing System v5
** [[Version 6 Unix|UNIX Time-Sharing System v6]]
*** MINI-UNIX
*** [[PWB/UNIX]]
**** USG
***** [[CB Unix]]
** [[Version 7 Unix|UNIX Time-Sharing System v7]] (It is from Version 7 Unix (and, to an extent, its descendants listed below) that almost all Unix-based and Unix-like operating systems descend.)
*** [[UNIX System III|Unix System III]]
*** Unix System IV
*** [[UNIX System V|Unix System V]]
**** Unix System V Releases 2.0, 3.0, 3.2, 4.0, and 4.2
** [[Version 8 Unix|UNIX Time-Sharing System v8]]
** [[Version 9 Unix|UNIX TIme-Sharing System v9]]
** [[Version 10 Unix|UNIX Time-Sharing System v10]]

Non-Unix Operating Systems:
* [[BESYS]]
* [[Plan 9 from Bell Labs]]
* [[Inferno (operating system)|Inferno]]

===Burroughs Corporation, Unisys===
* [[Burroughs MCP]]

===Commodore International===
*GEOS
**AmigaOS
***AROS Research Operating System
****Geoworks

===Control Data Corporation===
* [[Chippewa Operating System]] (COS)
** MACE (Mansfield and Cahlander Executive)
*** [[CDC Kronos|Kronos]] (Kronographic OS)
**** [[NOS (software)|NOS]] (Network Operating System)
***** NOS/BE NOS Batch Environment
***** NOS/VE NOS Virtual Environment
** [[CDC SCOPE|SCOPE]] (Supervisory Control Of Program Execution)
** SIPROS (for Simultaneous Processing Operating System){{Citation needed|date=April 2019}}
* EP/IX (Enhanced Performance Unix){{Citation needed|date=April 2019}}

===CloudMosa===
* [[Puffin OS]]

===Convergent Technologies===
* [[Convergent Technologies Operating System]] – later acquired by [[Unisys]]

===Cromemco===
* [[Cromemco DOS]] (CDOS) – a Disk Operating system compatible with [[CP/M]]
* [[Cromix]] – a multitasking, multi-user, [[Unix]]-like OS for [[Cromemco]] microcomputers with [[Zilog Z80|Z80A]] and/or [[Motorola 68000|68000]] CPU

===Data General===
* [[Data General AOS|AOS]] for 16-bit [[Data General Eclipse]] computers and [[Data General AOS|AOS/VS]] for 32-bit (MV series) Eclipses, MP/AOS for microNOVA-based computers
* [[DG/UX]]
* [[Data General RDOS|RDOS]] Real-time Disk Operating System, with variants: RTOS and DOS (not related to [[PC DOS]], [[MS-DOS]] etc.)

===Datapoint===
* CTOS Cassette Tape Operating System for the [[Datapoint 2200]]<ref>{{cite manual|url=http://bitsavers.org/pdf/datapoint/software/Datapoint_2200_Cassette_Tape_Operating_System_May1972.pdf|title=Datapoint 2200 Cassette Tape Operating System|date=May 1972|publisher=[[Datapoint]]}}</ref>
* DOS Disk Operating System for the Datapoint 2200, 5500, and 1100<ref>{{cite manual|url=http://bitsavers.org/pdf/datapoint/software/50127_Datapoint_DOS_UsersGuide_Feb75.pdf|title=Disk Operating System DOS. User's Guide|date=February 1975|publisher=[[Datapoint]]}}</ref>

===DDC-I, Inc.===
* [[Deos]] – Time & Space Partitioned RTOS, Certified to DO-178B, Level A since 1998
* [[HeartOS]] – POSIX-based Hard Real-Time Operating System

===Digital Research, Inc.===
* [[CP/M]]
** [[CP/M]] CP/M for [[Intel 8080]]/[[Intel 8085|8085]] and [[Zilog Z80]]
*** [[Personal CP/M]], a refinement of CP/M
*** [[CP/M Plus]] with BDOS 3.0
** [[CP/M-68K]] CP/M for [[Motorola 68000]]
** [[CP/M-8000]] CP/M for [[Zilog Z8000]]
** [[CP/M-86]] CP/M for [[Intel 8088]]/[[Intel 8086|8086]]
*** [[CP/M-86 Plus]]
*** [[Personal CP/M-86]]
** [[MP/M]] Multi-user version of CP/M-80
*** [[MP/M II]]
** [[MP/M-86]] Multi-user version of CP/M-86
*** [[MP/M 8-16]], a dual-processor variant of MP/M for 8086 and 8080 CPUs.
** [[Concurrent CP/M]], the successor of CP/M-80 and MP/M-80
** [[Concurrent CP/M-86]], the successor of CP/M-86 and MP/M-86
*** [[Concurrent CP/M 8-16]], a dual-processor variant of Concurrent CP/M for 8086 and 8080 CPUs.
** [[Concurrent CP/M-68K]], a variant for the 68000
* [[DOS]]
** [[Concurrent DOS]], the successor of Concurrent CP/M-86 with PC-MODE
*** [[Concurrent PC DOS]], a Concurrent DOS variant for IBM compatible PCs
*** [[Concurrent DOS 8-16]], a dual-processor variant of Concurrent DOS for 8086 and 8080 CPUs
*** [[Concurrent DOS 286]]
*** [[Concurrent DOS XM]], a real-mode variant of Concurrent DOS with EEMS support
*** [[Concurrent DOS 386]]
**** [[Concurrent DOS 386/MGE]], a Concurrent DOS 386 variant with advanced graphics terminal capabilities
** [[Concurrent DOS 68K]], a port of Concurrent DOS to Motorola 68000 CPUs with DOS source code portability capabilities
** [[FlexOS]] 1.0 – 2.34, a derivative of Concurrent DOS 286
*** [[FlexOS 186]], a variant of FlexOS for terminals
*** [[FlexOS 286]], a variant of FlexOS for hosts
**** [[Siemens S5-DOS/MT]], an industrial control system based on FlexOS
**** [[IBM 4680 OS]], a [[point of sale|POS]] operating system based on FlexOS
**** [[IBM 4690 OS]], a POS operating system based on FlexOS
***** [[Toshiba 4690 OS]], a POS operating system based on IBM 4690 OS and FlexOS
*** [[FlexOS 386]], a later variant of FlexOS for hosts
**** [[IBM 4690 OS]], a POS operating system based on FlexOS
***** [[Toshiba 4690 OS]], a POS operating system based on IBM 4690 OS and FlexOS
*** [[FlexOS 68K]], a derivative of Concurrent DOS 68K
** [[Multiuser DOS]], the successor of Concurrent DOS 386
*** [[CCI Multiuser DOS]]
*** [[Datapac Multiuser DOS]]
**** [[Datapac System Manager]], a derivative of Datapac Multiuser DOS
*** [[IMS Multiuser DOS]]
**** IMS [[REAL/32]], a derivative of Multiuser DOS
***** IMS [[REAL/NG]], the successor of REAL/32
** [[DOS Plus]] 1.1 – 2.1, a single-user, multi-tasking system derived from Concurrent DOS 4.1 – 5.0
** [[DR-DOS]] 3.31 – 6.0, a single-user, single-tasking native DOS derived from Concurrent DOS 6.0
*** Novell [[PalmDOS]] 1.0
*** Novell [[Star Trek project|"Star Trek"]]
*** [[Novell DOS]] 7, a single-user, multi-tasking system derived from DR DOS
*** Caldera [[OpenDOS]] 7.01
*** Caldera [[DR-DOS]] 7.02 and higher

===Digital Equipment Corporation, Tandem Computers, Compaq, Hewlett-Packard===
* [[DEC BATCH-11/DOS-11|Batch-11/DOS-11]]
* [[Domain/OS]] – originally ''Aegis'', from [[Apollo Computer]] who were bought by HP
* [[HP-UX]]
* [[HP Multi-Programming Executive|Multi-Programming Executive]] – from [[Hewlett-Packard|HP]]
* [[NonStop (server computers)|NonStop]]
* [[OS/8]]
* [[RSTS/E]] – multi-user time-sharing OS for [[PDP-11]]s
* [[RSX-11]] – multiuser, multitasking OS for PDP-11s
* [[RT-11]] – single user OS for PDP-11
* [[TOPS-10]] – for the PDP-10
* [[TENEX (operating system)|TENEX]] – an ancestor of [[TOPS-20]] from [[BBN Technologies|BBN]], for the PDP-10
* [[TOPS-20]] – for the PDP-10
* [[Tru64 UNIX|Digital UNIX]] – derived from OSF/1, became HP's [[Tru64 UNIX]]
* [[Ultrix]]
* [[OpenVMS|VMS]] – originally by [[Digital Equipment Corporation|DEC]] and HP now by VMS Software Inc.) for the [[VAX]] mini-computer range, [[DEC Alpha|Alpha]] and Intel [[Itanium 2|Itanium i2 and i4]]; later renamed OpenVMS
* [[WAITS]] – for the PDP-6 and PDP-10

===ENEA AB===
* [[Operating System Embedded|OSE]] – Flexible, small footprint, high-performance RTOS for control processors

===Fujitsu===
* [[Towns OS]]
* XSP
* [[OS/IV]]
* [[MSP (operating system)|MSP]]
* [[MSP-EX]]

=== General Electric, Honeywell, Bull ===
* [[Real-Time Multiprogramming Operating System]]
* [[General Comprehensive Operating System|GCOS]]
* [[Multics]]

===Google===
[[File:Android phones.jpg|upright|thumb|220px|[[Android (operating system)|Android OS]] on the [[Samsung Galaxy]] smartphones]]

* [[Chromium OS]] is an open source operating system development version of Chrome OS. Both operating systems are based on the [[Linux]] kernel.
** [[Chrome OS]] is designed to work exclusively with web applications. Announced on July 7, 2009, Chrome OS is currently publicly available and was released summer 2011. The Chrome OS source code was released on November 19, 2009, under the BSD license as Chromium OS.
** [[Container-Optimized OS]] (COS) is an operating system that is optimized for running Docker containers, based on [[Chromium OS]].<ref>{{cite web|url=https://cloud.google.com/container-optimized-os/docs|title=Container-Optimized OS from Google documentation|website=[[Google Cloud Platform]]}}</ref>
* [[Android (operating system)|Android]] is an operating system for mobile devices. It consists of [[Android Runtime]] (userland) with Linux (kernel), with its Linux kernel modified to add drivers for mobile device hardware and to remove unused Vanilla Linux drivers.
* [[gLinux]], a Linux distribution that Google uses internally
* [[Google Fuchsia|Fuchsia]] is a [[Capability-based operating system|capability-based]], [[Real-time operating system|real-time]], operating system (RTOS) [[Scalability|scalable]] to universal devices, in early development, from the tiniest [[Embedded system|embedded]] hardware, [[Smartwatch|wristwatches]], tablets to the largest personal computers. Unlike Chrome OS and Android, it is not based on the Linux kernel, but instead began on a new microkernel called "Zircon", derived from "Little Kernel".

===Green Hills Software===
* [[Integrity (operating system)|INTEGRITY]] – Reliable Operating system
* [[INTEGRITY-178B]] – A DO-178B certified version of [[Integrity (operating system)|INTEGRITY]].
* ''[[Green Hills Software#Real-time operating systems|u-velOSity]]'' – A lightweight [[microkernel]].

===Harris Corporation===
* [[Vulcan O/S]] – Proprietary O/S for Harris' Computer Systems (HCX)
* [[Harris UNIX]] – Proprietary UNIX based OS for Harris' Computers (MCX)

===Heathkit, Zenith Data Systems===
* [[HDOS]] – ran on the [[Heathkit H8|H8]] and Heath/[[Zenith Z-89]] series
* [[Heathkit H11#Specifications|HT-11]] – a modified version of [[RT-11]] that ran on the [[Heathkit H11]]

===Hewlett-Packard===
* [[HP Multi-Programming Executive]] (MPE, MPE/XL, and MPE/iX) – runs on HP 3000 and HP e3000 mini-computers
* [[HP-UX]] – runs on HP9000 and Itanium servers (from small to mainframe-class computers)
* [[NonStop OS]] – runs on HP's NonStop line of Itanium servers

===Honeywell===
* [[Honeywell CP-6|CP-6]]

===Huawei===
* [[Harmony OS]]

===Intel Corporation===
* [[RMX (operating system)|iRMX]] – real-time operating system originally created to support the Intel 8080 and 8086 processor families in embedded applications.
* [[ISIS (operating system)|ISIS]], [[ISIS-II]] – "Intel Systems Implementation Supervisor" was an environment for development of software within the Intel microprocessor family in the early 1980s on their [[Intellec]] Microcomputer Development System and clones. ISIS-II worked with 8&nbsp;inch floppy disks and had an editor, cross-assemblers, a linker, an object locator, debugger, compilers for [[PL/M]], a BASIC interpreter, etc. and allowed file management through a console.

===IBM===
{{further|History of IBM mainframe operating systems}}

====On early mainframes: 1400, 701, 704, 709, 7090, 7094====<!--IBM-->
* [[BESYS]] – for the [[IBM 7090]]
* [[Compatible Time-Sharing System]] (CTSS) – developed at MIT's Computation Center for use on a modified [[IBM 7094]]
* [[GM-NAA I/O|GM OS & GM-NAA I/O]] – for the [[IBM 704]]
* [[IBM 7090/94 IBSYS|IBSYS]] – tape based operating system for [[IBM 7090]] and [[IBM 7094]]
* [[IJMON]] – A bootable serial I/O monitor for loading programs for the [[IBM 1400 series]]{{cn|date=March 2019}}
* [[SHARE Operating System]] (SOS) – for the [[IBM 704]] and [[IBM 709|709]]
* [[University of Michigan Executive System]] (UMES) – for the [[IBM 704]], [[IBM 709|709]], and [[IBM 7090|7090]])

====On S/360, S/370, and successor mainframes====<!--IBM-->
* [[OS/360 and successors]] on IBM S/360, S/370, and successor mainframes
**[[OS/360]] (first official OS targeted for the [[System/360]] architecture)
*** PCP (Primary Control Program, a kernel and a ground breaking automatic space allocating file system)
*** [[MFT (operating system)|MFT]] (original Multi-programming with a Fixed number of Tasks, replaced by MFT II)
*** [[MFT (operating system)|MFT II]] (Multi-Programming with a Fixed number of Tasks, had up to 15 fixed size application partitions, plus partitions for system tasks, initially defined at boot time but redefinable by operator command)
*** [[Multiprogramming with a Variable number of Tasks|MVT]] (Multi-Programming Variable Tasks, had up to 15 application regions defined dynamically, plus additional regions for system tasks)
** OS/VS (port of OS/360 targeted for the [[System/370]] [[virtual memory]] architecture, ''"OS/370"'' is not correct name for OS/VS1 and OS/VS2, but rather refers to OS/VS2 MVS and MVS/SP Version 1),<br />Customer installations in the following variations:
*** SVS (Single Virtual Storage, both VS1 & VS2 began as SVS systems)
*** [[OS/VS1]] (Operating System/Virtual Storage 1, Virtual-memory version of MFT II)
*** OS/VS2 (Operating System/Virtual Storage 2, Virtual-memory version of OS/MVT but without multiprocessing support)
**** OS/VS2 R2 (called [[Multiple Virtual Storage]], MVS, eliminated most need for VS1)
** MVS/SE (MVS System Extensions)
** MVS/SP (MVS System Product)
** [[MVS/XA]] (MVS/SP V2. MVS supported eXtended Architecture, [[31-bit]] addressing)
** [[MVS/ESA]] (MVS supported Enterprise System Architecture, horizontal addressing extensions: data only address spaces called Dataspaces; a Unix environment was available starting with MVS/ESA V4R3)
** [[OS/390]] (Upgrade from MVS, with an additional [[Unix]] environment)
** [[Phoenix (computer)|Phoenix/MVS]] (Developed at [[Cambridge University]])
** [[z/OS]] (OS/390 supported [[z/Architecture]], [[64-bit]] addressing)
* [[DOS/360 and successors]] on IBM S/360, S/370, and successor mainframes
** [[BOS/360]] (early interim version of DOS/360, briefly available at a few Alpha & Beta System/360 sites)
** [[TOS/360]] (similar to BOS above and more fleeting, able to boot and run from 2x00 series tape drives)
** [[DOS/360]] (Disk Operating System (DOS), multi-programming system with up to 3 partitions, first commonly available OS for System/360)
*** DOS/360/RJE (DOS/360 with a control program extension that provided for the monitoring of remote job entry hardware (card reader & printer) connected by dedicated phone lines)
** [[DOS/VS]] (First DOS offered on System/370 systems, provided virtual storage)
** [[DOS/VSE]] (also known as VSE, upgrade of DOS/VS, up to 14 fixed size processing partitions )
** [[VSE/SP]] (program product replacing DOS/VSE and VSE/AF)
** VSE/ESA (DOS/VSE extended virtual memory support to 32-bit addresses (Extended System Architecture)).
** [[z/VSE]]  (latest version of the four decades old DOS lineage, supports 64-bit addresses, multiprocessing, multiprogramming, SNA, TCP/IP, and some virtual machine features in support of Linux workloads)
* [[CP/CMS]] (Control Program/Cambridge Monitor System) and successors on IBM S/360, S/370, and successor mainframes
** [[CP-40]]/CMS (for System/360 Model 40)
** [[CP-67]]/CMS (for System/360 Model 67)
** [[VM/370]] ([[Virtual machine|Virtual Machine]] / Conversational Monitor System, [[VM (operating system)|virtual memory operating system]] for System/370)
** [[VM (operating system)|VM/XA]]  (VM/eXtended Architecture for System/370 with extended virtual memory)
** VM/ESA ([[Virtual machine|Virtual Machine]] / Extended System Architecture, added 31-bit addressing to VM series)
** [[z/VM]] (z/Architecture version of the VM OS with 64-bit addressing)
{{further|History of CP/CMS}}
* TPF Line (Transaction Processing Facility) on IBM S/360, S/370, and successor mainframes (largely used by airlines)
** [[Airline Control Program|ACP]] (Airline Control Program)
** [[Transaction Processing Facility|TPF]] (Transaction Processing Facility)
** [[z/TPF]] ([[z/Architecture]] extension)
* [[Unix-like]] on IBM S/360, S/370, and successor mainframes
** [[IBM AIX#IBM mainframes|AIX/370]] (IBM's Advanced Interactive eXecutive, a System V Unix version)
** [[IBM AIX#IBM mainframes|AIX/ESA]] (IBM's Advanced Interactive eXecutive, a System V Unix version)
** [[OpenSolaris for System z]]
** [[UTS (Mainframe UNIX)|UTS]] (developed by Amdahl)
** [[Linux on IBM Z]]
* Others on IBM S/360, S/370, and successor mainframes:
** [[BOS/360]] (Basic Operating System)
** [[Michigan Terminal System|MTS]] (Michigan Terminal System, developed by a group of universities in the US, Canada, and the UK for the IBM System/360 Model 67, System/370 series, and compatible mainframes)
** RTOS/360 (IBM's Real Time Operating System, ran on 5 NASA custom System/360-75s)<ref>[http://dl.acm.org/citation.cfm?doid=1476793.1476796 "RTOS: extending OS/360 for real time spaceflight control"], J. L. Johnstone, in AFIPS '69 (Spring) Proceedings of the May 14–16, 1969, spring joint computer conference, pages 15-27.</ref>
** [[TOS/360]] (Tape Operating System)
** [[TSS/360]] (IBM's Time Sharing System)
** [[MUSIC/SP]] (developed by [[McGill University]] for IBM System/370)
** [[ORVYL and WYLBUR]] (developed by [[Stanford University]] for IBM System/360)

====On PC and Intel x86 based architectures====<!--IBM-->
* [[PC DOS]], IBM DOS
** PC DOS 1.x, 2.x, 3.x (developed jointly with Microsoft)
** IBM DOS 4.x, 5.0 (developed jointly with Microsoft)
** PC DOS 6.1, 6.3, 7, 2000, 7.10
{{See also|List of operating systems#Microsoft Corporation|l1=MS-DOS and Windows}}
* [[OS/2]]
** OS/2 1.x (developed jointly with Microsoft)
** OS/2 2.x
** [[OS/2 Warp]] 3 (ported to PPC via [[Workplace OS]])
** [[OS/2 Warp]] 4
** [[eComStation]] (Warp 4.5/Workspace on Demand, rebundled by Serenity Systems International)
** [[ArcaOS]] (Warp 4.52 based system sold by Arca Noae, LLC)
* [[IBM 4680 OS]] version 1 to 4, a [[point of sale|POS]] operating system based on [[Digital Research]]'s [[Concurrent DOS 286]] and [[FlexOS 286]] 1.xx
** [[IBM 4690 OS]] version 1 to 6.3, a successor to 4680 OS based on [[Novell]]'s [[FlexOS 286]]/[[FlexOS 386]] 2.3x
*** [[Toshiba 4690 OS]] version 6.4, a successor to 4690 OS 6.3
* [[Unix-like]] on [[IBM Personal System/2|PS/2]]
** [[IBM AIX#IBM PS/2 series|AIX]] (IBM's Advanced Interactive eXecutive, a System V Unix version)

====On other hardware platforms====<!--IBM-->
* [[IBM Series/1]]
** [[IBM Series/1#Software support|EDX]] ([[Event Driven Executive]])
** [[IBM Series/1#Software support|RPS]] (Realtime Programming System)
** [[IBM Series/1#Software support|CPS]] (Control Programming Support, subset of RPS)
** [[SerIX]] (Unix on Series/1)
* [[IBM 1130]]
** [[IBM 1130#Operating procedure|DMS]] (Disk Monitor System)
* [[IBM 1800]]
** [[IBM 1800 TSX|TSX]] (Time Sharing eXecutive)
** [[IBM 1800 MPX|MPX]] (Multi Programming eXecutive)
* [[IBM 8100]]
** [[IBM 8100 DPCX|DPCX]] (Distributed Processing Control eXecutive)
** [[IBM 8100 DPPX|DPPX]] (Distributed Processing Programming Executive)
* [[IBM System/3]]
** DMS (Disk Management System)
* [[IBM System/34]], [[IBM System/36]]
** SSP (System Support Program)
* [[IBM System/38]]
** [[IBM System/38#Features|CPF]] (Control Program Facility)
* [[IBM System/88]]
** [[Stratus VOS]] (developed by [[Stratus Technologies|Stratus]], and used for IBM [[System/88]], [[Original equipment manufacturer]] from Stratus)
* [[IBM System i|AS/400]], iSeries, System i, Power Systems i Edition
** [[IBM i|OS/400]] (descendant of [[System/38]] CPF, include [[System/36]] SSP environment)
** [[i5/OS]] (extends [[OS/400]] with significant interoperability features)
** [[IBM i]] (extends [[i5/OS]])
* [[UNIX]] on [[IBM RT PC]]
** [[Academic Operating System|AOS]] (a BSD Unix version, not related to [[Data General]] AOS)
** [[IBM AIX#IBM RT PC|AIX]] (Advanced Interactive eXecutive, a System V Unix version)
* [[UNIX]] on [[IBM POWER Instruction Set Architecture|POWER ISA]], [[PowerPC]], and [[Power ISA]]
** [[IBM AIX#POWER ISA/PowerPC/Power ISA-based systems|AIX]] (Advanced Interactive eXecutive, a System V Unix version)
* Others
** [[Workplace OS]] (a [[Microkernel]] based operating system including OS/2, developed and canceled in the 1990s)
** [[K42]] (open-source research operating system on [[PowerPC]] or [[x86]] based cache-coherent multiprocessor systems)
** [[Dynix]] (developed by [[Sequent Computer Systems|Sequent]], and used for IBM [[NUMA-Q]] too)

===International Computers Limited===
* [[J (operating system)|J]] and [[MultiJob]] – for the System 4 series mainframes
* [[GEORGE (operating system)|GEORGE]] 2/3/4 GEneral ORGanisational Environment – used by [[International Computers Limited|ICL]] [[ICT 1900 series|1900 series]] mainframes
* [[Executive (operating system)|Executive]] – used on the 1900 and 290x range of minicomputers. A modified version of Executive was also used as part of GEORGE 3 and 4.
* [[TME (operating system)|TME]] – used on the ME29 minicomputer
* [[ICL VME]] – including early variants VME/B and VME/2900, appearing on the [[ICL 2900 Series]] and Series 39 mainframes, implemented in [[S3 programming language|S3]]
* [[VME/K]] – on early smaller 2900s

===Jide===
*[[Remix OS]]

===Lynx Real-time Systems, LynuxWorks, Lynx Software Technologies===
* [[LynxOS]]

===Micrium Inc.===
* [[MicroC/OS-II]]  – small pre-emptive priority based multi-tasking kernel
* [[MicroC/OS-III]] – small pre-emptive priority based multi-tasking kernel, with unlimited number of tasks and priorities, and round robin scheduling

===Microsoft Corporation===
* [[Xenix]] (licensed version of Unix; licensed to [[Santa Cruz Operation|SCO]] in 1987)
* [[MSX-DOS]] (developed by MS Japan for the MSX 8-bit computer)
* [[MS-DOS]] (developed jointly with IBM, versions 1.0–6.22)
* [[DOS/V]]
*[[OS/2]] 1.x (developed jointly with IBM until version 1.3)
* [[Microsoft Windows|Windows]] (16-bit and 32-bit preemptive and cooperative multitasking, running atop MS-DOS)
** [[Windows 1.0]] (Windows 1)
** [[Windows 2.0]] (Windows 2 – separate version for i386 processor)
** [[Windows 3.0]] (Windows 3)
** [[Windows 3.1x]] (Windows 3.1)
** [[Windows for Workgroups 3.1]] (Codename Snowball)
** [[Windows 3.2]] (Chinese-only release)
** [[Windows for Workgroups 3.11]]
** [[Windows 95]] (codename Chicago – Windows 4.0)
** [[Windows 98]] (codename Memphis – Windows 4.1)
** [[Windows ME|Windows Millennium Edition]] (Windows ME – Windows 4.9)
* [[Windows NT]] (Full 32-bit or 64-bit kernel, not dependent on MS-DOS)
** [[Windows NT 3.1]]
** [[Windows NT 3.5]]
** [[Windows NT 3.51]]
** [[Windows NT 4.0]]
** [[Windows 2000]] (Windows NT 5.0)
** [[Windows XP]] (Windows NT 5.1)
** [[Windows Server 2003]] (Windows NT 5.2)
** [[Windows Fundamentals for Legacy PCs]] (based on Windows XP)
** [[Windows Vista]] (Windows NT 6.0)
** [[Windows Azure]] (Cloud OS Platform) 2009
** [[Windows Home Server]] (based on Windows Server 2003)
** [[Windows Server 2008]] (based on Windows Vista)
** [[Windows 7]] (Windows NT 6.1)
** [[Windows Phone 7]]
** [[Windows Server 2008 R2]] (based on Windows 7)
** [[Windows Home Server 2011]] (based on Windows Server 2008 R2)
** [[Windows Server 2012]] (based on Windows 8)
** [[Windows 8]] (Windows NT 6.2)
** [[Windows Phone 8]]
** [[Windows 8.1]] (Windows NT 6.3)
** [[Windows Phone 8.1]]
** [[Windows Server 2012 R2]] (based on Windows 8.1)
** [[Xbox One system software]]
** [[Windows 10]] (Windows NT 10)
** [[Windows 10 Mobile]]
** [[Windows Server 2016]]
** [[Windows Server 2019]]
* [[Windows CE]] (OS for handhelds, embedded devices, and real-time applications that is similar to other versions of Windows)
** [[Windows CE 3.0]]
** [[Windows CE 5.0]]
** [[Windows CE 6.0]]
** [[Windows Embedded Compact 7]]
** [[Windows Embedded Compact 2013]]
** [[Windows Mobile]] (based on Windows CE, but for a smaller form factor)
* [[Singularity (operating system)|Singularity]] – A research operating system written mostly in [[managed code]] ([[C Sharp (programming language)|C#]])
* [[Midori (operating system)|Midori]] – A managed code operating system
* [[Xbox 360 system software]]
* [[Xbox One system software]]
* [[Azure Sphere]]
* [[ThreadX]]

===MITS===
* [[Altair DOS]] – An early disk operating system for the [[Altair 8800]] machine.{{Citation needed|date=April 2019}}

===MontaVista===
* MontaVista [[Mobilinux]]

===NCR Corporation===
* [[Transaction Management eXecutive|TMX]] – Transaction Management eXecutive
* [[IMOS]] – Interactive Multiprogramming Operating System (circa 1978), for the NCR Century 8200 series minicomputers{{Citation needed|date=April 2019}}
* [[NCR VRX|VRX]] – Virtual Resource eXecutive

===Nintendo===
* [[ES (operating system)|ES]] is a computer operating system developed originally by Nintendo and since 2008 by Esrille. It is open source and runs natively on x86 platforms.

===NeXT===
* [[NeXTSTEP]]

===Novell===
* [[NetWare]] – network operating system providing high-performance network services. Has been superseded by Open Enterprise Server line, which can be based on NetWare or Linux to provide the same set of services.
* [[UnixWare]]
** [[Novell "SuperNOS"]] – a never released merge of NetWare and UnixWare
* [[Novell "Corsair"]]
** [[Novell "Expose"]]
* [[Open Enterprise Server]] – the successor to NetWare

===Quadros Systems===
* [[RTXC Quadros]] RTOS – proprietary C-based RTOS used in embedded systems

===RCA===
* [[Time Sharing Operating System]] (TSOS) – first OS supporting virtual addressing of the main storage and support for both timeshare and batch interface

===RoweBots===
* [[DSPnano RTOS]] – 8/16 Bit Ultra Tiny Embedded Linux Compatible RTOS

===Samsung Electronics===
* [[Bada]]
* [[Tizen]] is an operating system based on the Linux kernel, a project within the Linux Foundation and is governed by a Technical Steering Group (TSG) while controlled by Samsung and backed by Intel. Tizen works on a wide range of Samsung devices including smartphones, tablets, smart TVs, PCs and wearable.

===SCO, SCO Group<ref>{{cite web| url = http://williambader.com/museum/dell/xenixhistory.html| title = SCO History by William Bader| access-date = 2010-03-12 }}</ref>===
* [[Xenix]], Unix System III based distribution for the Intel 8086/8088 architecture
** [[Xenix]] 286, Unix System V Release 2 based distribution for the Intel 80286 architecture
** [[Xenix]] 386, Unix System V Release 2 based distribution for the Intel 80386 architecture
* [[SCO OpenServer|SCO Unix]], SCO UNIX System V/386 was the first volume commercial product licensed by AT&T to use the UNIX System trademark (1989). Derived from AT&T System V Release 3.2 with an infusion of Xenix device drivers and utilities plus most of the SVR4 features
** [[SCO Open Desktop]], the first 32-bit graphical user interface for UNIX Systems running on Intel processor-based computers. Based on [[SCO OpenServer|SCO Unix]]
* [[SCO OpenServer]] 5, AT&T UNIX System V Release 3 based
* [[SCO OpenServer]] 6, SVR5 (UnixWare 7) based kernel with SCO OpenServer 5 application and binary compatibility, system administration, and user environments
* [[UnixWare]]
** [[UnixWare]] 2.x, based on AT&T System V Release 4.2MP
** [[UnixWare]] 7, UnixWare 2 kernel plus parts of 3.2v5 (UnixWare 2 + OpenServer 5 = UnixWare 7). Referred to by [[Santa Cruz Operation|SCO]] as SVR5

===Scientific Data Systems (SDS)===
* [[Berkeley Timesharing System]] for the [[SDS 940]]

===SYSGO===
* [[PikeOS]] – a certified real time operating system for safety and security critical embedded systems

===Tandy Corporation===
* [[TRSDOS]] – A floppy-disk-oriented OS supplied by Tandy/Radio Shack for their [[TRS-80]] Z80-based line of personal computers. Eventually renamed as LS-DOS or LDOS.
* [[Color BASIC]] – A ROM-based OS created by Microsoft for the [[TRS-80 Color Computer]].{{citation needed|date=May 2017}}
* [[NewDos/80]] – A third-party OS for Tandy's TRS-80 personal computers.
* [[DeskMate]] – Operating system created by Tandy Corporation and introduced with the [[Tandy 1000]] computer.{{citation needed|date=May 2017}}

===TCSC (later NCSC)===
* [[Edos]] – enhanced version of IBM's [[DOS/360]] (and later [[DOS/VS]] and [[DOS/VSE]]) operating system for [[System/360]] and [[System/370]] IBM mainframes

===Texas Instruments===
* [[TI-RTOS|TI-RTOS Kernel]] – Real-time operating system for TI's embedded devices.

===TRON Project===
* [[TRON Project|TRON]] – open [[real-time operating system]] [[Kernel (computing)|kernel]]
* [[T-Kernel]]

===UNIVAC, Unisys===
* [[UNIVAC EXEC I|EXEC I]]
* [[UNIVAC EXEC II|EXEC II]]
* [[EXEC 8]]/OS 1100/[[OS 2200]]
* [[VS/9]], successor to [[Time Sharing Operating System|RCA TSOS]]

===Wang Laboratories===
* [[Wang Laboratories#Word processors|WPS]] Wang Word Processing System. Micro-code based system.
* [[Wang Laboratories#Wang OIS|OIS]] Wang Office Information System. Successor to the WPS. Combined the WPS and VP/MVP systems.

===Wind River Systems===
* [[VxWorks]] – Small footprint, scalable, high-performance RTOS for embedded microprocessor based systems.<ref name="windriver.com">{{cite web|url=http://www.windriver.com/products/vxworks/|title=VxWorks|website=www.windriver.com}}</ref>

===Zilog===
* [[Z80-RIO]]

===Zorin Group===
* [[Zorin OS]]

===Other===

====Lisp-based====
* [[Lisp Machines|Lisp Machines, Inc.]] (also known as LMI) used an operating system written in [[MIT]]'s [[Lisp Machine Lisp]].
* [[Symbolics]] [[Genera (operating system)|Genera]] written in a systems dialect of the [[Lisp (programming language)|Lisp]] programming language called [[ZetaLisp]] and Symbolics [[Common Lisp]]. Genera was ported to a virtual machine for the [[DEC Alpha]] line of computers.
* [[Texas Instruments]]' Explorer [[Lisp machine]] workstations also had systems code written in [[Lisp Machine Lisp]].
* [[Xerox]] 1100 series of Lisp machines used an operating system also written in [[Interlisp]], and was also ported to a virtual machine called "Medley."

====For Elektronika BK====
*[[ANDOS]]
*[[CSI-DOS]]
*[[MK-DOS]]

====Non-standard language-based====
* [[Pilot (operating system)|Pilot]] operating system – written in the [[Mesa (programming language)|Mesa]] and used in [[Xerox Star]] workstations
* [[PERQ]] Operating System (POS) – written in PERQ [[Pascal (programming language)|Pascal]]

====Other proprietary non-Unix-like====
* [[Elbrus]] THIS LINE HAS BEEN EDITED IN FAVOR OF THE NON-UNICODE CHARACTERS IT ORIGINALLY CONTAINS --> [[Elbrus (computer)|Эльбрус-1 (Elbrus-1)]] and Эльбрус-2 – used for application, job control, system programming,<ref>{{cite web|url=http://www.ixbt.com/cpu/e2k-spec.html |title=Эльбрус Бабаяна и Pentium Пентковского |publisher=Ixbt.com |access-date=2013-09-21}}</ref>  implemented in [[AL-76 programming language|uЭль-76 (AL-76)]].
* [[EOS (operating system)|EOS]] – developed by [[ETA Systems]] for use in their [[ETA-10]] line of [[supercomputer]]s
* EMBOS – developed by [[Elxsi]] for use on their [[mini-supercomputer]]s
* [[General Comprehensive Operating System|GCOS]] – a proprietary Operating System originally developed by [[General Electric]]
* [[MAI Basic Four]] – An OS implementing [[Business Basic]] from MAI Systems.
* [[Michigan Terminal System]] – Developed by a group of universities in the US, Canada, and the UK for use on the IBM System/360 Model 67, the System/370 series, and compatible mainframes
* [[MUSIC/SP]] – an operating system developed for the S/370, running normally under VM
* OS ES – an operating system for [[ES EVM]]
* [[PC-MOS/386]] – DOS-like, but multiuser/multitasking
* Prolog-Dispatcher – used to control Soviet [[Buran (spacecraft)|Buran]] space ship.
* [[SINTRAN III]] – an operating system used with [[Norsk Data]] computers.
* [[SkyOS]] – commercial desktop OS for PCs
* [[SODA (operating system)|SODA]] – used by the [[Odra (computer)|Odra 1204]] computers.<ref>{{cite journal|url=http://comjnl.oxfordjournals.org/cgi/content/abstract/11/2/148|title=SODA—A Dual Activity Operating System|author=Władysław M. Turski|journal=[[The Computer Journal]]|year=1968|volume=11|issue=2|pages=148–156|doi=10.1093/comjnl/11.2.148|doi-access=free}}</ref>
* [[THEOS]]
* [[TSX-32]] – a 32-bit operating system for x86 platform.
* TX990/TXDS, [[DX10]] and DNOS – proprietary operating systems for [[TI-990]] minicomputers

====Other proprietary Unix-like and POSIX-compliant====
* [[Domain/OS|Aegis]] ([[Apollo Computer]])
* [[Amiga Unix]] (Amiga ports of Unix System V release 3.2 with Amiga A2500UX and SVR4 with Amiga A3000UX. Started in 1990, last version was in 1992)
* [[Coherent (operating system)|Coherent]] ([[Unix-like]] OS from Mark Williams Co. for PC class computers)
* [[DC/OSx]] (DataCenter/OSx&mdash;an operating system developed by [[Pyramid Technology]] for its [[MIPS architecture|MIPS]]-based systems)
* [[DG/UX]] (Data General Corp)
* [[DNIX]] from [[DIAB]]
* [[DSPnano RTOS]] (POSIX nanokernel, DSP Optimized, Open Source)
* [[HeliOS]] developed and sold by [[Perihelion Software]] mainly for [[transputer]]-based systems
* [[Interactive Unix]] (a [[porting|port]] of the [[UNIX System V]] [[operating system]] for [[x86|Intel x86]] by [[Interactive Systems Corporation]])
* [[IRIX]] from [[Silicon Graphics|SGI]]
* [[MeikOS]]
* [[NeXTSTEP]] (developed by [[NeXT]]; a Unix-based OS based on the [[Mach (kernel)|Mach]] microkernel)
* [[OS-9]] [[Unix-like]] [[Real-time operating system|RTOS]]. (OS from [[Microware]] for [[Motorola 6809]] based microcomputers)
* OS9/68K [[Unix-like]] [[Real-time operating system|RTOS]]. (OS from [[Microware]] for [[Motorola 68000 series|Motorola 680x0]] based microcomputers; based on [[OS-9]])
* [[OS-9000]] [[Unix-like]] [[Real-time operating system|RTOS]]. (OS from [[Microware]] for [[Intel]] x86 based microcomputers; based on [[OS-9]], written in [[C (programming language)|C]])
* [[OSF/1]] (developed into a commercial offering by [[Digital Equipment Corporation]])
* [[OpenStep]]
* [[QNX]] (POSIX, microkernel OS; usually a real time embedded OS)
* [[Rhapsody (operating system)|Rhapsody]] (an early form of Mac OS X)
* [[RISC iX]] – derived from BSD 4.3, by Acorn computers, for their [[ARM architecture|ARM]] family of machines
* [[MIPS RISC/os|RISC/os]] (a port by [[MIPS Technologies]] of [[4.3BSD]] for its [[MIPS architecture|MIPS]]-based computers)
* [[RMX (operating system)|RMX]]
* [[SCO UNIX]] (from [[Santa Cruz Operation|SCO]], bought by Caldera who renamed themselves [[SCO Group]])
* [[SINIX]] (a port by [[Siemens Nixdorf Informationssysteme|SNI]] of [[Unix]] to the [[MIPS architecture]])
* [[Solaris (operating system)|Solaris]] (from Sun, bought by Oracle; a System V-based replacement for SunOS)
* [[SunOS]] (BSD-based Unix system used on early Sun hardware)
* [[SUPER-UX]] (a port of [[UNIX System V|System V Release 4.2MP]] with features adopted from [[Berkeley Software Distribution|BSD]] and [[Linux]] for [[NEC SX architecture]] [[supercomputer]]s)
* [[UNIX System V|System V]] (a release of AT&T Unix, 'SVR4' was the 4th minor release)
* [[Microport (software)|System V/AT, 386]] (The first version of AT&T System V UNIX on the IBM 286 and 386 PCs, ported and sold by [[Microport (software)|Microport]])
* [[Trusted Solaris]] (Solaris with kernel and other enhancements to support [[multilevel security]])
* [[UniFLEX]] ([[Unix-like]] OS from [[Technical Systems Consultants|TSC]] for DMA-capable, extended addresses, Motorola 6809 based computers; e.g. [[SWTPC]], [[GIMIX]] and others)
* [[Unicos]] (the version of Unix designed for Cray Supercomputers, mainly geared to vector calculations)
* UTX-32 (Developed by Gould CSD (Computer System Division), a Unix-based OS that included both BSD and System V characteristics. It was one of the first Unix based systems to receive NSA's C2 security level certification.){{Citation needed|date=April 2019}}
* [[Zenix]], Zenith corporations Unix (a popular USA electronics maker at the time){{Citation needed|date=April 2019}}

== Non-proprietary ==

===Unix or Unix-like===

* [[MINIX]] (study OS developed by [[Andrew S. Tanenbaum]] in the [[Netherlands]])
* [[Berkeley Software Distribution|BSD]] (Berkeley Software Distribution, a variant of Unix for [[Digital Equipment Corporation|DEC]] [[VAX]] hardware)
** [[FreeBSD]] (one of the outgrowths of UC Regents' abandonment of [[CSRG]]'s 'BSD Unix')
*** [[DragonFlyBSD]], forked from FreeBSD 4.8
*** [[MidnightBSD]], forked from FreeBSD 6.1
*** [[GhostBSD]]
*** [[TrueOS]] (previously known as PC-BSD)
** [[NetBSD]] (an embedded device BSD variant)
*** [[OpenBSD]] forked from NetBSD
**** [[Bitrig]] forked from OpenBSD
** [[Darwin (operating system)|Darwin]], created by Apple using code from NeXTSTEP, FreeBSD, and NetBSD
*[[GNU]] (also known as GNU/Hurd)
* [[Linux]] (see also [[List of Linux distributions]]) (alleged to be GNU/Linux<ref>{{Cite web|url=https://www.gnu.org/gnu/gnu-linux-faq.en.html|title=gnu.org|website=www.gnu.org|language=en|access-date=2018-08-24}}</ref> see [[GNU/Linux naming controversy]])
* [[Redox (operating system)|Redox]] (written in Rust)<ref>{{cite web|url=http://www.redox-os.org/|title=Redox - Your Next(Gen) OS - Redox - Your Next(Gen) OS|website=www.redox-os.org}}</ref>
*[[Android (operating system)|Android]]<ref>{{Cite web|url=https://www.linuxfoundation.org/blog/2012/12/video-what-a-year-for-linux/|title=Video: What a Year for Linux|website=[[The Linux Foundation]]|date=2012-12-13|access-date=2020-06-30}}</ref>
**[[Android-x86]]
***[[Remix OS]]
* [[Cray Linux Environment]]
*[[OpenSolaris]]
**[[illumos]], contains original Unix (SVR4) code derived from the [[OpenSolaris]] (discontinued by Oracle in favor of [[Solaris (operating system)|Solaris]] 11 Express)
***[[OpenIndiana]], operates under the illumos Foundation. Uses the illumos kernel, which is a derivative of [[OS/Net]], which is basically an [[OpenSolaris]]/[[Solaris (operating system)|Solaris]] kernel with the bulk of the drivers, core libraries, and basic utilities.
***[[Nexenta OS]], based on the illumos kernel with Ubuntu packages
***[[SmartOS]], an illumos distribution for cloud computing with [[Kernel-based Virtual Machine]] integration.
* [[RTEMS]] (Real-Time Executive for Multiprocessor Systems)
* [[Haiku (operating system)|Haiku]] (open source inspired by [[BeOS]], under development)
* [[Syllable Desktop]]
* [[VSTa]]
* [[Plurix]] (or Tropix<ref>{{Cite web|url=http://www.tropix.nce.ufrj.br/|title=TROPIX: Distribuição e Instalação|website=www.tropix.nce.ufrj.br|access-date=2018-08-24}}</ref>) (By [[Federal University of Rio de Janeiro]] - UFRJ)
* [[TUNIS]] (University of Toronto)
* [[dahliaOS]] - dahliaOS is a modern, secure, lightweight and responsive operating system, combining the best of GNU/Linux and Fuchsia OS.

===Non-Unix===

* [[Cosmos (operating system)|Cosmos]] – written in C#
* [[FreeDOS]] – open source DOS variant
* [[Genode]] – operating system framework for microkernels (written in C++)
* [[Ghost (operating system)|Ghost OS]] – written in Assembly, C/C++
* [[Incompatible Timesharing System|ITS]] – written by [[Massachusetts Institute of Technology|MIT]] students (for the [[PDP-6]] and [[PDP-10]]) (written in MIDAS)
* [[OS/2#Future|osFree]] – OS/2 Warp open source clone.
* [[OSv]] – written in C++
* [[Phantom OS]] – persistent object oriented
* [[ReactOS]] – open source OS designed to be binary compatible with [[Windows NT]] and its variants ([[Windows XP]], [[Windows 2000]], etc.); currently in development phase
* [[SharpOS (operating system)|SharpOS]] – written in .NET C#
* [[TempleOS]] – written in HolyC
* [[Visopsys]] – written by Andy McLaughlin (written in C and Assembly)

== Research ==

=== Unix or Unix-like ===
* [[Plan 9 from Bell Labs]] – distributed OS developed at [[Bell Labs]], based on original Unix design principles yet functionally different and going much further
** [[Inferno (operating system)|Inferno]] – distributed OS derived from Plan 9, originally from Bell Labs
* [[Research Unix]]<ref>{{Cite web|url=http://www.tuhs.org/Archive/Caldera-license.pdf|title=Caldera license|date=2002-01-23|access-date=2019-01-29}}</ref><ref>{{Cite web|url=http://www.lemis.com/grog/UNIX/|title=UNIX is free!|website=www.lemis.com|access-date=2018-08-24}}</ref>

=== Non-Unix ===
*[[Amoeba distributed operating system|Amoeba]] – research OS by [[Andrew S. Tanenbaum]]
*[[Croquet Project|Croquet]]
*[[Extremely Reliable Operating System|EROS]] – microkernel, capability-based
**[[CapROS]] – microkernel EROS successor
*[[Harmony (operating system)|Harmony]] - realtime, multitasking, multiprocessing message-passing system developed at the National Research Council of Canada.
*[[HelenOS]] – research and experimental operating system
*[[House (operating system)|House]] – Haskell User's Operating System and Environment, research OS written in Haskell and C
*[[ILIOS]] – Research OS designed for routing
*[[L4 microkernel family|L4]] – second generation microkernel
*[[Mach kernel|Mach]] – from OS kernel research at [[Carnegie Mellon University]]; see [[NeXTSTEP]]
*[[Nemesis (computing)|Nemesis]] – Cambridge University research OS – detailed quality of service abilities
*[[Singularity (operating system)|Singularity]] — experimental OS from Microsoft Research written in [[managed code]] to be highly [[Dependability|dependable]]
*[[Spring (operating system)|Spring]] – research OS from Sun Microsystems
*[[THE multiprogramming system]] – by Dijkstra in 1968, at the [[Eindhoven University of Technology]] in the Netherlands, introduced the first form of software-based memory segmentation, freeing programmers from being forced to use actual physical locations
*[[Thoth (operating system)|Thoth]] - realtime, multiprocess message-passing system developed at the [[University of Waterloo]].
*[[V (operating system)|V]] – from Stanford, early 1980s<ref name="capabook">{{cite web|url=http://homes.cs.washington.edu/~levy/capabook/Chapter7.pdf|title=Capability-Based Computer Systems|publisher=Cs.washington.edu|access-date=2013-09-21}}</ref>
*[[Verve (operating system)|Verve]] — OS designed by Microsoft Research to be verified end-to-end for [[type safety]] and [[memory safety]]
*[[Xinu]] – Study OS developed by [[Douglas E. Comer]] in the United States<ref>"Despite its name suggesting some similarity to Unix, Xinu is a different type of operating system, written with no knowledge of the Unix source code, or compatibility goals. It uses different abstractions, and [[system call]]s, some with names matching those of Unix, but different semantics."
Garfinkel, Simson; Spafford, Gene; Schwartz, Alan (2003). Practical UNIX and Internet Security. O'Reilly. p. 19.</ref>

==Disk operating systems (DOS)==
{{Main|DOS}}
* [[86-DOS]] (developed at Seattle Computer Products by Tim Paterson for the new Intel 808x CPUs; licensed to [[Microsoft]], became PC DOS/MS-DOS. Also known by its working title QDOS.)
** [[PC DOS]] (IBM's DOS variant, developed jointly with Microsoft, versions 1.0–7.0, 2000, 7.10)
** [[MS-DOS]] (Microsoft's DOS variant for OEM, developed jointly with IBM, versions 1.x–6.22 Microsoft's now abandoned DOS variant)
* [[Concurrent CP/M-86]] 3.1 (BDOS 3.1) with [[PC-MODE]] (Digital Research's successor of [[CP/M-86]] and [[MP/M-86]])
** [[Concurrent DOS]] 3.1-4.1 (BDOS 3.1-4.1)
*** [[Concurrent PC DOS]] 3.2 (BDOS 3.2) (Concurrent DOS variant for IBM compatible PCs)
**** [[DOS Plus]] 1.1, 1.2 (BDOS 4.1), 2.1 (BDOS 5.0) (single-user, multi-tasking system derived from Concurrent DOS 4.1-5.0)
*** [[Concurrent DOS 8-16]] (dual-processor variant of Concurrent DOS for 8086 and 8080 CPUs)
*** [[Concurrent DOS 286]] 1.x
**** [[FlexOS]] 1.00-2.34 (derivative of Concurrent DOS 286)
***** [[FlexOS 186]] (variant of FlexOS for terminals)
***** [[FlexOS 286]] (variant of FlexOS for hosts)
****** [[Siemens S5-DOS/MT]] (industrial control system based on FlexOS)
****** [[IBM 4680 OS]] ([[point of sale|POS]] operating system based on FlexOS)
****** [[IBM 4690 OS]] (POS operating system based on FlexOS)
******* [[Toshiba 4690 OS]] (POS operating system based on IBM 4690 OS and FlexOS)
***** [[FlexOS 386]] (later variant of FlexOS for hosts)
****** [[IBM 4690 OS]] (POS operating system based on FlexOS)
******* [[Toshiba 4690 OS]] (POS operating system based on IBM 4690 OS and FlexOS)
*** [[Concurrent DOS 386]] 1.0, 1.1, 2.0, 3.0 (BDOS 5.0-6.2)
**** [[Concurrent DOS 386/MGE]] (Concurrent DOS 386 variant with advanced graphics terminal capabilities)
**** [[Multiuser DOS]] 5.0, 5.01, 5.1 (BDOS 6.3-6.6) (successor of Concurrent DOS 386)
***** [[CCI Multiuser DOS]] 5.0-7.22 (up to BDOS 6.6<!-- at least for 7.22 -->)
***** [[Datapac Multiuser DOS]]
****** [[Datapac System Manager]] 7 (derivative of Datapac Multiuser DOS)
***** [[IMS Multiuser DOS]] 5.1, 7.0, 7.1 (BDOS 6.6-6.7)
****** IMS [[REAL/32]] 7.50, 7.51, 7.52, 7.53, 7.54, 7.60, 7.61, 7.62, 7.63, 7.70, 7.71, 7.72, 7.73, 7.74, 7.80, 7.81, 7.82, 7.83, 7.90, 7.91, 7.92, 7.93, 7.94, 7.95 (BDOS 6.8 and higher) (derivative of Multiuser DOS)
******* IMS [[REAL/NG]] (successor of REAL/32)
*** [[Concurrent DOS XM]] 5.0, 5.2, 6.0, 6.2 (BDOS 5.0-6.2) (real-mode variant of Concurrent DOS with EEMS support)
**** [[DR-DOS|DR DOS]] 3.31, 3.32, 3.33, 3.34, 3.35, 5.0, 6.0 (BDOS 6.0-7.1) single-user, single-tasking native DOS derived from Concurrent DOS 6.0)
***** Novell [[PalmDOS]] 1 (BDOS 7.0)
***** Novell [[DR DOS "StarTrek"]]
***** [[Novell DOS]] 7 (single-user, multi-tasking system derived from DR DOS, BDOS 7.2)
****** Novell DOS 7 updates 1-10 (BDOS 7.2)
******* Caldera [[OpenDOS]] 7.01 (BDOS 7.2)
******** Enhanced DR-DOS 7.01.0x (BDOS 7.2)
********* Dell Real Mode Kernel (DRMK)
****** Novell DOS 7 updates 11-15.2 (BDOS 7.2)
******* Caldera [[DR-DOS]] 7.02-7.03 (BDOS 7.3)
******** [[DR-DOS "WinBolt"]]
******** OEM DR-DOS 7.04-7.05 (BDOS 7.3)
******** OEM DR-DOS 7.06 (PQDOS)
******** OEM DR-DOS 7.07 (BDOS 7.4/7.7)
* [[FreeDOS]] ([[open-source software|open source]] DOS variant)
* [[ProDOS]] (operating system for the [[Apple II]] series computers)
* [[PTS-DOS]] (DOS variant by [[Russia]]n company [[Phystechsoft]])
* [[TurboDOS]] (Software 2000, Inc.) for [[Z80]] and [[Intel 8086]] processor-based systems
* Multi-tasking user interfaces and environments for DOS
** [[DESQview]] + [[QEMM 386]] multi-tasking user interface for DOS
** DESQView/X ([[X Window System|X-windowing]] GUI for DOS)

==Network operating systems==
{{Main|Network operating system}}
* [[Banyan VINES]] – by [[Banyan Systems]]
* [[Cambridge Ring (computer network)|Cambridge Ring]]
* [[Cisco IOS]] – by Cisco Systems
*[[Cisco NX-OS]] – previously SAN-OS
* [[CTOS]] – by [[Convergent Technologies (Unisys)|Convergent Technologies]], later acquired by [[Unisys]]
* [[Data ONTAP]] – by [[NetApp]]
* [[ExtremeWare]] – by [[Extreme Networks]]
* [[ExtremeXOS]] – by [[Extreme Networks]]
* [[Fabric OS]] – by [[Brocade Communications Systems|Brocade]]
* [[JunOS]] – by Juniper
* [[NetWare]] – networking OS by [[Novell]]
* [[Network operating system]] (NOS) – developed by [[Control Data Corporation|CDC]] for use in their Cyber line of supercomputers
* [[Novell Open Enterprise Server]] – Open Source networking OS by [[Novell]]. Can incorporate either [[SUSE Linux]] or Novell NetWare as its kernel
* [[Plan 9 from Bell Labs|Plan 9]] – distributed OS developed at [[Bell Labs]], based on Unix design principles but not functionally identical
**[[Inferno (operating system)|Inferno]] – distributed OS derived from Plan 9, originally from Bell Labs
* [[TurboDOS]] – by Software 2000, Inc.

==Generic, commodity, and other==
* [[BLIS/COBOL]]
* [[Bluebottle OS|Bluebottle]] also known as AOS (a concurrent and active object update to the [[Oberon operating system]])
* [[BS1000]] by [[Siemens|Siemens AG]]
* [[BS2000]] by [[Siemens|Siemens AG]], now [[BS2000/OSD]] from [[Fujitsu-Siemens Computers]] (formerly [[Siemens Nixdorf Informationssysteme]])
* [[BS3000]] by [[Siemens|Siemens AG]] (functionally similar to OS-IV and MSP from Fujitsu)
*[[Contiki]] for various, mostly 8-bit systems, including the [[Apple II series]], the [[Atari 8-bit family]], and some [[Commodore International|Commodore]] machines.
* [[FLEX9]] (by [[Technical Systems Consultants|TSC]] for Motorola 6809 based machines; successor to [[FLEX (operating system)|FLEX]], which was for Motorola 6800 CPUs)
* [[Graphics Environment Manager|GEM]] (windowing GUI for CP/M, DOS, and [[Atari]] TOS)
* [[GEOS (8-bit operating system)|GEOS]] (popular windowing GUI for PC, Commodore, Apple computers)
* [[JavaOS]]
* [[JNode]] (Java New Operating System Design Effort), written 99% in Java (native compiled), provides own JVM and JIT compiler. Based on [[GNU Classpath]].<ref>[http://www.osnews.com/story/20911/JNode_0_2_8_Released "JNode 0.2.8 Released"], Thom Holwerda, OSNews, 4 February 2009.</ref><ref>[http://www.jnode.org/ Jnode: Java New Operating System Design Effort], jnode.org. Retrieved 24 July 2014.</ref>
* [[JX (operating system)|JX]] Java operating system that focuses on a flexible and robust operating system architecture developed as an open source system by the University of Erlangen.
* [[KERNAL]] (default OS on Commodore 64)
* [[MERLIN (operating system)|MERLIN]] for the [[Corvus Concept]]
* [[MorphOS]] (Amiga compatible)
* MSP by [[Fujitsu]] (successor to OS-IV), now MSP/EX,<ref>{{cite web|url=http://www.fujitsu.com/downloads/GSRVR/msp.pdf |title=Fujitsu Extended System Architecture (EXA) Operating System|publisher=Fujitsu.com|access-date=2013-09-21}}</ref> also known as Extended System Architecture (EXA), for 31-bit mode
* [[NetWare]] (networking OS by [[Novell]])
* [[Oberon (operating system)]] (developed at ETH-Zürich by [[Niklaus Wirth]] et al.) for the Ceres and Chameleon workstation projects
* [[OSD/XC]] by [[Fujitsu-Siemens]] (BS2000 ported to an emulation on a Sun SPARC platform)
* [[OS-IV]] by [[Fujitsu]] (based on early versions of IBM's [[MVS]])
* [[Pick operating system|Pick]] (often licensed and renamed)
* [[PRIMOS]] by [[Prime Computer]] (sometimes spelled PR1MOS and PR1ME)
* [[Sinclair QDOS]] (multitasking for the [[Sinclair QL]] computer)
* [[SSB-DOS]] (by [[Technical Systems Consultants|TSC]] for Smoke Signal Broadcasting; a variant of [[FLEX (operating system)|FLEX]] in most respects)
* [[SymbOS]] (GUI based multitasking operating system for [[Z80]] computers)
* [[Symobi]] (GUI based modern micro-kernel OS for [[x86]], [[ARM architecture|ARM]] and [[PowerPC]] processors, developed by Miray Software; used and developed further at [[Technical University of Munich]])
* [[TripOS]], 1978
* [[TurboDOS]] (Software 2000, Inc.)
* [[UCSD Pascal|UCSD p-System]] (portable complete programming environment/operating system/virtual machine developed by a long running student project at [[UCSD]]; directed by Prof [[Kenneth Bowles]]; written in [[Pascal programming language|Pascal]])
* [[Stratus VOS|VOS]] by [[Stratus Technologies]] with strong influence from [[Multics]]
* [[VOS3 (operating system)|VOS3]] by [[Hitachi, Ltd.|Hitachi]] for its IBM-compatible mainframes, based on IBM's [[MVS]]
* [[VM2000]] by [[Siemens AG]]
* [[Visi On]] (first GUI for early PC machines; not commercially successful)
* [[VPS/VM]] (IBM based, main operating system at [[Boston University]] for over 10 years.)

==Hobby==
* [[AROS]] – AROS Research Operating System (formerly known as Amiga Research Operating System)
* [[AtheOS]] – branched to become [[Syllable Desktop]]
** [[Syllable Desktop (operating system)|Syllable Desktop]] – a modern, independently originated OS; see [[AtheOS]]
* [[BareMetal]]
* [[DexOS]] – 32-bit operating system written in x86 assembly
* [[DSPnano RTOS]]
* [[EmuTOS]]
* [[EROS (microkernel)|EROS]] – Extremely Reliable Operating System
* [[HelenOS]] – based on a preemptible microkernel design
* [[LSE/OS]]
* [[MenuetOS]] – extremely compact OS with [[GUI]], written entirely in [[FASM]] assembly language
** [[KolibriOS]] – a fork of MenuetOS
* [[ToaruOS]]
** [[ToaruOS#PonyOS|PonyOS]]
* [[SerenityOS]]

==Embedded==
<!-- This section is linked from [[Embedded operating system]] -->

=== Mobile operating systems ===
See also [[Mobile operating system|Mobile Operating systems]]

*[[DIP DOS]] on [[Atari Portfolio]]
*[[Embedded Linux]] (see also [[Linux for mobile devices]])
**[[Android (operating system)|Android]]
***[[Replicant (operating system)|Replicant]]
***[[LineageOS]]
***See also [[List of custom Android distributions]]
**[[Firefox OS]]
**[[Angstrom distribution]]
**[[Familiar Linux]]
**[[Maemo]] based on [[Debian]] deployed on [[Nokia]]'s [[Nokia 770]], [[Nokia N800|N800]] and [[Nokia N810|N810]] Internet Tablets.
**[[OpenZaurus]]
**[[webOS]] from [[Palm, Inc.]], later [[Hewlett-Packard]] via acquisition, and most recently at [[LG Electronics]] through acquisition from Hewlett-Packard<ref>{{cite web|url=http://www8.hp.com/us/en/hp-news/press-release.html?id=1375489 |title=HP News - LG Electronics Acquires webOS from HP to Enhance Smart TV |publisher=.hp.com |date=2013-02-25 |access-date=2013-09-21}}</ref>
**[[Access Linux Platform]]
**[[bada]]
**[[Openmoko Linux]]
**[[OPhone]]
**[[MeeGo]] (from merger of
*[[Maemo]] &
*[[Moblin]] )
**[[Mobilinux]]
**[[MotoMagx]]
**[[Qt Extended]]
**[[Sailfish OS]]
**[[Tizen]] (earlier called [[LiMo Platform]])
**[[Ubuntu Touch]]
**[[PostmarketOS]]
*[[Inferno (operating system)|Inferno]] (distributed OS originally from [[Bell Labs]])
*[[Magic Cap]]
*[[MS-DOS]] on [[Poqet PC]], [[HP 95LX]], [[HP 100LX]], [[HP 200LX]], [[HP 1000CX]], [[HP OmniGo 700LX]]
*[[NetBSD]]
*[[Newton OS]] on [[Apple MessagePad]]
*[[Palm OS]] from Palm, Inc; now spun off as PalmSource
*[[PEN/GEOS]] on [[HP OmniGo 100]] and [[HP OmniGo 120|120]]
*[[PenPoint OS]]
*[[Plan 9 from Bell Labs]]
*[[Pocket viewer|PVOS]]
*[[Symbian OS]]
**[[EPOC (operating system)|EPOC]]
*[[Windows CE]], from Microsoft
**[[Pocket PC]] from Microsoft, a variant of Windows CE
**[[Windows Mobile]] from Microsoft, a variant of Windows CE
**[[Windows Phone]] from Microsoft
*[[DSPnano RTOS]]
*[[iOS]]
**[[watchOS]]
**[[tvOS]]
*[[iPod software]]
*[[iPodLinux]]
*[[iriver clix]] OS
*[[RockBox]]
*[[BlackBerry OS]]
*[[PEN/GEOS]], [[GEOS-SC]], [[GEOS-SE]]
*[[Palm OS]]
*[[Symbian platform]]
*[[Symbian OS]]
*[[BlackBerry 10]]

===Routers===
* [[CatOS]] – by [[Cisco Systems]]
* [[Cisco IOS]] – originally Internetwork Operating System by [[Cisco Systems]]
* [[Inferno (operating system)|Inferno]] – distributed OS originally from [[Bell Labs]]
* [[IOS-XR]] – by [[Cisco Systems]]
* [[JunOS]] – by [[Juniper Networks]]
* LCOS – by [[LANCOM Systems]]<ref>{{Cite web|title=LCOS Data-Sheet|url=https://www.lancom-systems.com//download/documentation/Data_Sheets/DS_LCOS-1040_EN.pdf}}</ref>
* [[Linux]]
** [[OpenWrt]]
*** [[DD-WRT]]
*** [[LEDE]]
*** [[Gargoyle (router firmware)|Gargoyle]]
*** [[LibreCMC]]
**[[Zeroshell]]
* [[RTOS]] – by Force10 Networks
* FreeBSD
** [[m0n0wall]]
** [[OPNsense]]
** [[PfSense|pfsense]]
[[List of wireless router firmware projects]]

===Other embedded===
* [[Apache Mynewt]]
* [[ChibiOS/RT]]
* [[Contiki]]
* [[ERIKA Enterprise]]
* [[eCos]]
* [[NetBSD]]
* [[Nucleus RTOS]]<ref>{{cite web|url=https://www.mentor.com/embedded-software/nucleus/|title=Mentor Nucleus RTOS}}</ref>
* [[NuttX]]
* [[MINIX]]
* [[NCOS]]
* [[freeRTOS|freeRTOS, openRTOS and safeRTOS]]
* [[OpenEmbedded]] (or [[Yocto Project]])
* [[PSOS (real-time operating system)|pSOS]] (Portable Software On Silicon)
* [[QNX]] – Unix-like real-time operating system, aimed primarily at the embedded systems market.<ref>{{cite web|url=http://www.qnx.com/|title=QNX operating systems, development tools, and professional services for connected embedded systems|website=www.qnx.com}}</ref>
* [[REX OS]] – microkernel OS; usually an embedded cell phone OS
* [[RIOT (operating system)|RIOT]]
* [[ROM-DOS]]
* [[TinyOS]]
* [[ThreadX]]
* [[RT-Thread]]
* [[DSPnano RTOS]]
* [[Windows IoT]]
* [[Windows Embedded]]
** [[Microsoft Windows CE|Windows CE]]
** Windows IoT Core
** Windows IoT Enterprise
* Wind River [[VxWorks]] – Small footprint, scalable, high-performance RTOS for embedded microprocessor based systems.<ref name="windriver.com"/>
* [[Wombat OS]] – microkernel OS; usually a real time embedded OS
* [[Zephyr (operating system)|Zephyr]]

===LEGO Mindstorms===
* [[brickOS]]
* [[leJOS]]

==Capability-based==
* [[Cambridge CAP computer]] – operating system demonstrated the use of security capabilities, both in hardware and software, also a useful fileserver, implemented in [[ALGOL 68C]]
* [[Flex machine]] – Custom microprogrammable hardware, with an operating system, (modular) compiler, editor, * garbage collector and filing system all written in [[ALGOL 68]].
* [[Hydra (operating system)|HYDRA]] – Running on the [[C.mmp]] computer at [[Carnegie Mellon University]], implemented in the programming language [[BLISS]]<ref>{{cite web|title=Reflections in a pool of processors - An experience report on C.mmp/Hydra|url=https://www.cs.auckland.ac.nz/courses/compsci703s1c/resources/WulfHarbison.pdf|page=945|first1=William A.|last1=Wulf|first2=Samual P.|last2=Harbison|publisher=University of Auckland|access-date=2013-09-21}}</ref>
* [[KeyKOS]] nanokernel
**[[Extremely Reliable Operating System|EROS]] microkernel
***[[CapROS]] EROS successor
* [[V (operating system)|V]] – from Stanford, early 1980s<ref name="capabook"/>