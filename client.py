import socket

student_id = "e2203027"
server_address = ("8.8.8.8", 80)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(student_id.encode(), server_address)
print(f"Sent {student_id} to 8.8.8.8:80")
s.close()
