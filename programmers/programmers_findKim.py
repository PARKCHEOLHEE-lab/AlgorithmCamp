# my code
seoul = ["Jane", "Jane", "Jane", "Kim", "Jane"]

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return (f"김서방은 {i}에 있다")

# best code
def find_kim(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다."
