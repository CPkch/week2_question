from priority_queue import PriorityQueue
def main():
    PQ = PriorityQueue()
  
    PQ.push("Task 1", 3)
    PQ.push("Task 2", 1)
    PQ.push("Task 3", 2)
  
    print(PQ.pop())
    print(PQ.pop())
    print(PQ.pop())

if __name__ == "__main__":
    main()
