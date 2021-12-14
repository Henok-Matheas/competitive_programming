n = [6,4,1]

def bubble_sort(n):
    swap=0
    sorted = [0] * len(n)
    for i in range(len(n)):
        for j in range(len(n) - 1):
            if n[j] > n[j + 1]:
                swap+=1
                n[j],n[j + 1] = n[j + 1], n[j]
    return (n[0],n[-1],swap)

sorted= bubble_sort(n)
print(f"""
Array is sorted  in : {sorted[2]} swaps
First Element : {sorted[0]}
Last Element : {sorted[1]}
""")