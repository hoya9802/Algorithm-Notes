import heapq

class Job():
    def __init__(self, time=0, cost=0):
        self.time = time
        self.cost = cost
        
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __le__(self, other):
        return self.cost <= other.cost

def solution(jobs):
    jobs.sort()
    
    next_idx = 1
    job_queue = [Job(jobs[0][0], jobs[0][1])]
    now = jobs[0][0]
    ans = 0
    
    while 1:
        while next_idx < len(jobs) and jobs[next_idx][0] <= now:
            job = Job(jobs[next_idx][0], jobs[next_idx][1])
            heapq.heappush(job_queue, job)
            next_idx += 1
        
        if len(job_queue) == 0:
            if next_idx < len(jobs):
                job = Job(jobs[next_idx][0], jobs[next_idx][1])
                heapq.heappush(job_queue, job)
                now = job.time
                next_idx += 1
            else:
                break
                
        next_job = heapq.heappop(job_queue)
        now += next_job.cost
        ans += (now - next_job.time)
    
    return ans // len(jobs)