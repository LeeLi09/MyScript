import csv


def ip2int(ip):
    param = ip.split('.')
    base = 256 * 256 * 256
    ipint = 0
    for p in param:
        ipint += base * int(p)
        base /= 256
    return ipint


def getaddr(ip, ipList):
    ipint = ip2int(ip)

    start = 0
    end = len(ipList)

    while True:
        if start == end:
            break
        middle = int((start + end) / 2)
        if ipint >= ipList[middle][0] and ipint <= ipList[middle][1]:
            return ipList[middle][3]
        elif ipint < ipList[middle][0]:
            end = middle
        elif ipint > ipList[middle][1]:
            start = middle + 1
    return 'null'


if __name__ == "__main__":
    ipList = []
    with open("./T_GeoIP-generic_business-ipv4.txt", 'r') as f:
        geoList = f.read().split('\n')
        for item in geoList:
            param = item.split('\t')
            if len(param) > 5:
                param[0] = ip2int(param[0])
                param[1] = ip2int(param[1])
                ipList.append(param)
    getaddr('8.8.8.8', ipList)
