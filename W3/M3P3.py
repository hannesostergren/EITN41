from pcapfile import savefile
import random
import ipaddress

testcap = open('../cia.log.2.pcap', 'rb')
capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

#print the packets
#print ('timestamp\teth src\t\t\teth dst\t\t\tIP src\t\tIP dst')
for pkt in capfile.packets:
    timestamp = pkt.timestamp
    # all data is ASCII encoded (byte arrays). If we want to compare with strings
    # we need to decode the byte arrays into UTF8 coded strings
    # eth_src = pkt.packet.src.decode('UTF8')
    # eth_dst = pkt.packet.dst.decode('UTF8')
    # ip_src = pkt.packet.payload.src.decode('UTF8')
    # ip_dst = pkt.packet.payload.dst.decode('UTF8')
    # print ('{}\t\t{}\t{}\t{}\t{}'.format(timestamp, eth_src, eth_dst, ip_src, ip_dst))

def disclosure_attack(batches, num_partners):
    union_set = batches.copy().pop(0)
    disjoint_packs = [union_set]
    for batch in batches:
        if union_set.isdisjoint(batch):
            disjoint_packs.append(batch)
            union_set = union_set.union(batch)
    assert(len(disjoint_packs) == num_partners)

    return disjoint_packs

def learning_phase(ANIP, MixIP, num_partners):
    batches = list()
    current_batch = set()
    rec = False
    add = False
    for pkt in capfile.packets:
        if add and not pkt.packet.payload.src.decode('utf-8') == MixIP:
            batches.append(current_batch.copy())
            current_batch.clear()
            add = False
            rec = False
        if pkt.packet.payload.src.decode('utf-8') == ANIP:
            rec = True
        elif pkt.packet.payload.src.decode('utf-8') == MixIP and rec:
            add = True
            current_batch.add(pkt.packet.payload.dst.decode('utf-8'))
    disjoint_packs = disclosure_attack(batches, num_partners)
    return batches, disjoint_packs
        

def find_partners(batches, disjoint_packets):
    for batch in batches:
        for i, dis in enumerate(disjoint_packets):
            no_others = all(map(lambda a: batch.isdisjoint(a) or a == dis, disjoint_packets))
            if no_others and dis.intersection(batch):
                disjoint_packets[i] = dis.intersection(batch)
    
        if all(map(lambda a: len(a) == 1, disjoint_packets)):
            return disjoint_packets
    return None


def main(ANIP, MixIP, num_partners): 
    batches, disjoint_sets = learning_phase(ANIP, MixIP, num_partners)
    
    partners = find_partners(batches, disjoint_sets)
    print("partner_ip: ", *partners)
    sum_partner_ip = sum([int(ipaddress.ip_address(partner.pop())) for partner in partners])
    print("sum partner_ip", sum_partner_ip)

main("245.221.13.37", "15.24.22.93", 9)