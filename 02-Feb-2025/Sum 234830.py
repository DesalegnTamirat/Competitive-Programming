# Problem: Sum - https://codeforces.com/contest/1742/problem/A

for _ in range(int(input())):
  a, b, c = sorted(map(int, input().split()))
  print("YES" if a + b == c else "NO")