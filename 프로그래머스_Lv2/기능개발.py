from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    count = 0
    time = 0
    while progresses:
        if progresses[0] + speeds[0] * time >= 100:
            count += 1
            progresses.popleft()
            speeds.popleft()
        else:
            if count > 0:
                answer.append(count)
                count = 0

            time += 1

    answer.append(count)
    return answer

solution([93, 30, 55], [1, 30, 5])