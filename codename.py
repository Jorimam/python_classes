message = "GhostNet#X44CR#98.654#TRC8821"

code_name=message[:8]
message_code=message[9:14]
last_letter=message_code[-1]
trace_id=message[-7:]
severity_level=message[-14:-9]


print(f"CodeName:\t {code_name}")
print(f"Message:\t Code {message_code}")
print(f"Last letter: \t{last_letter}")
print(f"Trace ID:\t{trace_id}")
print(f"Traceable:\t YES")
print(f"Severity:\t{severity_level}")
'''CodeName: GhostNet
  MessageCode: X44CR
  lastletter: R
  TraceID: TRC8821
 Traceable: Yes
  severitylevel: 98.65
'''
print("________________")
message=message.split("#")
print(f"Code Name:\t {message[0]}")
print(f"Message:\t {message[1]}")
print(f"Trace Id:\t {message[3]}")
print(f"Traceable:\t YES")
print(f"Severity:\t {message[2]}")

print(message[2][2] )
