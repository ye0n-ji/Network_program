import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        return struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)

    def unpack_Udphdr(self, packet):
        return struct.unpack('!HHHH', packet)


# =========================
# 실행 부분
# =========================

udp = Udphdr(5555, 80, 1000, 0xFFFF)

packed = udp.pack_Udphdr()

# 🔥 1. hex 출력 (슬라이드 스타일)
print(binascii.b2a_hex(packed))

# 🔥 2. unpack 결과 출력
unpacked = udp.unpack_Udphdr(packed)
print(unpacked)

# 🔥 3. 최종 출력 형식
print(f"Source Port:{unpacked[0]} Destination Port:{unpacked[1]} "
      f"Length:{unpacked[2]} Checksum:{unpacked[3]}")