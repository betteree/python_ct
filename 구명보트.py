function solution(people, limit) {
    var answer = 0;
    people.sort((a, b) => a - b);
    
    let i = 0;           // 가장 가벼운 사람을 가리키는 포인터
    let j = people.length - 1; // 가장 무거운 사람을 가리키는 포인터
    
    while (i <= j) {
        // 가장 가벼운 사람과 무거운 사람을 함께 태울 수 있는 경우
        if (people[i] + people[j] <= limit) {
            i++; // 가벼운 사람을 태우고 인덱스 증가
        }
        // 무거운 사람을 보트에 태운 후 인덱스 감소
        j--;
        answer++; // 보트 개수 증가
    }
    
    return answer;
}
