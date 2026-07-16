from rich import print

from nas_sentinel.banner import show_banner
from nas_sentinel.disk import DiskMonitor


def main():

    show_banner()

    ssd = DiskMonitor("/dev/sda")
    hdd = DiskMonitor("/dev/sdb")

    print()

    print("SSD")
    print("Exists :", ssd.exists())
    print("SMART  :", ssd.smart_supported())

    print()

    print("HDD")
    print("Exists :", hdd.exists())
    print("SMART  :", hdd.smart_supported())


if __name__ == "__main__":
    main()
