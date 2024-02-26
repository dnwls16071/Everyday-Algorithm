import heapq

def solution(operations):
    minHeap = []
    maxHeap = []
    for operation in operations:
        op = operation.split(" ")
        if op[0] == "I":
            heapq.heappush(minHeap, int(op[1]))
            heapq.heappush(maxHeap, -int(op[1]))
        else:
            if op[1] == "1":
                if maxHeap:
                    heapq.heappop(maxHeap)
                    minHeap = [-x for x in maxHeap]
                    heapq.heapify(minHeap)
            else:
                if minHeap:
                    heapq.heappop(minHeap)
                    maxHeap = [-x for x in minHeap]
                    heapq.heapify(maxHeap)
    if len(minHeap) != 0 and len(maxHeap) != 0:
        return [-maxHeap[0], minHeap[0]]
    else:
        return [0, 0]