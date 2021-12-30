from math import log2
import copy

#instr = '6053231004C12DC26D00526BEE728D2C013AC7795ACA756F93B524D8000AAC8FF80B3A7A4016F6802D35C7C94C8AC97AD81D30024C00D1003C80AD050029C00E20240580853401E98C00D50038400D401518C00C7003880376300290023000060D800D09B9D03E7F546930052C016000422234208CC000854778CF0EA7C9C802ACE005FE4EBE1B99EA4C8A2A804D26730E25AA8B23CBDE7C855808057C9C87718DFEED9A008880391520BC280004260C44C8E460086802600087C548430A4401B8C91AE3749CF9CEFF0A8C0041498F180532A9728813A012261367931FF43E9040191F002A539D7A9CEBFCF7B3DE36CA56BC506005EE6393A0ACAA990030B3E29348734BC200D980390960BC723007614C618DC600D4268AD168C0268ED2CB72E09341040181D802B285937A739ACCEFFE9F4B6D30802DC94803D80292B5389DFEB2A440081CE0FCE951005AD800D04BF26B32FC9AFCF8D280592D65B9CE67DCEF20C530E13B7F67F8FB140D200E6673BA45C0086262FBB084F5BF381918017221E402474EF86280333100622FC37844200DC6A8950650005C8273133A300465A7AEC08B00103925392575007E63310592EA747830052801C99C9CB215397F3ACF97CFE41C802DBD004244C67B189E3BC4584E2013C1F91B0BCD60AA1690060360094F6A70B7FC7D34A52CBAE011CB6A17509F8DF61F3B4ED46A683E6BD258100667EA4B1A6211006AD367D600ACBD61FD10CBD61FD129003D9600B4608C931D54700AA6E2932D3CBB45399A49E66E641274AE4040039B8BD2C933137F95A4A76CFBAE122704026E700662200D4358530D4401F8AD0722DCEC3124E92B639CC5AF413300700010D8F30FE1B80021506A33C3F1007A314348DC0002EC4D9CF36280213938F648925BDE134803CB9BD6BF3BFD83C0149E859EA6614A8C'
instr = 'EE00D40C823060'

def hex2bin(instr):
    return bin(int(instr, 16)) if instr else None

def bin2dec(instr):
    return int(instr, 2) if instr else None

class Packet:
    def __init__(self, version, type_id, value=None, contents=[]):
        self.version = bin2dec(version)
        self.type_id = bin2dec(type_id)
        self.value = bin2dec(value)
        self.contents = contents

    def __repr__(self):
        retstr = f'Packet: Ver: {self.version}, ID: {self.type_id}'
        if self.value: retstr += f', Val: {self.value}'
        if self.contents: retstr += f', Contents: {self.contents}'
        return retstr

def parse_packet(instr):
    vers = instr[:3]
    type_id = instr[3:6]
    currpack = Packet(vers, type_id)

    currpos = 6
    if currpack.type_id == 4: # literal
        valbytes = ''

        #start grabbing chunks of 5 bits until a chunk starts with 0
        while True:
            nextchunk = instr[currpos:currpos+5]
            valbytes += nextchunk[1:] # strip leading digit
            currpos += 5
            if nextchunk[0] == '0':
                break
        currpack.value = bin2dec(valbytes)
        remstr = instr[currpos:]
    else: # operator
        modebit = instr[6]
        if modebit == '0': # next 15 = # bits
            numbits = bin2dec(instr[7:22])
            remstr = instr[22:22+numbits]

            while remstr:
                if remstr.count('0') == len(remstr):
                    break
                subpack, remstr = parse_packet(remstr)
                currpack.contents.append(subpack)

        elif modebit == '1': # next 11 = # subpackets
            numloops = bin2dec(instr[7:18])
            remstr = instr[18:]

            for loop in range(numloops):
                subpack, remstr = parse_packet(remstr)
                currpack.contents.append(subpack)

    return currpack, remstr

def add_versions(inpacket, totalvers=0):
    totalvers += inpacket.version
    if not inpacket.contents:
        return totalvers
    else:
        for packet in inpacket.contents:
            totalvers += add_versions(packet, totalvers)

def main():
    bitcount = int(len(instr) * log2(16))
    binstr = bin(int(instr, 16))[2:].zfill(bitcount)
    packet, null = parse_packet(binstr)
    print(packet)
    #print(add_versions(packet))

if __name__ == '__main__':
    main()
