#6883. 문서 통계
import sys
#(1 ≤ a, b ≤ 100)

document = sys.stdin.readline()
print(len(document.strip()))
print(len(''.join(document.split())))
print(len((document.split())))
