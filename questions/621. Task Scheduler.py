class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap) #max heap containing values

        q = collections.deque() #list of [-cnt, time]

        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt =  1 + heapq.heappop(maxHeap)

                if cnt:
                    q.append([cnt, time + n])

            
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])

        
        return time



        
