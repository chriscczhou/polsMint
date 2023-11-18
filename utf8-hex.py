data = 'data:,{"p":"prc-20","op":"mint","tick":"pols","amt":"100000000"}'
# 将字符串转换为UTF-8编码的字节
utf8_bytes = data.encode('utf-8')
# 将字节转换为十六进制表示的字符串
hex_str = utf8_bytes.hex()
print("0x"+hex_str)