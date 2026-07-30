# 

def infinite_generator():
    count = 1
    while True:
        yield f"#Refil : {count}"
        count += 1

serve_chai = infinite_generator()

for _ in range(2):
    print(next(serve_chai))