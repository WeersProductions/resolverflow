from pyspark.sql import SparkSession
from pyspark.sql.functions import array, array_intersect, col, expr, lit, size, split, when


def tag_info_df(spark):
    """ Extract features from the tags of a post

    Args:
        spark (SparkSession): used to run queries and commands

    Returns:
        DataFrame: With columns [
            (post)_Id,
            number_of_tags,
            contains_language_tag,
            contains_platform_tag
        ]
    """
    language_list = ["abap", "abc", "actionscript", "ada", "algol", "algol 58", "algol 60", "algol w", "algol 68",
                     "alice", "amiga e", "apex", "apl", "applescript", "argh!", "aargh!", "assembly",
                     "assembly language", "autolisp", "autolt", "awk",
                     "b", "bash", "basic", "ballerina", "bbc basic", "bc", "bcpl", "blitz basic", "bourne shell",
                     "brainfuck",
                     "c", "c++", "c#", "cfml", "cl", "classic visual basic", "clean", "clipper", "clojure", "cobol",
                     "comal", "common lisp", "coffeescript", "crystal", "c shell", "ct",
                     "d", "darkbasic", "dart", "decimal basic", "delphi", "delta cobol", "div games studio",
                     "egl", "eiffel", "elixir", "elm", "emacs lisp", "erlang", "euphoria",
                     "f#", "factor", "fenix project", "forth", "fortran", "foxpro",
                     "gambas", "gcl", "gml", "go", "grasshopper", "groovy",
                     "hack", "haskell", "hypertalk",
                     "icon", "inform", "io", "ironpython",
                     "j", "just another language", "java", "javascript", "just basic", "jscript", "julia",
                     "korn shell", "kotlin",
                     "labview", "ladder logic", "leet", "liberty basic", "lisp", "logo", "lua",
                     "m4", "machine", "machine language", "malbolge", "maple", "matlab", "m-code", "mercury", "ml",
                     "modula-2", "mondrian", "mql4", "msl",
                     "natural",
                     "oberon", "objective-c", "objectpal", "object pascal", "ocaml", "opencl", "openedge abl", "oz",
                     "pascal", "pawn", "perl", "php", "piet", "pl/1", "pl/i", "pl/sql", "pl/pgsql", "postscript",
                     "powerbasic", "powerbuilder", "powershell", "processing", "progress", "prolog", "providex",
                     "purebasic", "python",
                     "q#", "qbasic",
                     "r", "raku", "rexx", "ring", "rpg", "ruby", "rust",
                     "sas", "scala", "sed", "scheme", "scratch", "scratch jr.", "seed7", "self", "simula", "smalltalk",
                     "smallbasic", "snobol", "solidity", "spark", "spss", "sql", "stata", "swift",
                     "tcl", "tex", "ti-basic", "transact-sql", "t-sql", "turbobasic", "turbo c", "turbo pascal",
                     "typescript",
                     "ubasic",
                     "vala", "vala/genie", "vb", "vbs", "vbscript", "verilog", "vhdl", "visual basic", "visual c",
                     "visual foxpro", "visual objects", "vbscripts", "whitespace",
                     "xslt", "xquery",
                     "yaml"]
    language_list_col = array(*[lit(x) for x in language_list])
    platform_list = ["arthur", "arx", "mos", "risc-ix", "risc-os", "amigaos", "amigaos-1.0-3.9", "amigaos-4",
                     "amiga-unix", "amsdos", "contiki", "cp-m-2.2", "cp-m-plus", "symbos", "apple-ii", "apple-dos",
                     "apple-pascal", "prodos", "gs-os", "gno-me", "apple-iii", "apple-sos", "apple-lisa",
                     "apple-macintosh", "classic-mac-os", "a-ux", "copland", "mklinux", "pink", "rhapsody", "macos",
                     "macos-server", "apple-network-server", "ibm-aix", "apple-messagepad", "newton-os", "iphone",
                     "ios", "ipad", "ipados", "apple-watch", "watchos", "apple-tv", "tvos", "a-rose", "ipod-software",
                     "netbsd", "domain-os", "atari-dos", "atari-tos", "atari-multitos", "xts-400", "beos", "beia",
                     "beos-r5.1d0", "magnussoft-zeta", "unix", "unix-time-sharing-system-v6", "pwb-unix", "cb-unix",
                     "unix-time-sharing-system-v7", "unix-system-iii", "unix-system-v", "unix-time-sharing-system-v8",
                     "unix-time-sharing-system-v9", "unix-time-sharing-system-v10", "besys", "plan-9-from-bell-labs",
                     "inferno", "burroughs-mcp", "chippewa-operating-system", "kronos", "nos", "scope", "puffin-os",
                     "convergent-technologies-operating-system", "cromemco-dos", "cromix", "aos", "dg-ux", "rdos",
                     "datapoint-2200", "datapoint", "deos", "heartos", "cp-m", "personal-cp-m", "cp-m-68k", "cp-m-8000",
                     "cp-m-86", "cp-m-86-plus", "personal-cp-m-86", "mp-m", "mp-m-ii", "mp-m-86", "mp-m-8-16",
                     "concurrent-cp-m", "concurrent-cp-m-86", "concurrent-cp-m-8-16", "concurrent-cp-m-68k", "dos",
                     "concurrent-dos", "concurrent-pc-dos", "concurrent-dos-8-16", "concurrent-dos-286",
                     "concurrent-dos-xm", "concurrent-dos-386", "concurrent-dos-386-mge", "concurrent-dos-68k",
                     "flexos", "flexos-186", "flexos-286", "siemens-s5-dos-mt", "ibm-4680-os", "ibm-4690-os",
                     "toshiba-4690-os", "flexos-386", "flexos-68k", "multiuser-dos", "cci-multiuser-dos",
                     "datapac-multiuser-dos", "datapac-system-manager", "ims-multiuser-dos", "real-32", "real-ng",
                     "dos-plus", "dr-dos", "palmdos", "star-trek", "novell-dos", "opendos", "batch-11-dos-11", "hp-ux",
                     "multi-programming-executive", "nonstop", "os-8", "rsts-e", "rsx-11", "rt-11", "tops-10", "tenex",
                     "tops-20", "digital-unix", "ultrix", "vms", "waits", "ose", "towns-os", "os-iv", "msp", "msp-ex",
                     "real-time-multiprogramming-operating-system", "gcos", "multics", "chromium-os", "chrome-os",
                     "container-optimized-os", "android", "glinux", "fuchsia", "integrity", "integrity-178b",
                     "u-velosity", "vulcan-o-s", "harris-unix", "hdos", "ht-11", "hp-multi-programming-executive",
                     "nonstop-os", "cp-6", "harmony-os", "irmx", "isis", "compatible-time-sharing-system",
                     "gm-os-&-gm-naa-i-o", "ibsys", "ijmon", "share-operating-system",
                     "university-of-michigan-executive-system", "os-360-and-successors", "os-360", "mft", "mft-ii",
                     "mvt", "system-370", "os-vs1", "multiple-virtual-storage", "mvs-xa", "mvs-esa", "os-390",
                     "phoenix-mvs", "z-os", "dos-360-and-successors", "bos-360", "tos-360", "dos-360", "dos-vs",
                     "dos-vse", "vse-sp", "z-vse", "cp-cms", "cp-40", "cp-67", "vm-370", "vm-xa", "virtual-machine",
                     "z-vm", "acp", "tpf", "z-tpf", "unix-like", "aix-370", "aix-esa", "opensolaris-for-system-z",
                     "uts", "linux-on-ibm-z", "mts", "tss-360", "music-sp", "orvyl-and-wylbur", "pc-dos", "os-2",
                     "os-2-warp", "ecomstation", "arcaos", "aix", "ibm-series-1", "edx", "rps", "cps", "serix",
                     "ibm-1130", "dms", "ibm-1800", "tsx", "mpx", "ibm-8100", "dpcx", "dppx", "ibm-system-3",
                     "ibm-system-34", "ibm-system-38", "cpf", "ibm-system-88", "stratus-vos", "as-400", "os-400",
                     "i5-os", "ibm-i", "workplace-os", "k42", "dynix", "j", "george", "executive", "tme", "icl-vme",
                     "vme-k", "remix-os", "lynxos", "microc-os-ii", "microc-os-iii", "xenix", "msx-dos", "ms-dos",
                     "dos-v", "windows", "windows-1.0", "windows-2.0", "windows-3.0", "windows-3.1x",
                     "windows-for-workgroups-3.1", "windows-3.2", "windows-for-workgroups-3.11", "windows-95",
                     "windows-98", "windows-millennium-edition", "windows-nt", "windows-nt-3.1", "windows-nt-3.5",
                     "windows-nt-3.51", "windows-nt-4.0", "windows-2000", "windows-xp", "windows-server-2003",
                     "windows-fundamentals-for-legacy-pcs", "windows-vista", "windows-azure", "windows-home-server",
                     "windows-server-2008", "windows-7", "windows-phone-7", "windows-server-2008-r2",
                     "windows-home-server-2011", "windows-server-2012", "windows-8", "windows-phone-8", "windows-8.1",
                     "windows-phone-8.1", "windows-server-2012-r2", "xbox-one-system-software", "windows-10",
                     "windows-10-mobile", "windows-server-2016", "windows-server-2019", "windows-ce", "windows-ce-3.0",
                     "windows-ce-5.0", "windows-ce-6.0", "windows-embedded-compact-7", "windows-embedded-compact-2013",
                     "windows-mobile", "singularity", "midori", "xbox-360-system-software", "azure-sphere", "threadx",
                     "altair-dos", "mobilinux", "tmx", "imos", "vrx", "es", "nextstep", "netware", "unixware",
                     "novell-supernos", "novell-corsair", "novell-expose", "open-enterprise-server", "rtxc-quadros",
                     "time-sharing-operating-system", "dspnano-rtos", "bada", "tizen", "sco-unix", "sco-open-desktop",
                     "sco-openserver", "berkeley-timesharing-system", "pikeos", "trsdos", "color-basic", "newdos-80",
                     "deskmate", "edos", "ti-rtos-kernel", "tron", "t-kernel", "exec-i", "exec-ii", "exec-8", "vs-9",
                     "wps", "ois", "vxworks", "z80-rio", "zorin-os", "lisp-machines--inc.", "symbolics",
                     "texas-instruments", "xerox", "andos", "csi-dos", "mk-dos", "pilot", "perq", "elbrus", "eos",
                     "elxsi", "mai-basic-four", "michigan-terminal-system", "es-evm", "pc-mos-386", "buran",
                     "sintran-iii", "skyos", "soda", "theos", "tsx-32", "dx10", "aegis", "coherent", "dc-osx", "dnix",
                     "helios", "interactive-unix", "irix", "meikos", "os-9", "os-9000", "osf-1", "openstep", "qnx",
                     "rmx", "sinix", "solaris", "sunos", "super-ux", "system-v", "system-v-at--386", "trusted-solaris",
                     "uniflex", "unicos", "zenix", "minix", "bsd", "freebsd", "dragonflybsd", "midnightbsd", "ghostbsd",
                     "trueos", "openbsd", "bitrig", "darwin", "gnu", "linux", "redox", "android-x86",
                     "cray-linux-environment", "opensolaris", "illumos", "openindiana", "nexenta-os", "smartos",
                     "rtems", "haiku", "syllable-desktop", "vsta", "plurix", "tunis", "dahliaos", "cosmos", "freedos",
                     "genode", "ghost-os", "its", "osfree", "osv", "phantom-os", "reactos", "sharpos", "templeos",
                     "visopsys", "research-unix", "amoeba", "croquet", "eros", "capros", "harmony", "helenos", "house",
                     "ilios", "l4", "mach", "nemesis", "spring", "the-multiprogramming-system", "thoth", "v", "verve",
                     "xinu", "86-dos", "dr-dos-startrek", "dr-dos-winbolt", "pts-dos", "turbodos", "desqview",
                     "x-windowing", "banyan-vines", "cambridge-ring", "cisco-ios", "cisco-nx-os", "ctos", "data-ontap",
                     "extremeware", "extremexos", "fabric-os", "junos", "network-operating-system",
                     "novell-open-enterprise-server", "plan-9", "blis-cobol", "bluebottle", "bs1000", "bs2000",
                     "bs3000", "flex9", "gem", "geos", "javaos", "jnode", "jx", "kernal", "merlin", "morphos",
                     "fujitsu", "oberon-(operating-system)", "osd-xc", "pick", "primos", "sinclair-qdos", "ssb-dos",
                     "symobi", "tripos", "ucsd-p-system", "vos", "vos3", "vm2000", "visi-on", "vps-vm", "aros",
                     "atheos", "baremetal", "dexos", "emutos", "lse-os", "menuetos", "kolibrios", "toaruos", "ponyos",
                     "serenityos", "dip-dos", "embedded-linux", "replicant", "lineageos",
                     "list-of-custom-android-distributions", "firefox-os", "angstrom-distribution", "familiar-linux",
                     "maemo", "openzaurus", "webos", "access-linux-platform", "openmoko-linux", "ophone", "meego",
                     "moblin", "motomagx", "qt-extended", "sailfish-os", "ubuntu-touch", "postmarketos", "magic-cap",
                     "palm-os", "pen-geos", "penpoint-os", "pvos", "symbian-os", "epoc", "pocket-pc", "windows-phone",
                     "ipodlinux", "iriver-clix", "rockbox", "blackberry-os", "symbian-platform", "blackberry-10",
                     "catos", "ios-xr", "lancom-systems", "openwrt", "dd-wrt", "lede", "gargoyle", "librecmc",
                     "zeroshell", "rtos", "m0n0wall", "opnsense", "pfsense", "apache-mynewt", "chibios-rt",
                     "erika-enterprise", "ecos", "nucleus-rtos", "nuttx", "ncos", "freertos--openrtos-and-safertos",
                     "openembedded", "psos", "rex-os", "riot", "rom-dos", "tinyos", "rt-thread", "windows-iot",
                     "windows-embedded", "wombat-os", "zephyr", "brickos", "lejos", "cambridge-cap-computer",
                     "flex-machine", "hydra", "keykos"]  # generated from util/platform_list.rb
    platform_list_col = array(*[lit(x) for x in platform_list])

    # TODO: this should use posthistory with posthistorytypeid==3, these are the initial tags.
    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet") \
        .select(["_Id", "_Tags"]) \
        .withColumn("_Tags", expr("substring(_Tags, 2, length(_Tags) - 2)")) \
        .withColumn("_Tags", split(col("_Tags"), "><")) \
        .withColumn("number_of_tags", when(size("_Tags") < 0, 0).otherwise(size("_Tags"))) \
        .withColumn("contains_language_tag", size(array_intersect("_Tags", language_list_col)) > 0) \
        .withColumn("contains_platform_tag", size(array_intersect("_Tags", platform_list_col)) > 0) \
        .drop("_Tags")

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    tag_info_df(spark).show()
